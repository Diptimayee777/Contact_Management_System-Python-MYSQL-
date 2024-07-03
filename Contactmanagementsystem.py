import mysql.connector as a
con= a.connect(host="localhost",user="root",password='Diptimayeesql77',database="contact_management")

def addcontact():
    cn=input("Enter the name of the contact")
    pn=input("Enter the phone number")
    ei=input("Enter the E-Mail Id")
    data=(cn,pn,ei)
    sql='insert into contacts values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit
    print(">...........................<")
    print("Contact added Successfully")
    main()
def editcontact():
    cn=input("Enter the contact name you want to edit: ")
    r=input("Enter new contact name: ")
    p=input("Enter new phone number: ")
    s=input("Enter new email id: ")
    a='update contacts set Name=%s, Phone_number=%s, EmailId=%s where Name=%s'
    c=con.cursor()
    c.execute(a, (r, p, s, cn))
    con.commit()
    print(">...........................<")
    print("Contact successfully edited")
    
def deletecontact():
    ac=input("Enter contact name you want to delete")
    a="delete from contacts where Name=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(" Contact Successfully Deleted")
    main()
    
def displaycontact():
    a="select * from contacts"
    try:
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        if myresult:
            print("Contact List:")
            print("----------------")
            for i in myresult:
                print("Name: ", i[0])
                print("Number: ", i[1])
                print("Email: ", i[2])  # Assuming email is the 3rd column
                print(">.....................<")
        else:
            print("No contacts found.")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        main()
def main():
    print("Contact Manager, 1 for Add Contact,2 for Edit Contact, 3 for delete contact and 4 for display contact")
    ch=int(input("Enter your choice"))
    if(ch==1):
        addcontact()
    elif(ch==2):
        editcontact()
    elif(ch==3):
        deletecontact()
    elif(ch==4):
        displaycontact()
    else:
        print("wrong choice")
pw=input("enterpassword")
if pw=='Diptimayeesql77':
    main()
else:
    print("wrong password")
