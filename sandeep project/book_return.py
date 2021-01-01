def bookreturn():
    bid=input("Enter book id:")

    file=open("database.txt")

    book=[]
    for line in file:    
        k=line
        book.append(k.split(":"))
    file.close()

    fw=open("database.txt","w")

    test=False
    for r in book:
        if r[1]==bid:
            print(" book returned success!!")
            print(" Thank You!!")
            r[5]='0'
            test=True
            for w in book:
                cs=":".join(w)
                fw.write(cs)
            fw.close()
            break
    if test==False:
        print(" please enter valid book id:")
        
        

