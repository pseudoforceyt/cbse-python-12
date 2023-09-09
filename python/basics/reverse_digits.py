# Program to reverse the digits of a 3 digit number

num=int(input("Enter a 3 digit number: "))

hd=num//100 #Hundreds digit
tod=num%100 #Tens and ones
td=tod//10 #Tens digit
od=tod%10 #Ones digit

rnum=od*100 + td*10 + hd #Reversed Number
print("Number with reversed digits:",rnum)
