def design_system(intent: dict):
    modules = [m.lower() for m in intent.get("modules", [])]
    features = [f.lower() for f in intent.get("features", [])]

    entities = set()

    # -------------------------
    # Core mappings
    # -------------------------
    if any("login" in x or "auth" in x for x in modules + features):
        entities.add("User")

    if any("contact" in x for x in modules):
        entities.add("Contact")

    if any("dashboard" in x or "analytics" in x for x in modules):
        entities.add("Analytics")

    if any("payment" in x or "subscription" in x for x in modules):
        entities.add("Subscription")

    # -------------------------
    # Blogging detection
    # -------------------------
    if any("blog" in x or "post" in x for x in modules + features):
        entities.add("Post")
        entities.add("User")

    # -------------------------
    # E-commerce detection
    # -------------------------
    if any("product" in x or "cart" in x or "order" in x for x in modules + features):
        entities.add("Product")
        entities.add("Order")
        entities.add("User")

    # -------------------------
    # Fallback for vague prompts
    # -------------------------
    if not entities:
        entities.update(["User", "Analytics"])

    return {
        "entities": list(entities),
        "roles": intent.get("roles", []),
        "features": intent.get("features", [])
    }