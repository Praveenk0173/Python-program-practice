updated palindrome program
code:
word = input("Enter a word: ")
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word
if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
program 6
code:
n = int(input("Enter how many prime numbers to print: "))
count = 0      
num = 2       
while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
program 7
code:
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)
program 8
code:
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)
program 9
code:
numbers = [2, -4, 6, 0, -3, 0]
positive = 0
negative = 0
zero = 0
i = 0
while i < len(numbers):
    num = numbers[i]
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
    i += 1
print("Positive =", positive)
print("Negative =", negative)
print("Zeros =", zero)
program 10 
code:
num = int(input("Enter a number: "))
digits = len(str(num))
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10
if sum_of_powers == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
