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

def print_sqlalchemy_exception(exception):
    print_separator()
    print("SQLAlchemy Exception:")
    print(exception)
    print_separator()

def print_query(query):
    print_separator()
    print("SQL Query:")
    print(query)
    print_separator()

def print_query_result(result):
    print_separator()
    print("Query Result:")
    for row in result:
        print(row)
    print_separator()
