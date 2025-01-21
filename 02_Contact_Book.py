contacts = {}
while True:
    print("\nPrint Contact Information")
    print("1.create Contact")
    print("2.view Contact")
    print("3.update Contact")
    print("4.delete Contact")
    print("5.search Contact")
    print("6.count Contact")
    print("7.Exit")

    choice = input("Enter your choice =")

    if choice == '1':
        name=input("Enter your name=")
        if name in contacts:
            print(f'Contact name {name} already exists')
        else:
            age = input("Enter your age=")
            mobile = input("Enter you mobile number= ")
            contacts[name]={'age':int(age),'mobile':mobile}
            print("Contact Create Successfully!")

    elif choice == '2':
        name = input("Enter the name of view contact=")
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name},Age:{age},Mobile Number:{mobile}')

    elif choice == '3':
        name = input("Enter the name of update contact=")
        if name in contacts:
            name = input("Enter the name=")
            age = input("Enter the age=")
            mobile = input("Enter mobile")
            contacts[name]={'name':name,'age':int(age),'mobile':mobile}
            print(f"Contact name {name} updated successfully!")
        else:
            print("Name Not Found")

    elif choice == '4':
        name = input("Enter the name to delete Contact:")
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print("Contact Not Found")

    elif choice == '5':
        search_name = input(f'Enter the name to be search=')
        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found-Name{name},Age{age},Mobile Number{mobile}')
                found=True
        if not found:
            print("No contact Found with that name")

    elif choice == '6':
        print("Total contact in your books:",len(contacts))

    elif choice == '7':
        print("Good bye....closing the program")
        break

    else:
        print("Invalid Input")



