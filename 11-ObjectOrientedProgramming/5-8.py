'''The Contact class contains the name, email and telephone fields enabling the description of a single contact on a smartphone. 
The Contact_List class allows you to store contacts (store objects describing contacts in an array) and perform the following operations:

Add a new contact
Display the contact list
Write a program consisting of 3 files (smartphone.py, contact.py, contact_list.py).
 In the mail program (smartphone.py), create an object representing a contact list and add the following people data:

John Brown     brown@onet.pl       555234000
Anna May   	   am@o2.pl            232000199
George Small   smallg@google.pl    222999100
Paola Big      bigpaola@poczta.pl  100200300
Then, display the contact list available on the smartphone.'''

class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.contact_arr = []
    def add(self):
        self.contact_arr += self.name, self.email, self.telephone
    def display(self):
        for i in self.contact_arr:
            print(i)
        
list = Contact('Diego', 'diego@example.com', '789123456')
list.add()
list.display()



