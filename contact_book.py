import json
class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def to_dict(self):
        return {
            'Name': self.name,
            'Number': self.number,
            'Email': self.email
        }

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact.to_dict()
        print(f"{contact.name} qo'shildi.")

    
    def save_to(self):
        with open ("data.json", "w") as file:
            json.dump(self.contacts, file, indent=4)
            print(f"Data.json ga saqlandi!")

    def load_to(self):
        with open ("data.json", "r") as file:
            self.contacts = json.load(file)
            print(f"Data.jsondan yuklandi!")

    def search_data(self, name):
        for ism in self.contacts:
            if ism.lower() == name.lower():
                print(self.contacts[ism])
                return "Topildi!"
        return "Topilmadi!"
            
    
    def update_data(self, name, new_number):
        if name in self.contacts:
            self.contacts[name]['Number'] = new_number
            print(f"{name} ning raqami yangilandi!")
        else:
            print(f"{name} topilmadi!")


    
    def delete_data(self, name):
        for ism in self.contacts:
            if ism.lower() == name.lower():
                contact = self.contacts[ism]
                del self.contacts[name]
                self.save_to()
                return f"{contact['Name']} deleted!"
        return "Topilmadi!"

        















k1 = Contact("Ali", "998901234567", "ali@gmail.com")
k2 = Contact("Vali", "99890123455", "vali@gmail.com")
book = ContactBook()
book.add_contact(k1)
book.add_contact(k2)
book.save_to()
book.update_data("Ali", "998907777777")
print(book.search_data("Vali"))
book.delete_data("Vali")