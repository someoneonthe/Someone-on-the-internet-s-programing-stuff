cars = {
    "1970vw Bug": (286,9),
    "1979 Firebird": (412,40),
    "1980 subaru": (361,18),
    "1975 cutlass": (161, 11)
}

mycar = input("choose a car from the following:", cars.Keys())
mycar
miles, gallons = cars[mycar]
mpg = float(miles) / gallons

print("Miles:", miles)
print("Gallons:", gallons)
print"MPG", round(mpg,1)
input()