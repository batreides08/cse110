# Milestone: Life Expectancy Analysis 

# Open the dataset
with open("C:/Users/Bryan Quiros/OneDrive/Escritorio/BYUI Software Dev/homework/cse110/Projects/life-expectancy.csv") as file:
    next(file)  # Skip the header line

    max_life_expectancy = -1
    min_life_expectancy = 999

    for line in file:
        parts = line.strip().split(",")
        life_expectancy = float(parts[3])  # Life expectancy is the 4th column

        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy

        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy

# Display results
print(f"The overall max life expectancy is: {max_life_expectancy}")
print(f"The overall min life expectancy is: {min_life_expectancy}")
