TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for provided coordinates in celsius.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"}
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "verify_identity",
            "description": "Verifies the customer's identity using Mango Likes you account mail.",
            "parameters": {
                "type": "object",
                "properties": {
                    "mly_email": {
                        "type": "string",
                        "description": "Customer's Mango Likes You account mail."
                    }
                },
                "required": ["mly_email"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "ask_clarification",
            "description": "Prompts the customer for clarification on their request.",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to ask the customer."
                    }
                },
                "required": ["prompt"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_orders",
            "description": "Retrieves all customer order ids based on the Mango Likes You user id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "mly_user_id": {
                        "type": "string",
                        "description": "Customer's Mango Likes You user id."
                    }
                },
                "required": ["mly_user_id"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_order_by_id",
            "description": "Retrieves the information of an order from its order id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Order id."
                    }
                },
                "required": ["order_id"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "return_order",
            "description": "Mark an order as returned from its order id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Order id."
                    }
                },
                "required": ["order_id"],
                "additionalProperties": False
            }
        }
    },
    # Functions for handling FAQs
    {
        "type": "function",
        "function": {
            "name": "get_stores_information",
            "description": "Informs the user about opening hours, location and contact information of Mango stores.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False
            }
        }
    },
        {
        "type": "function",
        "function": {
            "name": "get_mly_information",
            "description": "Informs the user about the conditions of the Mango Likes You loyalty club.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False
            }
        }
    },
    # Final case resolution function
    {
        "type": "function",
        "function": {
            "name": "case_resolution",
            "description": "Finalizes and closes the customer case with all resolution details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "mly_email": {"type": "string", "description": "Customer's Mango Likes You account mail."},
                    "resolution_details": {"type": "string", "description": "Details of how the case was resolved."}
                },
                "required": ["mly_email", "resolution_details"],
                "additionalProperties": False
            }
        }
    }
]