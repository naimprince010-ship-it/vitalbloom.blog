<?php

$posts = get_posts([
    'post_type' => 'post',
    'post_status' => 'publish',
    'numberposts' => -1,
    'orderby' => 'date',
    'order' => 'DESC',
]);

echo "slug,words,h2,h3,paragraphs,sources\n";

foreach ($posts as $post) {
    $html = $post->post_content;
    $text = wp_strip_all_tags($html);

    preg_match_all("/\b[[:alnum:]][[:alnum:]'-]*\b/u", $text, $words);
    preg_match_all('/<h2\b/i', $html, $h2);
    preg_match_all('/<h3\b/i', $html, $h3);
    preg_match_all('/<p\b/i', $html, $paragraphs);

    $sources = json_decode(get_post_meta($post->ID, '_vitalbloom_sources', true), true);
    $source_count = is_array($sources) ? count($sources) : 0;

    echo implode(',', [
        $post->post_name,
        count($words[0]),
        count($h2[0]),
        count($h3[0]),
        count($paragraphs[0]),
        $source_count,
    ]) . "\n";
}
