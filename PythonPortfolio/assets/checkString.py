#Made by Alyssa Bishop
#Date: March 15 2025
def check_string(str1, str2):
    if str1 == str2:
        return "strings are equal"
    elif str1 != str2:
        return "strings not equal"
#user input 2 strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
#results
answer = check_string(str1, str2)
print(answer)