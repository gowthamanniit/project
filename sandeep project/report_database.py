def reportdatabase():
    file=open("database.txt")
    book=[]
    for line in file:
        print(line)
    file.close()

