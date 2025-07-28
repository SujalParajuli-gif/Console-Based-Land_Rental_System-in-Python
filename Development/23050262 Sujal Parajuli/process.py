import datetime


# This is a function to rent a property
def for_rent_land(lands, to_rent_lands):
    
    # Filtering available lands
    available_property = {a: b for a, b in lands.items() if b[4] == '\tAvailable'}
    Display(available_property)
    print("\n")
    ans = input("Which land are you interested in for a rent? ")
    
    
    if ans in available_property:
        duration = int(input("How long do you want to rent the land in months? "))
        try:
            # Calculating total cost based on duration
            Cost = int(available_property[ans][3]) * duration
            print(f"The total cost for renting kitta {ans} for {duration} month's is: NPR {Cost}")
            # Storing rented land details
            to_rent_lands[ans] = {"City": available_property[ans][0], "Price": available_property[ans][3], "duration": duration, "Cost": Cost}
            lands[ans][4] = "Not Available"  # Updating land availability
        except ValueError:
            print(" Please enter valid duration in months.")    
    else:
        print("Kitta number that you have entered is not available or does not exist")

     #This is a function to return a property
def for_return_land(lands, to_return_lands):
    # Filtering rented lands
    to_rent_lands = {a: b for a, b in lands.items() if b[4] == '\tNot Available'}
    Display(to_rent_lands)
    print("\n")
    ans = input("Do you remember which land did u rent? ")
    
    if ans in to_rent_lands:
        duration = int(input("Could you please specify the months you rented the land for?"))
        real_duration = int(input("Could you please specify after how many months you are returning the land?")) 
        
        try:
            # Validating return duration
            if real_duration < duration:
                print("Invalid duration: The real duration cannot be less than the rented duration.")
                return
            
            back = real_duration - duration
            per_month_cost = int(to_rent_lands[ans][3])
            total = per_month_cost * duration
            # Calculating fine for exceeding duration
            if real_duration > duration:
                fine_per_month = 0.15 * per_month_cost
                fine = fine_per_month * back
                total += fine
                print(f"A fine must be paid for each month you have exceeded: NPR {fine}")
            
            print(f"Total cost for renting kitta {ans} with/without fine is: NPR {total}")
             
            # Including rental cost and fine in to_return_lands dictionary
            to_return_lands[ans] = {
                "City": to_rent_lands[ans][0],                
                "rental_cost": per_month_cost * duration,
                "duration": real_duration,
                "Fine": fine if real_duration > duration else 0,                
                "Price": per_month_cost,
                "Cost": total,
                "Total": total - (fine if real_duration > duration else 0)
            }
            
            lands[ans][4] = "Available" 
        
        except ValueError:
            print("Invalid input. Please enter valid duration in months.")
    else:
        print("The kitta number you entered is not rented or does not exist.")

#below is the Function for displaying lands
def Display(lands):
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Kitta\t|\t\tCity\t|\t\t\tDirection\t|\tAnna\t|\t\tPrice\t|\t\tAvailability")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    for key, value in lands.items():
        print(f"{key}\t\t{value[0]}\t\t{value[1]}\t\t{value[2]}\t\t{value[3]}\t\t{value[4]}")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")

"""
Below is theFunction for generating bill
it will help to display the rented lands and calculate the total amount
"""
def generate_bill(for_rent_land, to_return_lands):
    total = 0
    print("-------------------------------------------------------------------------------------------------------------------")
    print("Kitta\t|\tCity\t\t|\tPrice\t|\tStatus\t|\tduration\t|\tCost")
    print("-------------------------------------------------------------------------------------------------------------------")

    """
    Displaying rented lands and 
    calculating the total amount


    """
    for a, b in for_rent_land.items():
        duration = b["duration"]
        Cost = b["Cost"]
        total += Cost
        print(f"{a}\t{b['City']}\t{b['Price']}\t\tRented\t\t{duration} months\t\t {Cost}\t")

    """
    Displaying returned lands and 
    calculating the total amount


    """
    for a, b in to_return_lands.items():
        duration = b["duration"]
        rentcost = b["rental_cost"]
        fine = b["Fine"]
        returncost = rentcost + fine
        total += returncost
        print(f"{a}\t{b['City']}\t\t{b['Price']}\t|     Rented\t|\t {duration} \t\t| \t\t{rentcost}\t")
        print("-------------------------------------------------------------------------------------------------------------------")
        print(f"                                                                                         | Fine = {fine}\t\n ");
           
            
    print(f"                                                                                         | Total = {total}\t")        
    print("-------------------------------------------------------------------------------------------------------------------")
        
    
   

    return total
