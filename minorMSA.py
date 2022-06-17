#Function Declarations
def get_float_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("value must be greater than 0 !!\n")
                continue
        except:
            print("please input a number !! :)\n")
        else:
            run_again = False

    return user_input

#INPUT
#Declare variables for known values
hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_labor_per_unit = 6
#prompt the user to enter the amount of wall to paint
#convert to a float
#if error in input ask user to re-enter input
wall_area = float(input("what is the area of wall in sq/ft??: "))

#prompt user to enter cost of paint per gallon
#convert to a float
paint_price = float(input("what is the price of paint per gallon??: "))

#PROCESS
#Calculate to hours of labor
hours_of_labor = (wall_area / unit_of_wall_area) * hours_labor_per_unit
#Calculate the cost of labor
labor_cost = hours_of_labor * hourly_labor_cost
#Calculate the amount of paint
gallons_of_paint = math.ceil(wall_area / unit_of_wall_area)
#Calculate the cost of the paint
paint_cost = gallons_of_paint * paint_price
#Calculate total cost of the job
total_cost = paint_cost + labor_cost

#OUTPUT
#Print hours of labor, cost of labor, amount of paint, cost of paint, total job cost