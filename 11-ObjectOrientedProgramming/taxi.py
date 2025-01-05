class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare

    def print_receipt(self):
        return f"{self.distance}, {self.rate_per_km}, {self.fare}"


def main():
    taxi1 = TaxiRide(2)
    taxi1.calculate_fare(100)
    print(taxi1.print_receipt())



if __name__ == "__main__":
    main()
