def bookcheckout():
    file=open("database.txt")
    cout=open("logfile.txt","a")

    book=[]
    for line in file:    
        k=line
        book.append(k.split(":"))

    file.close()

    fw=open("database.txt","w")
    test=False

    while True:
        mid=input("Enter 4-digit member id:")
        if not len(mid)==4:
            print("Enter valid 4 digit member id: ")
        else:        
            print("Enter book id to checkout:")
            bid=input("enter book id:")
            for r in book:
                if r[1]==bid and r[5]=='0':                
                    print("book checkout success!")                
                    r[5]=mid
                    cout.write(r[0]+":"+r[1]+":"+r[2]+":"+r[3]+":"+r[4]+":"+r[5]+":.\n")
                    cout.close()
                    test=True
                    break
            for w in book:
                cs=":".join(w)
                fw.write(cs)
                    
            if test==False:
                print("book not available!!:")            
            break

    fw.close()

