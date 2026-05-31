<?php
/**
 * Plugin Name: VitalBloom Backend Noindex
 * Description: Keeps the headless WordPress backend out of public search results.
 */

add_action('send_headers', function () {
    header('X-Robots-Tag: noindex, nofollow', true);
});

add_action('wp_head', function () {
    echo "<meta name=\"robots\" content=\"noindex,nofollow\" />\n";
}, 1);

add_filter('robots_txt', function () {
    return "User-agent: *\nDisallow: /\n";
}, 999);
