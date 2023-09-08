# Schema for the main results json
results_schema = {
    "type": "object",

    "properties": {
        "results_found": {
            "type": "number"
        },
        "results_start": {
            "type": "number"
        },
        "results_shown": {
            "type": "number"
        },
        "restaurants": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "restaurant": {
                        "type": "object"
                    }
                }
            }
        }               
    },

    "required": [
        "results_found",
        "results_start",
        "results_shown",
        "restaurants"
    ]
}

# Schema for each restaurant field
restaurants_schema = {
    "type": "object",

    "properties": {
        "restaurant": {
            "type": "object",
            "properties": {
                "R": {
                    "type": "object",
                    "properties": {
                        "res_id": {"type": "number"}
                    },
                    "required": [
                        "res_id"
                    ]
                },
                "apikey": {"type": "string"},
                "id": {"type": "string"},
                "name": {"type": "string"},
                "url": {"type": "string", "format": "uri"},
                "location": {
                    "type": "object",
                    "properties": {
                        "address": {"type": "string"},
                        "locality": {"type": "string"},
                        "city": {"type": "string"},
                        "city_id": {"type": "number"},
                        "latitude": {"type": "string"},
                        "longitude": {"type": "string"},
                        "zipcode": {"type": "string"},
                        "country_id": {"type": "number"},
                        "locality_verbose": {"type": "string"}
                    },
                    "required": [
                        "city", 
                        "country_id"
                    ]
                },
                "switch_to_order_menu": {"type": "number"},
                "cuisines": {"type": "string"},
                "average_cost_for_two": {"type": "number"},
                "price_range": {"type": "number"},
                "currency": {"type": "string"},
                "offers": {"type": "array"},
                "zomato_events": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "event": {
                                "type": "object"
                            }
                        }
                    }
                },
                "opentable_support": {"type": "number"},
                "is_zomato_book_res": {"type": "number"},
                "mezzo_provider": {"type": "string"},
                "is_book_form_web_view": {"type": "number"},
                "book_form_web_view_url": {"type": "string"},
                "book_again_url": {"type": "string"},
                "thumb": {"type": "string"},
                "user_rating": {
                    "type": "object",
                    "properties": {
                        "aggregate_rating": {"anyOf": [{"type": "string"},{"type": "number"}]},
                        "rating_text": {"type": "string"},
                        "rating_color": {"type": "string"},
                        "votes": {"anyOf": [{"type": "string"},{"type": "number"}]},
                        "has_fake_reviews": {"type": "number"}
                    },
                    "required": [
                        "aggregate_rating", 
                        "rating_text", 
                        "votes"
                    ]
                },
                "photos_url": {"type": "string", "format": "uri"},
                "menu_url": {"type": "string", "format": "uri"},
                "featured_image": {"type": "string"},
                "has_online_delivery": {"type": "number"},
                "is_delivering_now": {"type": "number"},
                "has_fake_reviews": {"type": "number"},
                "include_bogo_offers": {"type": "boolean"},
                "deeplink": {"type": "string"},
                "is_table_reservation_supported": {"type": "number"},
                "has_table_booking": {"type": "number"},
                "events_url": {"type": "string", "format": "uri"},
                "establishment_types": {"type": "array"}
            },
            "required": [
                "id",
                "name", 
                "location", 
                "cuisines", 
                "user_rating", 
            ]
        }
    },
    "required": ["restaurant"]
}


# Schema for each event field in a restaurant record (if any)
events_schema = {
    "type": "object",

    "properties": {
        "event_id": {"type": "number"},
        "friendly_start_date": {"type": "string"},
        "friendly_end_date": {"type": "string"},
        "friendly_timing_str": {"type": "string"},
        "start_date": {"type": "string", "format": "date"},
        "end_date": {"type": "string", "format": "date"},
        "end_time": {"type": "string", "pattern": "^(?:[01]\\d|2[0-3]):[0-5]\\d:[0-5]\\d$"},
        "start_time": {"type": "string", "pattern": "^(?:[01]\\d|2[0-3]):[0-5]\\d:[0-5]\\d$"},
        "is_active": {"type": "number"},
        "date_added": {"type": "string", "format": "date-time"},
        "photos": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "photo": {
                        "type": "object",
                        "properties": {
                            "url": {"type": "string", "format": "uri"},
                            "thumb_url": {"type": "string", "format": "uri"},
                            "order": {"type": "number"},
                            "md5sum": {"type": "string"},
                            "id": {"type": "number"},
                            "photo_id": {"type": "number"},
                            "uuid": {"type": "number"},
                            "type": {"type": "string"}
                        },
                        "required": [
                            "url"
                        ]
                    }
                },
                "required": [
                    "photo"
                ]
            }
        },
        "restaurants": {"type": "array"},
        "is_valid": {"type": "number"},
        "share_url": {"type": "string", "format": "uri"},
        "show_share_url": {"type": "number"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "display_time": {"type": "string"},
        "display_date": {"type": "string"},
        "is_end_time_set": {"type": "number"},
        "disclaimer": {"type": "string"},
        "event_category": {"type": "number"},
        "event_category_name": {"type": "string"},
        "book_link": {"type": "string"},
        "types": {"type": "array"},
        "share_data": {
            "type": "object",
            "properties": {
                "should_show": {"type": "number"}
            },
        }
    },
    "required": [
        "event_id", 
        "photos", 
        "title",
        "start_date",
        "end_date"
    ]
}

