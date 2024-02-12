def heating_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    else:
        print("Standby")

heating_cooling(70, 68)
heating_cooling(72, 74)
heating_cooling(72, 72)

actual_temp = int(input("Enter the actual temperature: "))
desired_temp = int(input("Enter the desired temperature: "))
print("Result based on user input:")
heating_cooling(actual_temp, desired_temp)