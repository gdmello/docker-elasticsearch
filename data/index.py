mappings = {"mappings": {
    "app": {
        "properties": {
            "description": {
                "type": "string"
            },
            "links": {
                "properties": {
                    "self": {
                        "properties": {
                            "href": {
                                "index": "not_analyzed",
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "name": {
                "fields": {
                    "raw": {
                        "index": "not_analyzed",
                        "type": "string"
                    }
                },
                "type": "string"
            },
            "type": {
                "type": "string"
            }
        }
    }
}}

settings = {
    "settings": {
        "number_of_replicas": 0
    }
}