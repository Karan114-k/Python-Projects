import random
import string
import secrets
import time
#OTP Generator
n=int(input("Enter Password Length = "))
otp=""
for _ in range(n):
    otp+= str(random.randint(0,9))
print(otp)
#Another method 
otp = random.randint(1000,9999)
print(otp)

#Password Generator
n=int(input("Enter password length = "))
digits = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
password = "".join(secrets.choice(digits) for _ in range(n))
print(password) 
