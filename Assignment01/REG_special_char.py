import re


def run(string):

    # Make own character set and pass 
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    
    # Pass the string in search 
    # method of regex object.    
    if(regex.search(string) is None):
        print("String is accepted")
        
    else:
        print("String is not accepted.")
    

# Driver Code
if __name__ == '__main__' :
    
    # Ask the user to enter a string
    string = input("Enter a string: ")
    
    # Calling run function 
    run(string)