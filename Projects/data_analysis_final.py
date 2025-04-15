"""
Author: Bryan Quiros
Purpose: To provide life expectancy results by country to user prompts

"""

# Initialize overall tracking variables
max_life = -1
min_life = 999
max_country = ""
min_country = ""
max_year = 0
min_year = 0

# Ask for year of interest
year_of_interest = input("Enter the year of interest: ")

# Initialize year specific variables
year_total = 0
year_count = 0
year_max = -1
year_min = 999
year_max_country = ""
year_min_country = ""

# Read and process the file
with open("C:/Users/Bryan Quiros/OneDrive/Escritorio/BYUI Software Dev/homework/cse110/Projects/life-expectancy.csv") as file:
    next(file)  

    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        year = int(parts[2])
        life = float(parts[3])

        # Overall max/min
        if life > max_life:
            max_life = life
            max_country = country
            max_year = year
        if life < min_life:
            min_life = life
            min_country = country
            min_year = year

        # Year specific analysis
        if str(year) == year_of_interest:
            year_total += life
            year_count += 1

            if life > year_max:
                year_max = life
                year_max_country = country
            if life < year_min:
                year_min = life
                year_min_country = country

# Output results
print(f"\nThe overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

if year_count > 0:
    year_avg = year_total / year_count
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {year_avg:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max}")
    print(f"The min life expectancy was in {year_min_country} with {year_min}")
else:
    print(f"No data found for the year {year_of_interest}.")
