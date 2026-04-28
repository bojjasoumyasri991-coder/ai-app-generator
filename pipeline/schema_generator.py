def generate_schema(design: dict):
    entities = design.get("entities", [])

    db_schema = {"tables": {}}
    api_schema = {"endpoints": []}
    ui_schema = {"pages": []}

    for entity in entities:

        if entity == "User":
            db_schema["tables"]["users"] = ["id", "email", "password"]
            api_schema["endpoints"].append({"path": "/login", "method": "POST"})
            ui_schema["pages"].append("login")

        elif entity == "Contact":
            db_schema["tables"]["contacts"] = ["id", "name", "user_id"]
            api_schema["endpoints"].append({"path": "/contacts", "method": "GET"})
            ui_schema["pages"].append("contacts")

        elif entity == "Analytics":
            db_schema["tables"]["analytics"] = ["id", "data"]
            api_schema["endpoints"].append({"path": "/analytics", "method": "GET"})
            ui_schema["pages"].append("dashboard")

        elif entity == "Subscription":
            db_schema["tables"]["subscriptions"] = ["id", "user_id", "plan"]
            api_schema["endpoints"].append({"path": "/subscribe", "method": "POST"})

        elif entity == "Post":
            db_schema["tables"]["posts"] = ["id", "title", "content", "user_id"]
            api_schema["endpoints"].append({"path": "/posts", "method": "GET"})
            ui_schema["pages"].append("posts")

        elif entity == "Product":
            db_schema["tables"]["products"] = ["id", "name", "price"]
            api_schema["endpoints"].append({"path": "/products", "method": "GET"})
            ui_schema["pages"].append("products")

        elif entity == "Order":
            db_schema["tables"]["orders"] = ["id", "user_id", "product_id"]
            api_schema["endpoints"].append({"path": "/orders", "method": "GET"})
            ui_schema["pages"].append("orders")

    # Remove duplicates
    ui_schema["pages"] = list(set(ui_schema["pages"]))

    return {
        "database": db_schema,
        "api": api_schema,
        "ui": ui_schema
    }