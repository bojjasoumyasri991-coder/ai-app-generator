def repair_schema(data):
    if "error" in data:
        return {
            "ui": {"pages": []},
            "api": {"endpoints": []},
            "database": {"tables": []},
            "auth": {"roles": [], "permissions": {}},
            "business_logic": []
        }
    return data