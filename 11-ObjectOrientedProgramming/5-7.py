'''Write a program containing a Statistics class that describes the properties of any set of numbers. The class should allow to:

Add to the set of numbers, the next number read from the keyboard (store the numbers in the array)
Display all numbers separated by a space
Determine the greatest number
Determine the smallest number
Calculate the arithmetic mean of numbers
Calculate of the median
Print of calculated / determined statistical quantities (minimum, maximum, arithmetic mean, median)
Then, use the program for numbers below to calculate and print the basic staticstics:

12, 37, 6, 9, 17'''

class Statistics:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        """Display all numbers separated by a space."""
        print("Numbers:", self.numbers)

    def get_minimum(self):
        """Return the smallest number."""
        if self.numbers:
            return min(self.numbers)
        return None

    def get_maximum(self):
        """Return the greatest number."""
        if self.numbers:
            return max(self.numbers)
        return None

    def calculate_mean(self):
        """Calculate and return the arithmetic mean."""
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        return None

    def calculate_median(self):
        """Calculate and return the median."""
        if self.numbers:
            sorted_numbers = sorted(self.numbers)
            n = len(sorted_numbers)
            mid = n // 2
            if n % 2 == 0:
                return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
            return sorted_numbers[mid]
        return None

    def display_statistics(self):
        """Print the minimum, maximum, mean, and median."""
        minimum = self.get_minimum()
        maximum = self.get_maximum()
        mean = self.calculate_mean()
        median = self.calculate_median()

        print("Statistics:")
        print(f"  Minimum: {minimum}")
        print(f"  Maximum: {maximum}")
        print(f"  Mean: {mean:.2f}")
        print(f"  Median: {median:.2f}")

# Main program
def main():
    stats = Statistics()
    numbers_to_add = [12, 37, 6, 9, 17]  # Predefined numbers

    # Add numbers to the statistics
    for number in numbers_to_add:
        stats.add(number)

    # Display all numbers
    stats.display_numbers()

    # Display calculated statistics
    stats.display_statistics()

if __name__ == "__main__":
    main()