'''In Python, the sorted() function is used to return a new sorted list from the elements of any iterable, such as a list, tuple, or dictionary. 
It doesn’t modify the original iterable but instead returns a new sorted list.

One of the sorted() function optional argument can be a function that serves as a key for the sort comparison. 
For example, you can pass a function that extracts a specific field from the items.

Find a syntax for the sorted() function online. Then use the function to sort a list of names by their length (number of letters). 
Define an anonymous function, which you use as an argument to the sorted() function. Sample result:

Unsorted list:
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
Sorted list:
James
Emily
Henry
Olivia
Sophia
William
Benjamin'''

names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sorted_names = sorted(names, key=len)
print(sorted_names)