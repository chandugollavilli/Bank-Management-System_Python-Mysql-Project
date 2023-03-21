import mysql.connector
bank_project = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "Chandu@123",
    database = "bank_project"
)

# print(bank_project)
bank_data = bank_project.cursor()

# bank_data.execute("CREATE DATABASE bank_project")

# bank_data.execute("CREATE TABLE ACCOUNT (NAME VARCHAR(100), ACCOUNTNO VARCHAR(100), DATEOFBIRTH VARCHAR(100), ADDRESS VARCHAR(100), PHONENO VARCHAR(100), OPENINGBALANCE INT )")

# bank_data.execute("CREATE TABLE AMOUNT (NAME VARCHAR(100), ACCOUNTNO VARCHAR(100), BALANCE INT)")



########################################Programming####################################

def openAccount():
    n = input("Enter Name: ")
    ac = input("Enter Account No: ")
    db = input("Enter D.O.B: ")
    p = input("Enter Phone: ")
    ad = input("Enter Address: ")
    ob = int(input("Enter Opening Balance: "))
    data1 = (n,ac,db,p,ad,ob)
    data2 = (n,ac,ob)
    sql1 = "INSERT INTO ACCOUNT values(%s,%s,%s,%s,%s,%s)"
    sql2 = "INSERT INTO AMOUNT values(%s,%s,%s)"
    bank_data= bank_project.cursor()
    bank_data.execute(sql1,data1)
    bank_data.execute(sql2,data2)
    bank_project.commit()
    print("\nAccount Created Sucessfully")
    main()

def depositAmount():
    am = int(input("Enter Amount: "))
    ac = input("Enter Account No: ")
    a = "SELECT BALANCE FROM AMOUNT WHERE ACCOUNTNO = %s"
    data = (ac,)
    bank_data = bank_project.cursor()
    bank_data.execute(a,data)
    myresult = bank_data.fetchone()
    tam = myresult[0] + am
    sql = "UPDATE AMOUNT SET BALANCE = %s WHERE ACCOUNTNO = %s"
    d = (tam,ac)
    bank_data.execute(sql,d)
    bank_project.commit()
    print("\n Amount Deposited Sucessfully")
    main()

def withdrawAmount():
    am = int(input("Enter Amount: "))
    ac = input("Enter Account No: ")
    a = "SELECT BALANCE FROM AMOUNT WHERE ACCOUNTNO = %s"
    data = (ac,)
    bank_data = bank_project.cursor()
    bank_data.execute(a,data)
    myresult = bank_data.fetchone()
    tam = myresult[0] - am
    sql = "UPDATE AMOUNT SET BALANCE = %s WHERE ACCOUNTNO = %s"
    d = (tam,ac)
    bank_data.execute(sql,d)
    bank_project.commit()
    print("\nAmount Withdraw Sucessfully")
    main()

def balance():
    ac = input("Enter Account No: ")
    a = "SELECT BALANCE FROM AMOUNT WHERE ACCOUNTNO = %s"
    data = (ac,)
    bank_data = bank_project.cursor()
    bank_data.execute(a,data)
    myresult = bank_data.fetchone()
    print("Balance for Account: ",ac,"is",myresult[0])
    main()

def dispacc():
    ac = input("Enter Account No: ")
    a = "SELECT * FROM ACCOUNT WHERE ACCOUNTNO = %s"
    data = (ac,)
    bank_data = bank_project.cursor()
    bank_data.execute(a,data)
    myresult = bank_data.fetchone()
    for i in myresult:
        print(i, end =" , ")
    main()


def closeaccount():
    ac = input("Enter Account No: ")
    sql1 = "DELETE FROM ACCOUNT WHERE ACCOUNTNO = %s"
    sql2 = "DELETE FROM AMOUNT WHERE ACCOUNTNO = %s"
    data = (ac,)
    bank_data = bank_project.cursor()
    bank_data.execute(sql1,data)
    bank_data.execute(sql2,data)
    bank_project.commit()
    print("\n Account Closed Sucessfully")
    main()


def main():
    print("""

    1.OPEN NEW ACCOUNT
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSE AN ACCOUNT

    """)
    choice = input("Enter Task No: ")
    if(choice == '1'):
        openAccount()
    elif(choice == '2'):
        depositAmount()
    elif(choice == '3'):
        withdrawAmount()
    elif(choice == '4'):
        balance()
    elif(choice == '5'):
        dispacc()
    elif(choice == '6'):
        closeaccount()
    else:
        print("Wrong choice..........")
        main()
main()