import pickle

f = open("Mobile.DAT", "wb+")
print("Enter data about mobiles")
flag,c = 'y',0
while flag.lower() == 'y':
    c += 1
    print(f"Mobile {c}")
    ModelNo = input("Model no.: ")
    memorycard = input("Memory card support (Y/N): ").upper()
    Modelname = input("Model name: ")
    megapixel = int(input("Camera Megapixels: "))
    pickle.dump([ModelNo, memorycard, Modelname, megapixel], f)
else:
    f.close()

f = open("Mobile.DAT", "rb")
search = input("Enter model no. of mobile whose megapixel to be updated: ")

records = list()
while True:
    try:
        cur = f.tell()
        rec = pickle.load(f)
        if rec[0] == search:
            rec[3] = int(input("New Camera Megapixels: "))
            records.append(rec)
        else:
            records.append(rec)
    except EOFError:
        f.close()
        break

f = open("Mobile.DAT", "wb+")
f.seek(0)
for i in records:
    pickle.dump(i, f)