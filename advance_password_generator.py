import random 

latters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symboles = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_latters = int(input("how many latters are you used in password : "))
n_number = int(input("how many numbers are you used in password : "))

n_symboles = int(input("how many symboles are you used in password : "))

password_list = []

for i in range(1,n_latters+1):
    password_list += random.choice(latters)
for i in range(1,n_number+1):
    password_list += random.choice(numbers)
for i in range(1,n_symboles+1):
    password_list += random.choice(symboles)


random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)