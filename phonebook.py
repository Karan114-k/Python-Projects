phonebook={
    "john":"23485"
}
def add_contact(phonebook):
    name = input("Enter your name")
    number = input ("Enter your number")
    phonebook[name]= number
    print("Contact added")
def search_contact(phonebook):
    name = input ("Enter your name")
    if name in phonebook:
        print(f"{name} number is {phonebook[name]}")
    else:
        print("Contact not found")
def delete_contact(phonebook):
    name = input("Enter your name")
    if name in phonebook:

        del phonebook[name]
        print("Contact deleted")
    else:
        print("Contact not found")
def show_contact(phonebook):
    for name,number in phonebook.items():
        print(f"{name}: {number}")
while True:
    print("1. Add Contact")
    print("2. Search contact")
    print("3. Delete Contact")
    print("4. Dilplay Contact")
    print("5. Exit")
    choice = input("Enter your choice 1/2/3/4/5")
    if choice=="1":
        add_contact(phonebook)
    elif choice=="2":
        search_contact(phonebook)
    elif choice=='3':
        delete_contact(phonebook)
    elif choice=='4':
        show_contact(phonebook)
    elif choice=='5':
        print("Goodbye !")
        break
    else:
        print("Invalid option")
