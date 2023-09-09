#Program to check whether the number is armstrong number or not
num=int(input("Enter a 3 digit number: "))

hd=num//100 #Hundreds digit
tod=num%100 #Tens and ones
td=tod//10 #Tens digit
od=tod%10 #Ones digit

angnum=hd**3 + td**3 + od**3
if angnum == num :
    print("The number is an armstrong number")
else :
    print("The number is not an armstrong number")
