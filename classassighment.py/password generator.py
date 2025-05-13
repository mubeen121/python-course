import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number= "0123456789"
Symbols="!@#$%^&*()_-+=?><{}[]"
all_chars=lower +upper +number+Symbols
length=int(input("Enter a Length:"))
password = ''.join(random.sample(all_chars,length))
print("Generatedd Password : ",password)

