def generate_schema(design: dict):
    entities = design.get("entities", [])
    roles = design.get("roles", ["Admin", "User"])

    db_schema = {
        "tables": {},
        "relations": []
    }

    api_schema = {"endpoints": []}

    ui_schema = {"pages": []}

    # ---------------- DATABASE + API + UI ---------------- #

    for entity in entities:

        if entity == "User":
            db_schema["tables"]["users"] = ["id", "email", "password", "role"]

            api_schema["endpoints"].append({
                "path": "/login",
                "method": "POST",
                "request": ["email", "password"],
                "response": ["token"]
            })

            ui_schema["pages"].append({
                "name": "login",
                "components": ["form", "email_input", "password_input"]
            })

        elif entity == "Contact":
            db_schema["tables"]["contacts"] = ["id", "name", "user_id"]

            db_schema["relations"].append("contacts.user_id -> users.id")

            api_schema["endpoints"].append({
                "path": "/contacts",
                "method": "GET"
            })

            ui_schema["pages"].append({
                "name": "contacts",
                "components": ["table", "add_contact_button"]
            })

        elif entity == "Analytics":
            db_schema["tables"]["analytics"] = ["id", "data", "created_at"]

            api_schema["endpoints"].append({
                "path": "/analytics",
                "method": "GET",
                "access": "Admin only"
            })

            ui_schema["pages"].append({
                "name": "dashboard",
                "components": ["charts", "summary_cards"]
            })

        elif entity == "Subscription":
            db_schema["tables"]["subscriptions"] = ["id", "user_id", "plan"]

            db_schema["relations"].append("subscriptions.user_id -> users.id")

            api_schema["endpoints"].append({
                "path": "/subscribe",
                "method": "POST"
            })

        elif entity == "Post":
            db_schema["tables"]["posts"] = ["id", "title", "content", "user_id"]

            db_schema["relations"].append("posts.user_id -> users.id")

            api_schema["endpoints"].append({
                "path": "/posts",
                "method": "GET"
            })

            ui_schema["pages"].append({
                "name": "posts",
                "components": ["feed", "create_post"]
            })

        elif entity == "Product":
            db_schema["tables"]["products"] = ["id", "name", "price"]

            api_schema["endpoints"].append({
                "path": "/products",
                "method": "GET"
            })

            ui_schema["pages"].append({
                "name": "products",
                "components": ["catalog"]
            })

        elif entity == "Order":
            db_schema["tables"]["orders"] = ["id", "user_id", "product_id"]

            db_schema["relations"].append("orders.user_id -> users.id")
            db_schema["relations"].append("orders.product_id -> products.id")

            api_schema["endpoints"].append({
                "path": "/orders",
                "method": "GET"
            })

            ui_schema["pages"].append({
                "name": "orders",
                "components": ["order_list"]
            })

    # ---------------- AUTH ---------------- #

    auth_schema = {
        "roles": roles,
        "permissions": {
            "Admin": ["view_analytics", "manage_users"],
            "User": ["view_contacts"]
        }
    }

    # ---------------- BUSINESS LOGIC ---------------- #

    business_logic = [
        "Only admins can access analytics",
        "Users can only access their own data",
        "Login required for all operations"
    ]

    return {
        "database": db_schema,
        "api": api_schema,
        "ui": ui_schema,
        "auth": auth_schema,
        "business_logic": business_logic
    }