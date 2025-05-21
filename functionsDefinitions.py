TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "greetings",
            "description": "Greets the client and tells him how he can help.",
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
            "name": "get_photo_recommendations",
            "description": "Look for the recommended features when making a photo campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "family": {
                        "type": "string",
                        "description": "Family to which the product belongs."
                    }
                },
                "required": ["family"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_instructions",
            "description": "Generates the necessary instructions to carry out the photographic campaign based on the desired characteristics.",
            "parameters": {
                "type": "object",
                "properties": {
                    "instructions": {
                        "type": "string",
                        "description": "Desired characteristics."
                    }
                },
                "required": ["instructions"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_images",
            "description": "Generates example images from desired features.",
            "parameters": {
                "type": "object",
                "properties": {
                    "features": {
                        "type": "string",
                        "description": "Desired characteristics."
                    }
                },
                "required": ["features"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_html",
            "description": "Genra un documento html",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "title": "The document title."
                    },
                    "text": {
                        "type": "string",
                        "title": "The document title."
                    },
                    "images": {
                        "type": "array",
                        "description": "The images to include in the document.",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["title", "text", "images"],
                "additionalProperties": False
            }
        }
    },
]