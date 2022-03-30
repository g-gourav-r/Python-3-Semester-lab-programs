## Add all the digits in a number until we end up with a single digit. If the number is 1, Then it is a magic number

numbers=input("Enter the number : ")
while len(numbers)>1:
  sum=0
  for number in numbers:
    sum+=int(number)
    numbers=str(sum)
  print("The sum of numbers is ", numbers)
if(numbers=="1"):
  print("Magic number")

## Print all the prime numbers within a range
n=int(input("Enter the number : "))
for i in range(2,n+1):
  prime=True
  for j in range(2,i):
    if i%j == 0:
      prime=False
  if(prime==True):
    print(i)