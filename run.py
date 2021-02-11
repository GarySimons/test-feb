# this function runs for the name and age function calls
def get_user_input(prompt):
    return input(prompt)


# this function runs twice
def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)


# name and age are the first two function calls to run sequentially
name = get_user_input("Input your name: ")
age = get_user_input("Input your age: ")


# Then function calls run sequentoally
print_out_to_console(f"Your name is {name}")
print_out_to_console(f"You are {age} years old")
