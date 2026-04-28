from pipeline.intent import extract_intent
from pipeline.design import design_system
from pipeline.schema_generator import generate_schema
from pipeline.validator import validate_schema
from pipeline.repair import repair_schema

def run_pipeline(user_input: str):
    print("\n--- USER INPUT ---")
    print(user_input)

    intent = extract_intent(user_input)
    print("\n--- INTENT ---")
    print(intent)

    design = design_system(intent)
    print("\n--- DESIGN ---")
    print(design)

    schema = generate_schema(design)
    print("\n--- SCHEMA ---")
    print(schema)

    errors = validate_schema(schema)
    print("\n--- VALIDATION ERRORS ---")
    print(errors)

    if errors:
        schema = repair_schema(schema, errors)
        print("\n--- REPAIRED SCHEMA ---")
        print(schema)

    return schema


if __name__ == "__main__":
    user_input = "Build a CRM with login, contacts, dashboard, and admin analytics"

    final_output = run_pipeline(user_input)

    print("\n=== FINAL OUTPUT ===")
    print(final_output)