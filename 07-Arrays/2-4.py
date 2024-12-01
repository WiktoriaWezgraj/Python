'''The data below contains weekly meal plan. Write a program that prints the weekly meal
 plan along with the day name as in the example below.

WEEKLY MEAL PLAN
(Breakfast, Lunch, Dinner)
==========================
Monday: Oatmeal, Grilled Checken Salad, Spaghetti
Tuesday: ...
Wednesday: ...'''

# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

# Returns a string with day meal names
# separated by comma

def day_meal_plan(meal_plan, day_number):
    menu = ""
    for i in range(len(meal_plan[day_number])):
        menu += meal_plan[day_number][i]
        if i < len(meal_plan[day_number]) - 1:  
            menu += ", "
    return menu

# Prints weekly meal plan
for i in range(len(meal_plan)):
    print(weekday(i), ":" ,day_meal_plan(meal_plan, i))