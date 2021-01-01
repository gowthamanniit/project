def booksearch():
    f=open("database.txt")

    book=[]
    for line in f:    
        k=line
        book.append(k.split(":"))


    sb=input("enter book title to be searched:")
    sb=sb.upper()
    test=False
    for s in book:
        if s[2].upper()==sb:        
            print("\nID: ",s[0],"\nISBN: ",s[1],"\nTITLE: ",s[2],"\nAUTHOR: ",s[3],"\nPURCHASE DATE: ",s[4],"\nMEMBER ID: ",s[5])
            test=True
    if test==False:
        print(" book is not available")
