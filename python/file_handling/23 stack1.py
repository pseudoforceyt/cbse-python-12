def DoPush(Customer):
    flag,c = 'y',0
    while flag.lower() == 'y':
        c += 1
        print("Customer", c)
        cid = input("ID: ")
        name = input("Name: ")
        phoneno = input("Phone no.: ")
        Customer.append([cid, name, phoneno])
        flag = input("Continue pushing? (y/N) ")

def DoPop(Customer):
    if len(Customer) > 0:
        print("Pop:", Customer.pop())
    else:
        print("Stack empty.")

def DoShow(Customer):
    print("\n\n[Customer ID, Name, Phone No.]\n")
    for i in Customer[::-1]:
        print(i)

Customer = list()
while True:
    print("What would you like to do?")
    print("1. Push to customer stack")
    print("2. Pop from customer stack")
    print("3. Show customer stack")
    print("4. Exit")

    ch = int(input("> "))
    if ch == 1:
        DoPush(Customer)
    elif ch == 2:
        DoPop(Customer)
    elif ch == 3:
        DoShow(Customer)
    elif ch == 4:
        print("Goodbye!")
        break
    else:
        print("Enter a valid choice!\n\n")