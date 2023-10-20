i=1
print("\n>>>>>>>>>>>>>>>>",i,"<<<<<<<<<<<<<<<<<",end='\n')
i=10
while i<=99:
    td=i//10
    od=i-td*10
    print(td,od,end="||")
    if i == td**3+od**3:
        print("\n>>>>>>>>>>>>>>>>",i,"<<<<<<<<<<<<<<<<<",end='\n')
    else:
        pass
    i+=1
while i<=999:
    hd=i//100
    td=(i-hd*100)//10
    od=i-(hd*100)-(td*10)
    print(hd,td,od,end="||")
    if i == hd**3+td**3+od**3:
        print("\n>>>>>>>>>>>>>>>>",i,"<<<<<<<<<<<<<<<<<",end='\n')
    else:
        pass
    i+=1
while i<=9999:
    thd=i//1000
    hd=(i-thd*1000)//100
    td=(i-thd*1000-hd*100)//10
    od=i-thd*1000-hd*100-td*10
    print(thd,hd,td,od,end="||")
    if i == thd**3+hd**3+td**3+od**3:
        print("\n>>>>>>>>>>>>>>>>",i,"<<<<<<<<<<<<<<<<<",end='\n')
    else:
        pass
    i+=1
while i<=99999:
    tthd=i//10000
    thd=(i-tthd*10000)//1000
    hd=(i-tthd*10000-thd*1000)//100
    td=(i-tthd*10000-thd*1000-hd*100)//10
    od=i-tthd*10000-thd*1000-hd*100-td*10
    print(tthd,thd,hd,td,od,end="||")
    if i == tthd**3+thd**3+hd**3+td**3+od**3:
        print("\n>>>>>>>>>>>>>>>>",i,"<<<<<<<<<<<<<<<<<",end='\n')
    else:
        pass
    i+=1
