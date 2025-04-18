import random 
alpha= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_chara= ["!","@","#","$","%","^","&","*","(",")",'+','-','/','']
numbers= ['1','2','3','4''5','6','7','8','9','0']
n_alpha= int(input("how many letters you would like in your password.. "))
n_special= int(input("how many special characters you would like in your password.. "))
n_num= int(input("how many number you want in your special characters.. "))

password= ""
for i in range(n_alpha):
    password+=random.choice(alpha)
for i in range(n_special):
    password+=random.choice(special_chara)
for i in range(n_num):
    password+= random.choice(numbers)

print(f" your password: '{password}'")