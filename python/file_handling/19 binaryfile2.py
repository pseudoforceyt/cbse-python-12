import pickle

f = open("Mobile.DAT", "rb+")
search = input("Enter model no. of mobile to be updated: ")
while True:
    try:
        rec = pickle.load(f)
        if rec[0] == search:
            rec[3] = int(input("Enter megapixel: "))
            f.seek(0)
            pickle.dump(rec, f)
    except EOFError:
        f.close()
