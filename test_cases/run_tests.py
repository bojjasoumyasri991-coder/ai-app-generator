import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import run_pipeline

test_prompts = [
    # normal cases
    "Build a CRM with login and contacts",
    "Create an e-commerce app with payments and admin dashboard",
    "Build a blogging platform with users and posts",

    # edge cases
    "Make something like app",
    "Build system with login but no users",
    "Create dashboard without data",
    "App with payments but no users",
]

def run_tests():
    results = []

    for prompt in test_prompts:
        print("\n========================")
        print("Prompt:", prompt)

        try:
            output = run_pipeline(prompt)
            success = bool(output["database"]["tables"])

            results.append({
                "prompt": prompt,
                "success": success
            })

        except Exception as e:
            results.append({
                "prompt": prompt,
                "success": False,
                "error": str(e)
            })

    # summary
    total = len(results)
    success_count = sum(1 for r in results if r["success"])

    print("\n===== RESULTS =====")
    print(f"Total: {total}")
    print(f"Success: {success_count}")
    print(f"Success Rate: {success_count / total * 100:.2f}%")


if __name__ == "__main__":
    run_tests()