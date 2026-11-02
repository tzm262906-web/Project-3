print("أهلاً بك في نظامنا!")

user_name = input("enter your name: ")

if user_name.strip() == "":
    user_name = "Guest"
    print("no name entered. defaulting to guest.")

print(f"hello, {user_name}!")
