print("مرحباً بك في نظامنا!")


name_input = input("Please enter your name: ").strip()


if not name_input:
    name_input = "Anonymous"
    print("Warning: No name provided. Setting default to Anonymous.")


print(f"Welcome aboard, {name_input}!")
