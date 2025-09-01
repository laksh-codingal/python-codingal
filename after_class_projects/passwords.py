
import random
import string

num = int(input("Enter the size of the password: "))
pwdList = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(pwdList) for _ in range(num))
print("The generated password is ", password)
