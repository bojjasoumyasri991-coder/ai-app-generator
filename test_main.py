from pipeline.intent import extract_intent
from pipeline.validator import validate_schema
from pipeline.repair import repair_schema

user_input = input("Enter your app idea:\n> ")

result = extract_intent(user_input)

validated = validate_schema(result)

if not validated["valid"]:
    result = repair_schema(result)

print("\n===== FINAL OUTPUT =====\n")
print(result)

print("\n===== VALIDATION =====\n")
print(validated)