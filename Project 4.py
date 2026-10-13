#==========================================================================
#    Project      4:        Temprature converter
#==========================================================================

print("1. Celsius se Fahrenheit")
print("2. Fahrenheit se Celsius")

choice = input("Number likho: ")

if choice == "1":
    c = float(input("Celsius likho: "))
    f = (c * 9/5) + 32
    print("Fahrenheit =", f)

elif choice == "2":
    f = float(input("Fahrenheit likho: "))
    c = (f - 32) * 5/9
    print("Celsius =", c)

else:
    print("Galat number")
