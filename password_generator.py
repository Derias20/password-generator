#Created by Derias -> https://github.com/Derias20
import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters= "@#$%&*/\?"
a = lower_case + upper_case + numbers + special_characters
length= int(input("How long should the password be?"))
password = "".join(random.sample(a,length))
print("Password:"+ password)