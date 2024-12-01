'''Write a program to translate words from English to Polish. The user enters a word in English from the keyboard. 
The program displays the translation of the word or information that the translation is unavailable.'''

translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

eng_word = input('Enter English Word: ')

if eng_word in translations:
    print(translations[eng_word])
else:
    print('There is no available translation.')