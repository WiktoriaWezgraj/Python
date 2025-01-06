'''In a beverage factory, a machine fills 500ml bottles. The computer checks whether the bottle has been filled correctly. 
For a 500ml bottle, the allowable tolerance is 2%. In the last ten bottles checked, the filling was:

508,500,512,499,492,511,503,476,501,509
Write a program that calculates the percentage of incorrectly filled bottles. Use the filter() along with a higher order function. Sample result:

Bottle capacity:    500ml
Filling tolerance:  2%
Filled bottles:     508,500,512,499,492,511,503,476,501,509
Incorrectly filled: 30%'''

filling = [508,500,512,499,492,511,503,476,501,509]
def check(fill):
    if 510 >= fill >= 490:
        return fill

result = list(filter(lambda fil: check(fil), filling))
incorrect_count = len(filling) - len(result)
incorrect_percentage = (incorrect_count / len(filling)) * 100
print(incorrect_percentage)

