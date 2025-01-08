import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','+','*']
c_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L','M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
print("WELCOME TO PASSWORD GENERATOR!")
nr_letter = int(input("How many numbers would you like in your password?: \n"))

nr_symbols = int(input("How many symbols would you like?:\n "))

nr_numbers= int(input("How many numbers would you like?:\n"))
nr_c_letters = int(input("How many c_numbers would you like?:\n"))
password = [ ]
for char in range(1, nr_letter +1):
    password += random.choice(letter)

for char in range(1, nr_symbols +1):
    password += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password += random.choice(numbers)

for char in range(1, nr_c_letters +1):
    password += random.choice(c_letters)


random.shuffle(password)


password_a = ""
for char in password:
    password_a += char

print(f"Your password is :{password_a}")