# Program to print all the words present in the string and print their length
s=input('Enter the string ')
words=s.split()
for word in words:
  print(word , ":" ,len(word))
print("Total words = ",len(words)

#FIbonacci series in reverse order
l=[]
n=int(input("Enter the number "))
if n==1:
  l.append(0)
else:
  l.append(0)
  l.append(1)
for i in range(2,n):
  l.append(l[i-1]+l[i-2])
l.reverse()
print(l)