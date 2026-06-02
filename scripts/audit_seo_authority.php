<?php

$posts = get_posts([
    'post_type' => 'post',
    'post_status' => 'publish',
    'numberposts' => -1,
    'orderby' => 'date',
    'order' => 'DESC',
]);

$site_url = home_url();
$host = parse_url($site_url, PHP_URL_HOST);
$items = [];

foreach ($posts as $post) {
    $html = $post->post_content;
    $text = wp_strip_all_tags($html);

    preg_match_all("/\b[[:alnum:]][[:alnum:]'-]*\b/u", $text, $words);
    preg_match_all('/<h2\b/i', $html, $h2);
    preg_match_all('/<h3\b/i', $html, $h3);
    preg_match_all('/<p\b/i', $html, $paragraphs);
    preg_match_all('/<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)<\/a>/is', $html, $links, PREG_SET_ORDER);

    $internal_links = [];
    $external_links = [];
    foreach ($links as $link) {
        $href = html_entity_decode($link[1]);
        $anchor = trim(wp_strip_all_tags($link[2]));
        $link_host = parse_url($href, PHP_URL_HOST);
        $is_internal = str_starts_with($href, '/') || $link_host === $host || $link_host === 'www.vitalbloom.blog' || $link_host === 'vitalbloom.blog';
        $target = $href;
        if ($link_host === $host || $link_host === 'www.vitalbloom.blog' || $link_host === 'vitalbloom.blog') {
            $target = parse_url($href, PHP_URL_PATH) ?: $href;
        }
        $record = [
            'href' => $target,
            'anchor' => $anchor,
        ];
        if ($is_internal) {
            $internal_links[] = $record;
        } else {
            $external_links[] = $record;
        }
    }

    $sources = json_decode(get_post_meta($post->ID, '_vitalbloom_sources', true), true);
    $yoast_title = get_post_meta($post->ID, '_yoast_wpseo_title', true);
    $yoast_desc = get_post_meta($post->ID, '_yoast_wpseo_metadesc', true);
    $focus_keyword = get_post_meta($post->ID, '_yoast_wpseo_focuskw', true);
    $fact_checked_by = get_post_meta($post->ID, '_vitalbloom_fact_checked_by', true);
    $fact_checked_at = get_post_meta($post->ID, '_vitalbloom_fact_checked_at', true);
    $categories = wp_get_post_terms($post->ID, 'category', ['fields' => 'names']);

    $items[] = [
        'id' => $post->ID,
        'title' => html_entity_decode($post->post_title),
        'slug' => $post->post_name,
        'url' => get_permalink($post),
        'categories' => $categories,
        'word_count' => count($words[0]),
        'h2_count' => count($h2[0]),
        'h3_count' => count($h3[0]),
        'paragraph_count' => count($paragraphs[0]),
        'internal_links' => $internal_links,
        'external_links' => $external_links,
        'source_count' => is_array($sources) ? count($sources) : 0,
        'has_sources' => is_array($sources) && count($sources) > 0,
        'yoast_title' => $yoast_title,
        'yoast_description' => $yoast_desc,
        'focus_keyword' => $focus_keyword,
        'fact_checked_by' => $fact_checked_by,
        'fact_checked_at' => $fact_checked_at,
        'has_featured_image' => has_post_thumbnail($post->ID),
        'modified_gmt' => $post->post_modified_gmt,
        'published_gmt' => $post->post_date_gmt,
    ];
}

echo wp_json_encode([
    'generated_at' => gmdate('c'),
    'site_url' => $site_url,
    'post_count' => count($items),
    'posts' => $items,
], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
