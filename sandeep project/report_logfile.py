def reportlogfile():
    file=open("logfile.txt")
    book=[]
    for line in file:
        print(line)
    file.close()

