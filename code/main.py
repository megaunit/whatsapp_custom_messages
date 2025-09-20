# from contacts import contacts_interface
# from sender import whatsapp_connect, send_message, #send_interface # TODO: do send message functino in sender.py
# from interface import make_window, update_connection_status
import tkinter as tk
import json

"/Users/mega/Desktop/Code/Whatsapp Messages/code/contacts.json"

class Contacts:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        with open(self.json_file_path, "r") as file:
            self.contacts = json.load(file)

    def add_contacts(self):
        while True:
            phone = input("Enter contact phone number to add, or press enter: ")
            if phone == "":
                break
            phone = phone.replace(" ", "").replace("+", "")
            if len(phone) != 12 or not phone.isdigit():
                print("Phone number should be: 966xxxxxxxxx")
                continue
            if phone in self.contacts.keys():
                print(f"This phone number is available in list ({self.contacts[phone]})")
                continue
            name = input("Enter contant name: ")
            self.contacts[phone] = name
            with open(self.json_file_path, "w") as file:
                json.dump(self.contacts, file)
            print(f"{phone} is added to list as {name}")

    def see_contacts(self):
        for phone, name in self.contacts.items():
            print(f"- Phone number {phone}, name {name}")
        input("Press enter to continue")

    def edit_contact(self):
        while True:
            phone = input("Enter contact's phone number to edit, or press enter: ") # Phone number is saved as a string
            if phone == "":
                break
            if phone not in self.contacts.keys():
                print("This phone number is not in list")
                continue
            new_name = input("Enter new name: ")
            self.contacts[phone] = new_name
            with open(self.json_file_path, "w") as file:
                json.dump(self.contacts, file)
            print(f"{phone} name is changed to {new_name}")

    def remove_contact(self):
        while True:
            phone = input("Enter contact's phone number to remove, or press enter: ") # Phone number is saved as a string
            if phone == "":
                break
            if phone not in self.contacts.keys():
                print("This phone number is not in list")
                continue
            name = self.contacts.pop(phone)
            with open(self.json_file_path, "w") as file:
                json.dump(self.contacts, file)
            print(f"{phone} ({name}) is removed from list")




class Interface:
    def __init__(self):
        pass


class SenderApp:
    def __init__(self):
        self.interface = Interface()


    
# def main():

#     make_window()

# def connect():
#     whatsapp_connect()

# # def main():
# #     # with open("contacts.json", "r") as file:
# #     #     contacts = json.load(file)
# #     print("\n" * 100)
# #     while True:
# #         choice = input("1. Manage contacts\n2. Send a message\n3. Exit\n")
# #         if choice not in ["1","2","3","١","٢","٣"]:
# #             print("\n" * 100)
# #             print("Choose only 1, 2, or 3")
# #         elif choice in ["1","١"]:
# #             contacts_interface()
# #             print("\n" * 100)
# #         elif choice in ["2","٢"]:
# #             send_interface()
# #             print("\n" * 100)
# #         elif choice in ["3","٣"]:
# #             quit()
# #         else:
# #             print("\n" * 100)
# #             print("Error")

# if __name__ == "__main__":
#     main()