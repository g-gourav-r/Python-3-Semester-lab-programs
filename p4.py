#remove and reverese the string and print the characters in the even places
s=input("Enter the string : ")
rev=s[::-1]
print(rev)
s=rev.replace(" ","")
s=s[1::2]
print(s)

#Print email id's without using lists
s=input("Enter the mail id's seperated by ;")
start =0
end=s.find(";")
while end!= -1:
  print(s[start:end])
  start=end+1
  end=s.find(";",start)
print(s[start:])

# Program to find occurance of a character in a given string

occ={}
s=input("Enter the string : ")
for character in s:
  if character in occ.keys():
    occ[character]+=1
  else:
    occ[character]=1
print(occ)
  