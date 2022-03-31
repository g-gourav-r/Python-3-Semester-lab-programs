# Extract substring between @ and #
s=input("Enter the string : ")
indexofat=s.find("@")
indexofhash=s.find("#")
print(s[indexofat+1:indexofhash])

#Count the occurance of e in the string

string=input("Enter the string : ")
count=0
for character in string:
  if(character=="e"):
    count+=1
print("The occurance of e in the string is ",count)

#Remove the woth "the" from the given string
s=input("Enter the string : ")
words=s.split()
result=" "
for word in words:
  if word.lower()!="the":
   result+=word
    result+=" "
print(result)

#Count the number of apples bought by the guest
Allguests = {'Sam':{'apple':3,'mango':5},'Ram':{'apple':10,'orange':6},'Bam':{'bannana':1,'apple':5}}
count = 0
for fruits in Allguests.values():
    count +=fruits.get('apple')

print("The number of apples is", count)