# DigitalOcean VPS Setup for Headless WordPress (WPGraphQL)

This guide deploys a production-ready WordPress backend for VitalBloom.blog at `backend.vitalbloom.blog` and exposes GraphQL at `/graphql`.

## 1. Provision VPS + DNS

1. Create an Ubuntu 22.04 LTS droplet on DigitalOcean.
2. Create DNS `A` record:
   - Host: `backend`
   - Value: `<YOUR_DROPLET_PUBLIC_IP>`
3. SSH into server:

```bash
ssh root@<YOUR_DROPLET_PUBLIC_IP>
```

## 2. Base Server Hardening

```bash
apt update && apt upgrade -y
apt install -y ufw fail2ban curl gnupg2 ca-certificates lsb-release software-properties-common
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable
```

Create a deploy user:

```bash
adduser deploy
usermod -aG sudo deploy
rsync --archive --chown=deploy:deploy ~/.ssh /home/deploy
```

## 3A. LEMP Stack Install (Recommended)

### Install Nginx, MySQL, PHP

```bash
apt install -y nginx mysql-server
apt install -y php8.2-fpm php8.2-mysql php8.2-curl php8.2-gd php8.2-xml php8.2-mbstring php8.2-zip php8.2-intl php8.2-soap unzip
systemctl enable nginx php8.2-fpm mysql
```

### Secure MySQL + Create DB

```bash
mysql_secure_installation
mysql -u root -p
```

Inside MySQL:

```sql
CREATE DATABASE vitalbloom_wp DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'vitalbloom_user'@'localhost' IDENTIFIED BY 'CHANGE_STRONG_PASSWORD';
GRANT ALL PRIVILEGES ON vitalbloom_wp.* TO 'vitalbloom_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### Install WordPress

```bash
mkdir -p /var/www/backend.vitalbloom.blog
cd /tmp
curl -O https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
rsync -avP wordpress/ /var/www/backend.vitalbloom.blog/
chown -R www-data:www-data /var/www/backend.vitalbloom.blog
find /var/www/backend.vitalbloom.blog -type d -exec chmod 755 {} \;
find /var/www/backend.vitalbloom.blog -type f -exec chmod 644 {} \;
```

Create wp-config:

```bash
cd /var/www/backend.vitalbloom.blog
cp wp-config-sample.php wp-config.php
```

Edit DB credentials:

```bash
sed -i "s/database_name_here/vitalbloom_wp/" wp-config.php
sed -i "s/username_here/vitalbloom_user/" wp-config.php
sed -i "s/password_here/CHANGE_STRONG_PASSWORD/" wp-config.php
```

Add this extra hardening in `wp-config.php`:

```php
define('DISALLOW_FILE_EDIT', true);
define('FORCE_SSL_ADMIN', true);
```

### Configure Nginx

Create `/etc/nginx/sites-available/backend.vitalbloom.blog`:

```nginx
server {
    listen 80;
    server_name backend.vitalbloom.blog;

    root /var/www/backend.vitalbloom.blog;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.2-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

Enable site:

```bash
ln -s /etc/nginx/sites-available/backend.vitalbloom.blog /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

Complete WordPress web installer at:

- `http://backend.vitalbloom.blog`

## 3B. Docker Alternative (Optional)

Use this only if you prefer containerized ops.

```bash
apt install -y docker.io docker-compose-plugin
mkdir -p /opt/vitalbloom-wordpress && cd /opt/vitalbloom-wordpress
```

Create `compose.yaml`:

```yaml
services:
  db:
    image: mysql:8
    restart: always
    environment:
      MYSQL_DATABASE: vitalbloom_wp
      MYSQL_USER: vitalbloom_user
      MYSQL_PASSWORD: CHANGE_STRONG_PASSWORD
      MYSQL_ROOT_PASSWORD: CHANGE_ROOT_PASSWORD
    volumes:
      - db_data:/var/lib/mysql

  wordpress:
    image: wordpress:php8.2-fpm
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: vitalbloom_user
      WORDPRESS_DB_PASSWORD: CHANGE_STRONG_PASSWORD
      WORDPRESS_DB_NAME: vitalbloom_wp
    volumes:
      - wp_data:/var/www/html

  nginx:
    image: nginx:stable
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - wp_data:/var/www/html:ro

volumes:
  db_data:
  wp_data:
```

Start:

```bash
docker compose up -d
```

## 4. SSL with Let's Encrypt

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d backend.vitalbloom.blog --redirect -m admin@vitalbloom.blog --agree-tos --no-eff-email
systemctl status certbot.timer
```

Verify renewal:

```bash
certbot renew --dry-run
```

## 5. Install Required WordPress Plugins

From WP Admin -> Plugins -> Add New, install and activate:

1. `WPGraphQL`
2. `Rank Math SEO` (or `Yoast SEO`)
3. `WPGraphQL SEO`

## 6. WPGraphQL Validation

Confirm GraphQL endpoint:

```bash
curl -X POST https://backend.vitalbloom.blog/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"{ posts(first: 1) { nodes { id slug title } } }"}'
```

## 7. Connect Frontend (VitalBloom.blog)

Set frontend environment:

- `NEXT_PUBLIC_CMS_API_URL=https://backend.vitalbloom.blog/graphql`
- `CMS_PREVIEW_SECRET=<strong-random-secret>`
- `WORDPRESS_AUTH_REFRESH_TOKEN=<optional-for-preview-flow>`

Rebuild frontend after env updates:

```bash
npm install
npm run build
npm run start
```

## 8. Webhook Revalidation (Later)

When WordPress publish/update event fires, call frontend endpoint:

```text
POST https://vitalbloom.blog/api/revalidate?secret=<CMS_PREVIEW_SECRET>
Body JSON: { "path": "/your-post-slug" }
```

## 9. Production Checklist

1. Disable XML-RPC unless required.
2. Limit login attempts / add WAF plugin or Cloudflare.
3. Enable daily DB backups and weekly offsite backups.
4. Keep WordPress core/plugins updated.
5. Restrict GraphQL introspection in production if policy requires.
