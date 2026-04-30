def generate_design(intent):
    return {
        "ui": {
            "pages": [
                {
                    "name": "Login",
                    "components": ["email_input", "password_input", "login_button"]
                },
                {
                    "name": "Dashboard",
                    "components": ["stats_cards", "charts", "activity_feed"]
                },
                {
                    "name": "Contacts",
                    "components": ["contact_list", "add_contact_form"]
                },
                {
                    "name": "Premium",
                    "components": ["plan_cards", "payment_form", "subscription_status"]
                }
            ]
        }
    }