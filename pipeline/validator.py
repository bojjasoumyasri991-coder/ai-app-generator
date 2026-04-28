def validate_schema(schema: dict):
    errors = []

    db_tables = schema.get("database", {}).get("tables", {})
    api_endpoints = schema.get("api", {}).get("endpoints", [])
    ui_pages = schema.get("ui", {}).get("pages", [])

    api_paths = [ep["path"] for ep in api_endpoints]

    # -------------------------
    # 1. API ↔ DB consistency
    # -------------------------
    for ep in api_endpoints:
        path = ep["path"]

        if path == "/contacts" and "contacts" not in db_tables:
            errors.append("API /contacts exists but contacts table missing")

        if path == "/login" and "users" not in db_tables:
            errors.append("API /login exists but users table missing")

        if path == "/analytics" and "analytics" not in db_tables:
            errors.append("API /analytics exists but analytics table missing")

    # -------------------------
    # 2. UI ↔ API consistency
    # -------------------------
    if "contacts" in ui_pages and "/contacts" not in api_paths:
        errors.append("UI contacts page exists but /contacts API missing")

    if "dashboard" in ui_pages and "/analytics" not in api_paths:
        errors.append("UI dashboard exists but /analytics API missing")

    if "login" in ui_pages and "/login" not in api_paths:
        errors.append("UI login exists but /login API missing")

    # -------------------------
    # 3. Empty checks
    # -------------------------
    if not db_tables:
        errors.append("Database schema is empty")

    if not api_endpoints:
        errors.append("API schema is empty")

    return errors