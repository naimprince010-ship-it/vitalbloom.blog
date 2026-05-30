<?php
/**
 * Plugin Name: VitalBloom GraphQL Meta
 * Description: Exposes VitalBloom editorial reference metadata to WPGraphQL.
 */

add_action('graphql_register_types', function () {
    $fields = [
        'vitalbloomSources' => '_vitalbloom_sources',
        'vitalbloomFactCheckedBy' => '_vitalbloom_fact_checked_by',
        'vitalbloomFactCheckedAt' => '_vitalbloom_fact_checked_at',
        'vitalbloomReviewedBy' => '_vitalbloom_reviewed_by',
        'vitalbloomReviewedAt' => '_vitalbloom_reviewed_at',
    ];

    foreach ($fields as $field_name => $meta_key) {
        register_graphql_field('Post', $field_name, [
            'type' => 'String',
            'resolve' => function ($post) use ($meta_key) {
                return get_post_meta($post->ID, $meta_key, true) ?: null;
            },
        ]);
    }
});

add_action('init', function () {
    $meta_keys = [
        '_vitalbloom_sources',
        '_vitalbloom_fact_checked_by',
        '_vitalbloom_fact_checked_at',
        '_vitalbloom_reviewed_by',
        '_vitalbloom_reviewed_at',
    ];

    foreach ($meta_keys as $meta_key) {
        register_post_meta('post', $meta_key, [
            'auth_callback' => function () {
                return current_user_can('edit_posts');
            },
            'show_in_rest' => true,
            'single' => true,
            'type' => 'string',
        ]);
    }
});
