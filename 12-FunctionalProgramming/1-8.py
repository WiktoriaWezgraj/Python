'''Define an anonymous function initials(name,surname) that returns the first letters of the name and surname.'''

initials = lambda name, surname: name[0]+surname[0]

name = 'Elf' 
surname = 'Arthur'
print(initials(name, surname))