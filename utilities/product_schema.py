product_schema = {
    "type": "object",

    "properties": {
        "data": {
            "type": "array",

            "items": {
                "type": "object",

                "properties": {
                    "_id": {
                        "type": "string"
                    },
                    "productName": {
                        "type": "string"
                    },
                    "productPrice": {
                        "type": "integer"
                    },
                    "productStatus": {
                        "type": "boolean"
                    }
                },

                "required": [
                    "_id",
                    "productName",
                    "productPrice",
                    "productStatus"
                ]
            }
        },

        "count": {
            "type": "integer"
        },

        "message": {
            "type": "string"
        }
    },

    "required": [
        "data",
        "count",
        "message"
    ]
}