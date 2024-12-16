'''
Cal Royer
11/28/24
Units 4 and 5 Exam Open Response Take 2
'''

def calculate_total_cost(meal_cost, tip_percentage):
    total_cost = meal_cost * (1 + (tip_percentage / 100))
    return round(total_cost, 2)

def main():
    while True:
        try:
            meal_cost = float(input("Enter the meal cost: "))
            tip_percentage = int(input("Enter the tip percentage: "))

            if tip_percentage < 0:
                print("Invalid tip percentage! Using default value of 15%.")
                tip_percentage = 15

            total_cost = calculate_total_cost(meal_cost, tip_percentage)
            print(f"The total cost of the meal is: ${total_cost}")
            break

        except ValueError:
            print("Invalid input. Please enter numeric values for meal cost and tip percentage.")


main()
