import random  
num = random.randint(1, 6)
print("dice roll:", num)
import string
password = (string.ascii_letters + string.digits)
password1 = ''.join(random.choice(password) for i in range(6))
print("Your password is:", password1)
import random
mylist =[1,34,567,90,6.9]
random.shuffle(mylist)
print("Shuffled list:", mylist)