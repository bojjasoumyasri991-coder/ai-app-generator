def validate_schema(schema: dict):
    required_keys = ["ui", "api", "database", "auth", "business_logic"]

    missing = [key for key in required_keys if key not in schema]

    if missing:
        return {
            "valid": False,
            "error": f"Missing keys: {missing}"
        }

    return {"valid": True}