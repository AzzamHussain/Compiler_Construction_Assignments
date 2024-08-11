import re

def data_type_finder(user_input):
    # Define regex patterns for data types
    integer_pattern = r"\d+"
    float_pattern = r"\d+\.\d+"
    string_pattern = r"[a-zA-Z]+"
    double_pattern = r"^\d*\.\d+$"
    char_pattern = r"^.$"

    # Check for matches
    if re.fullmatch(integer_pattern, user_input):
        print("Input is an integer.")
    elif re.fullmatch(float_pattern, user_input):
        print("Input is a float.")
    elif re.fullmatch(string_pattern, user_input):
        print("Input is a string.")
    elif re.fullmatch(double_pattern, user_input):
        print("Input is a double.")
    elif re.fullmatch(char_pattern, user_input):
        print("Input is a char.")
    else:
        print("Unable to determine the data type.")
while True:
    # Example user input
    user_input = input("Enter a value:")
    data_type_finder(user_input)
    should_continue=input("Do you want to check other Data Types (yes/no)?").lower()
    if(should_continue!="yes"):
        print("existing program")
        break
