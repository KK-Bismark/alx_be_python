# A python program that converts temperatures between Celsius and Fahrenheit, 
# using global variables to store conversion factors.


# Global variables
#FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# A function to convert from fahrenheit to celcius
def convert_to_celsius(fahrenheit):
    temp_celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_celcius


# A function to convert from celcius to fahrenheit
def convert_to_fahrenheit(celsius):
    temp_fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return temp_fahrenheit


# Main Function
def main():
    # prompt for user values
    user_temp = float(input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F) ").upper()

    # check to see which function to call
    if temp_unit == 'C':
        new_temp = convert_to_fahrenheit(user_temp)
        new_temp_unit = 'F'
    elif temp_unit == 'F':
        new_temp = convert_to_celsius(user_temp)
        new_temp_unit = 'C'
    else:
        print("You selected a wrong unit.")

    # print the new temperature in the converted unit
    dgr = "\u00B0"
    print(f"{user_temp}{dgr}{temp_unit} is {new_temp}{dgr}{new_temp_unit}")



if __name__ == "__main__":
    main()
