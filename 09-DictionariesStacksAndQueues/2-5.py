'''Two contact lists retrieved from a database contain email addresses. Write a program that combines these lists and simultaneously removes duplicates.'''

contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = contacts_A | contacts_B  # Union
print("Merged contacts:", merged_contacts)