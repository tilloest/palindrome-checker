
def is_palindrome(input_string):
    filtered_string = input_string.lower()
    filtered_string = ''.join(char for char in filtered_string if char.isalnum())
    reversed_string = filtered_string[::-1]
    if filtered_string == reversed_string:
        return True
    else:
        return False
    
input_string = input("Enter a string: ")
print(is_palindrome(input_string))
