def repair_schema(schema: dict, errors: list):
    db_tables = schema["database"]["tables"]
    api_endpoints = schema["api"]["endpoints"]

    for error in errors:

        if "contacts table missing" in error:
            db_tables["contacts"] = ["id", "name", "user_id"]

        if "users table missing" in error:
            db_tables["users"] = ["id", "email", "password"]

        if "analytics table missing" in error:
            db_tables["analytics"] = ["id", "data"]

        if "/contacts API missing" in error:
            api_endpoints.append({"path": "/contacts", "method": "GET"})

        if "/login API missing" in error:
            api_endpoints.append({"path": "/login", "method": "POST"})

        if "/analytics API missing" in error:
            api_endpoints.append({"path": "/analytics", "method": "GET"})

    return schema