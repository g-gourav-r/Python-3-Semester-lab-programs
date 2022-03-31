# Extract mail Id from the given string
import re
s=input('Enter the string : ')
words=s.split()
for word in words:
  obj=re.match("^[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-zA-Z]*",word)
  
  if obj:
    print(word)

# Validate a password
import re
password =input("Enter the password : ")
obj=re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_@#$])[0-9A-Za-z_@#$]{6,16}$",password)

if obj:
  print("Valid password")
else:
  print("Invalid password")
