#SI and CI

p = int(input("Enter principal amount: "))
r = float(input("Enter rate of interest per annum (exclude % symbol): "))
t = float(input("Enter time period in years: "))

SI = int(p*t*r/100)
CI = int(p*(1+(r/100))**t)

print("Simple Interest for given data = ",SI,"\nCompound Interest for given data = ",CI)
