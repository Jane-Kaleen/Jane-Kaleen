def convert_c_to_f(temp_in_celsius):
    temp_in_fahrenheit = temp_in_celsius * 1.8 + 32
    return (temp_in_fahrenheit)

temp_from_user=int(input("What Celsius temmp do you want to convert?"))
temperature_in_f = convert_c_to_f(temp_from_user)
print(temperature_in_f)