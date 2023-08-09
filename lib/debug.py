def print_separator():
    print("-" * 40)

def debug_print(message):
    print_separator()
    print("DEBUG:", message)
    print_separator()

def print_variable(variable_name, value):
    print_separator()
    print(f"{variable_name}:", value)
    print_separator()

def print_dict(dictionary):
    print_separator()
    for key, value in dictionary.items():
        print(f"{key}: {value}")
    print_separator()
