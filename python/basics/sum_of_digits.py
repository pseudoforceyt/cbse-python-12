#Program to print the sum of digits of a 3 digit number
num=int(input("Enter a 3 digit number: "))

hd=num//100 #Hundreds digit
tod=num%100 #Tens and ones
td=tod//10 #Tens digit
od=tod%10 #Ones digit

snum=hd+td+od #Sum of digits
print("Sum of the digits is:",snum)
