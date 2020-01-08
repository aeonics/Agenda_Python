import csv

class Contact:
    
    def __init__(self, name, phone, email):
        self.name =  name
        self.phone = phone
        self.email = email


class ContactBook:
    
    def __init__(self):
        self._contacts = []
        
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
        
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
            
    def delete (self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
            
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
            
    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                contact.name = str(input('Cual es el nuevo nombre: '))
                contact.phone = str(input('Cual es el nuevo telefono: '))
                contact.email = str(input('Cual es el nuevo email: '))
                self._save()
                
                break
        else:
            self._not_found()
        
            
    def _not_found(self):
        print('*'* 20)
        print(' NO ENCONTRADO')
        print('*'* 20)
            
    def _print_contact(self, contact):
        print('-*- ' * 18)
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('-*- ' * 18)
        
    def _save(self):
        with open('contacts.csv','w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))
        
def run():
        
    contact_book = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
        
        contact_book.add(row[0], row[1], row[2])
           
   
            
    print('*'* 33)
    print(' A G E N D A  T E L E F O N I C A')
    print('*'* 33)
    while True:
        
        option = str(input(''' ¿Que opcion deseas hacer? 
                           [a]ñadir Contacto
                           [u]Actualizar Contacto
                           [b]uscar Contacto
                           [d]Borrar Contacto
                           [l]istar Contactos
                           [s]alir
                           =====> '''))
        if option == 'a':
            name = str(input('Escribe el nombre del contacto:'))
            phone = str(input('Cual es el telefono: '))
            email = str(input('Cual es el email: '))
            
            contact_book.add(name,phone,email)
        elif option == 'u':
            print('ACTUALIZAR CONTACTO')
            name = str(input('Escribe el nombre del contacto: '))
            
            contact_book.update(name)
        elif option == 'b':
            print('BUSCAR CONTACTO')
            name = str(input('Escribe el nombre del contacto: '))
            
            contact_book.search(name)
        elif option == 'd':
            print('ELIMINAR CONTACTO')
            name = str(input('Escribe el nombre del contacto: '))
            
            contact_book.delete(name)
        elif option == 'l':
            contact_book.show_all()
        elif option == 's':
            print('Gracias por usar esta Agenda')
            print('')
            break
        else:
            print('='* 55)
            print('Esa opcion no la encontre usa la letra que esta entre []')
            print('='* 55)

if __name__ == "__main__":
    run()