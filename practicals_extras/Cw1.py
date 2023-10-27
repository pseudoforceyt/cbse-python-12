import pickle
f = open("Product.dat", "wb")
flag,c = 'y',0
while flag.lower() == 'y':
  c += 1
  print("Product", c)
  pno = int(input("Product no. "))
  pname = input("Product name: ")
  price = float(input("Price: "))
  pickle.dump([pno, pname, price], f)
  flag = input("Continue? (y/N) ")
f.close()

records, found = list(), 0
search = int(input("Product to modify: "))
f = open("Product.dat", "rb")
while True:
  try:
    rec = pickle.load(f)
    if rec[0] == search:
      rec[2] = float(input("New price: "))
      found = 1
    records.append(rec)
  except EOFError:
    if found == 0:
      print("Record not found")
    f.close()
    break

f = open("Product.dat", "wb")
for i in records:
  pickle.dump(i, f)

  
    
