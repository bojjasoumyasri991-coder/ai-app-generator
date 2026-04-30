def generate_schema(intent):
    return {
        "api": {
            "endpoints": [
                {"method": "POST", "path": "/login", "access": "public"},
                {"method": "GET", "path": "/contacts", "access": "user"},
                {"method": "POST", "path": "/contacts", "access": "user"},
                {"method": "GET", "path": "/dashboard", "access": "admin"},
            ]
        },
        "database": {
            "tables": [
                {"name": "users", "fields": ["id", "email", "password", "role"]},
                {"name": "contacts", "fields": ["id", "user_id", "name", "email"]}
            ]
        },
        "auth": {
            "roles": ["admin", "user"],
            "permissions": {
                "admin": ["view_dashboard", "manage_users"],
                "user": ["view_contacts", "add_contacts"]
            }
        },
        "business_logic": [
            "Users must login",
            "Users manage their own contacts",
            "Admins can view analytics",
            "Premium users get extra features"
        ]
    }