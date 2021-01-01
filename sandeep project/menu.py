import book_search
import book_checkout
import book_return
import report_database
import report_logfile
import sys
while True:
    print("Library Management System")
    print(" 1. book search ")
    print(" 2. book checkout ")
    print(" 3. book return ")
    print(" 4. report - view all books ")
    print(" 5. report - view checkout books")
    print(" 6. exit ")    
    ch=input("Enter Your Choice:")
    if ch=='1':
        book_search.booksearch()
    elif ch=='2':
        book_checkout.bookcheckout()
    elif ch=='3':
        book_return.bookreturn()
    elif ch=='4':
        report_database.reportdatabase()
    elif ch=='5':
        report_logfile.reportlogfile()
    elif ch=='6':
        sys.exit('')
    else:
        print("Please enter correct choice:")
