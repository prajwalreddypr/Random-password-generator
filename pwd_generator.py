import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""
print("Welcome to the password Generator")

noOfLetters = int(input("How many letter do you need in your pwd ?"))
noOfNumbers = int(input("How many numbers do you need in your pwd ?"))  #takes input, the no of charcaters needed for the pwd
noOfSymbols = int(input("How many symbols do you need in your pwd ?"))


for letter in range(0, noOfLetters):
    password += random.choice(letters)
    
for number in range(0, noOfNumbers):
    password += random.choice(numbers)     #uses random module to jumble the characters taken as input
    
for symbol in range(0, noOfSymbols):
    password += random.choice(symbols)
    
    
print(password)                              #prints the pwd

pwd_list = list(password)                    #converting the string to a list, bcos string cant be shuffled in python.
random.shuffle(pwd_list)            
shuffledPassword = "".join(pwd_list)         
print(shuffledPassword)                         #prints the jumbled pwd, where symbols, characters and letters are all mixed






