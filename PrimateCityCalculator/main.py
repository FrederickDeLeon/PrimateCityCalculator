# PrimateCityCalculator 
# A primate city is a city that is overwhelmingly dominant in its county or region, either in terms of population,
# economic activity, or cultural significance, or a combination of all these factors.

# This program calculates whether a given city is a primate city based on its population compared to other cities in
# country or region. A commonly used threshold is that the largest city must have more than twice the population of 
# the second largest city to be considered a primate city.

# The program provides users with multiple methods to determine the primacy of a city. 

def main():
    
    greetingMsg = "Primate City Calculator"
    print(greetingMsg) 
    
    optionsMenu = "Which method would you like to use to calculate primate city status?\n" \
                  "1. 2 City Population Ratio\n" \
                  "2. 3 City Population Ratio\n" \
                  "3. Jefferson's Index of Primacy\n"
    print(optionsMenu) 
    
    menuInput = input("Enter the number corresponding to your choice: ")
    if menuInput == '1':
        method_1()
    elif menuInput == '2':
        method_2()
    elif menuInput == '3':
        jefferson_index()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
    

# Method 1: 2 City Population Ratio
def method_1():
    print("Method 1: 2 City Population Ratio selected.")
    method1Input_A = input("Please enter the population of the largest city: ")
    method1Input_B = input("Please enter the population of the second largest city: ")
    primateNumber = int(method1Input_A) / int(method1Input_B)
    print(f"The primate city ratio is: {primateNumber}")
    if primateNumber > 2:
        print("The largest city is a primate city.")
    else:
        print("The largest city is not a primate city.")


# Method 2: 3 City Population Ratio
def method_2():
    print("Method 2: 3 City Population Ratio selected.")
    method2Input_A = input("Please enter the population of the largest city: ")
    method2Input_B = input("Please enter the population of the second largest city: ") 
    method2Input_C = input("Please enter the population of the third largest city: ")
    primateNumber = int(method2Input_A) / (int(method2Input_B) + int(method2Input_C))
    print(f"The primate city ratio is: {primateNumber}")
    if primateNumber > 2:
        print("The largest city is a primate city.")
    else:
        print("The largest city is not a primate city.")

# Method 3: Jefferson's Index of Primacy
def jefferson_index():
    print("Method 3: Jefferson's Index of Primacy selected.")
    jeffersonInput_A = input("Please enter what percent of the population of the largest city lives in the second largest city: ")
    jeffersonInput_B = input("Please enter what percent of the population of the largest city lives in the third largest city: ")
    print(f"The Index of Primacy is 100-{int(jeffersonInput_A)}-{int(jeffersonInput_B)}")
    if 100 > 2*(int(jeffersonInput_A)):
        print("The largest city is a primate city.")
    else:
        print("The largest city is not a primate city.")

if __name__ == "__main__":
    main()










