def main() -> None:
    print("=== RepoPilot ===")

    task = input("What do you want me to do? ").strip()

    if not task:
        print("No task received.")
        return

    print(f"Task received: {task}")
