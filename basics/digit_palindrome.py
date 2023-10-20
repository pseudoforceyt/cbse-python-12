# Program to check whether the number is digit palindrome
num = int(input("Enter a 3 digit number: "))

hd = num//100
tod = num%100
td = tod//10
od = tod%10

if od*100+td*10+hd == num :
    print("The number is a digit palindrome")
else :
    print("The number is NOT a digit palindrome")
