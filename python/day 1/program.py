problem 1
code:
num=int(input("enter the number:"))
for i in range(1,11):
    result=num*i
    print(num,"X",i,"=",result)
problem 2
code:
num = int(input("Enter an integer: "))
sum_digits = 0
n = abs(num)
while n > 0:
  sum_digits += n % 10
  n //= 10
  print("Sum of digits:", sum_digits)
problem 3
code:
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in string:
  if ch in vowels:
    count += 1
print("Number of vowels:", count)
problem 4
code:
string = input("Enter a string: ")
if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
problem 5
code:
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
