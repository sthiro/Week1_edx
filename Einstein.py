def Einstein(mass):
    return mass * pow(300000000,2) # Power is the higher priority than multiplican, First it find the value of c^2 and then does the multiplication operation.

val = int(input("m: ")) # Input and convert string into integer
Energy = Einstein(val)

print("E:",Energy)