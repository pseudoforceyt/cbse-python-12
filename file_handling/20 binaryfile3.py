import pickle
f = open('Telephone.DAT','wb+')
# 1:
flag, c = 'y', 0
print("Enter directory details")
while flag.lower() == 'y':
    c += 1
    print(f"Record {c}")
    name = input("Name: ")
    address = input("Address: ")
    areacode = input("Area code: ")
    phone_number = input("Phone number: ")
    pickle.dump([name, address, areacode, phone_number], f)
    flag = input("Continue? (y/N) ")

# 2:
f.seek(0)
records = list()
while True:
    try:
        cur = f.tell()
        rec = pickle.load(f)
        if rec[2] != "TP101":
            records.append(rec)
    except EOFError:
        f.close()
        break

f = open('Telephone.DAT','wb+')
f.seek(0)
for i in records:
    pickle.dump(i, f)

# 3:
count = 0
f.seek(0)
print("Directory listing:\n")
print("Name, Address, Area code, Phone number")
while True:
    try:
        rec = pickle.load(f)
        print(rec[0], rec[1], rec[2], rec[3], sep=", ")
        count += 1
    except EOFError:
        f.close()
        print(f"\nTotal {count} record(s).")
        break