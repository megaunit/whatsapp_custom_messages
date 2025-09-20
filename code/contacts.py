import json

def contacts_interface():

    

    print("\n" * 100)
    while True:
        choice = input("1. See contacts\n2. Add contacts\n3. Edit contacts\n4. Remove contacts\n5. Main Menu\n")
        if choice not in ["1","2","3","4","5","١","٢","٣","٤","٥"]:
            print("\n" * 100)
            print("Choose only 1, 2, 3, 4, or 5")
        elif choice in ["1","١"]:
            print("\n" * 100)
            see_contacts(contacts)
            print("\n" * 100)
        elif choice in ["2","٢"]:
            print("\n" * 100)
            add_contacts(contacts)
            print("\n" * 100)
        elif choice in ["3","٣"]:
            print("\n" * 100)
            edit_contact(contacts)
            print("\n" * 100)
        elif choice in ["4","٤"]:
            print("\n" * 100)
            remove_contact(contacts)
            print("\n" * 100)
        elif choice in ["5","٥"]:
            break
        else:
            print("\n" * 100)
            print("Error")


