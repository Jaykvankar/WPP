class Converter:
    factors ={
        "inches": 1, "feet": 1/12, "yards": 1/36, "miles": 1/63360, "kilometers": 1/39370.1,
        "meters": 1/39.3701, "centimeters": 1/0.393701, "millimeters": 1/0.0393701
    }
    def __init__(self, length, unit):
        if unit in self.factors:
            self.len_inches = length / self.factors[unit]
        else:
            print("Invalid unit. Please enter a valid unit.")
    def inches(self):
        return self.len_inches * self.factors["inches"]
    def feet(self):
        return self.len_inches * self.factors["feet"]
    def yards(self):
        return self.len_inches * self.factors["yards"]
    def miles(self):
        return self.len_inches * self.factors["miles"]
    def kilometers(self):
        return self.len_inches * self.factors["kilometers"]
    def meters(self):
        return self.len_inches * self.factors["meters"]
    def centimeters(self):
        return self.len_inches * self.factors["centimeters"]
    def millimeters(self):
        return self.len_inches * self.factors["millimeters"]

while True:
    length = float(input("Enter the length: "))
    unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()

    converter = Converter(length, unit)

    print("\nChoose a unit to convert to:")
    print("1. Inches")
    print("2. Feet")
    print("3. Yards")
    print("4. Miles")
    print("5. Kilometers")
    print("6. Meters")
    print("7. Centimeters")
    print("8. Millimeters")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        print(f"{length} {unit} = {converter.inches()} inches")
    elif choice == "2":
        print(f"{length} {unit} = {converter.feet()} feet")
    elif choice == "3":
        print(f"{length} {unit} = {converter.yards()} yards")
    elif choice == "4":
        print(f"{length} {unit} = {converter.miles()} miles")
    elif choice == "5":
        print(f"{length} {unit} = {converter.kilometers()} kilometers")
    elif choice == "6":
        print(f"{length} {unit} = {converter.meters()} meters")
    elif choice == "7":
        print(f"{length} {unit} = {converter.centimeters()} centimeters")
    elif choice == "8":
        print(f"{length} {unit} = {converter.millimeters()} millimeters")
    elif choice == "9":
        print("Exiting..")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
