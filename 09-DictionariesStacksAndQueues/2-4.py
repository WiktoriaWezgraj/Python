'''The program below finds spam in received emails. 
Complete the program that displays those received email addresses that are on the spam list.'''

emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = emails_received & spam_list  # Intersection
print("Spam emails:", spam_emails)