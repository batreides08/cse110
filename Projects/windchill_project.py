"""
Author: Bryan Quiros
Purpose: To provide the user wind chill values for various wind speeds 

"""

# Ask the user for the temperature
temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

# Convert Celsius to Fahrenheit if needed
if unit == 'C':
    temperature = (temperature * 9/5) + 32

# Loop through wind speeds from 5 to 60 mph (inclusive), incrementing by 5
wind_speed = 5
while wind_speed <= 60:
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
    wind_speed += 5
