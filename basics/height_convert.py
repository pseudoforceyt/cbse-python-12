print("^^ Convert your Height ^^")

cm=int(input("Enter your height in centimeters: "))
inch=cm*0.3937
ft=inch/12

ftint=int(ft)
reminch=int(inch-ftint*12)

print("Your height in\nInches:",inch,"in\nFeet:",ft,"ft OR",ftint,"\'",reminch,"\"")
