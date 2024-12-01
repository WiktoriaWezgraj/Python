'''12. Programming languages ​​often provide built-in functions for sorting collections of data. 
Data can be sorted in ascending or descending order. Look at the list of built-in functions below and find the one that allows you to sort collections of data.

   <https://docs.python.org/3/library/functions.html>

   Then write a program that uses the built-in function to sort the data below:'''

   # Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
print(sorted(distances_traveled))
   # Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
daily_temperatures.sort(reverse=True)
print(daily_temperatures)
   # Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
      "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
file_names.sort()
print(file_names)
# NIE DZIALA