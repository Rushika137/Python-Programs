def temperature_converter(): 
   print("-----TEMPERATURE CONVERTER-----")
   while True:
    try:
        temperature = float(input("enter the temperature: "))
        break
    except ValueError:
        print("Invalid temperature. Enter a number.")
   print("1.Celsius → Fahrenheit")
   print("2.Fahrenheit → Celsius")     
   print("3.Celsius → Kelvin")
   print("4.Kelvin → Celsius")
   while True:
    try:
        conversion = int(input("choose conversion:"))

        if conversion < 1 or conversion > 4:
            print("Invalid choice. Choose between 1 and 4.")
        else:
            break

    except ValueError:
        print("Invalid choice. Enter a number.")
   if conversion == 1:
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"{fahrenheit:.2f} °F")
   elif conversion == 2:
        celsius = (temperature - 32) * 5 / 9
        print(f"{celsius:.2f} °C")
   elif conversion == 3:
        kelvin = temperature + 273.15
        print(f"{kelvin:.2f} K")
   else:
        celsius = temperature - 273.15
        print(f"{celsius:.2f} °C")
while True:
    temperature_converter()
    
    while True:
        string=input("do you want to ask again:").lower()
        if string=="yes":
            break
        elif string=="no":
            print("THANK YOU")
            exit()
        else:
            print("invalid choice,enter again")

        