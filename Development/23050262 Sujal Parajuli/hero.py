import datetime
from process import *  # Importing functions from seperate module
from read import *  
from write import * 
def hero():
    
    # Getting customer information
    name=input("\nPlease enter your Name: ").upper()
    address=input("Please enter your Address: ").upper()
    contact=(input("Please enter your number: "))


    # To diaplay the companies land and other details in our program!
    print("\n")
    print("                                                WELCOME!!!\n")
    print("                                           Techno Property Nepal")
    print("                                        Location: Kathmandu, Nepal")
    print("                                            Contact No: 071-59999")
    print("                                  Email: NepalTechnoProperty12@gmail.com\n\n")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("Kitta      |   \tCity             |\tDirection     |\t\tAnna   |\tPrice   |\tAvailability    |")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("\n")
    # Custom Land Details which will be used throughout our program!
    dic = {
        '1': ['\tBhairahawa', '\tSouth',   '\t3', '\t90000', '\tAvailable'],

        '2': ['\tKathmandu '  , '\tWest',   '\t4', '\t100000', '\tNotAvailable'],
 
        '3': ['\tBhaktapur', '\tSouth',   ' \t5', '\t80000', '\tAvailable'],
  
        '4': ['\tDillibazar ', '\tEast',    '\t6', '\t120000', '\tNot Available'],
        
        '5': ['\tLalitpur ',  '\tNorth',   '\t7', '\t50000', '\tAvailable'],

        '6': ['\tDharan',    '\t\tWest',   '\t8', '\t30000', '\tNot Available'],

        '7': ['\tItahari',    '\t\tEast',   '\t9', '\t60000', '\tNot Available']
        
    }

    
# To Display Custom land details
    for key, value in dic.items():
        print(f"{key}\t{value[0]}\t{value[1]}\t\t{value[2]}\t{value[3]}\t{value[4]}")
        print("-------------------------------------------------------------------------------------------------------------------")        

        print("\n\n")
    print(" \nTo rent a land, Please input 'rent'")
    print("\nTo return a land, please input'return'")
   
# Initializing dictionaries to store rented and returned lands
    to_rent_lands = {}
    to_return_lands= {}
        
    # Loop to handle user interactions
    next = True  # Initialize a variable for the first choice

    final_choice = None  # Initialize a variable for last choice 

    while next:
            if final_choice is None:
                reason = input("\nWhat do you want to do, rent or return?").lower()
            else:
                reason = final_choice
            print("\n")
            
            try:
                # Renting a land
                if reason == "rent":
                    for_rent_land(dic, to_rent_lands)
                    final_choice = "rent"  # Update last choice
                    
                # Returning a land
                elif reason == "return":
                    for_return_land(dic, to_return_lands)
                    final_choice = "return"  # Update last choice
                    
                
                else:
                    print("Your Input is Invalid!")
            except Exception as e:
                print("Error:", e)

    # To ask for continuation of the program
            while True:
                try:
                    ans = input("Would you like to continue? (yes/no): ").lower()
                    print("\n\n")
                    if ans == "yes":
                        break  
                    # It will Break out of the loop and continue the code.
                    elif ans == "no":
                        next = False
                        break 
                     # It will Break out of the loop and stop the code.
                    else:
                        print("Please enter 'yes' or 'no'.\n")
                except Exception as e:
                    print("An error occurred:", e)

    # Check if there are rented or returned lands before generating the bill
            if to_rent_lands or to_return_lands:
                try:
                        # Displaying billing information
                        print("\n")
                        print("                                                Techno Property Nepal ")
                        print("                                               Address: Kathmandu, Nepal")
                        print("                                                   Contact: 071-59999")
                        print("                                        Email: NepalTechnoProperty12@gmail.com\n\n")

                    # Generating a unique bill ID based on the current date and time.
                        year = str(datetime.datetime.now().year)
                        month = str(datetime.datetime.now().month)
                        day = str(datetime.datetime.now().day)
                        hour = str(datetime.datetime.now().hour)                                       
                        id_ = year + month + day + hour 

                        print("\t\t\t\t\t\t\t\t\t\tDate: ", year, "/", month, "/", day,"/", hour ,"\n\n")
                        print("Bill ID: ", id_)
                        print("Customer Name: ", name)
                        print("Customer Address: ", address)
                        print("Customer Contact: ", contact)
                        print("\n")

                        # Generating and displaying the bill
                        generate_bill(to_rent_lands, to_return_lands)
                        
                        # Writing billing information to a file
                        for_writting_bill(name, address, contact, to_rent_lands, to_return_lands)
                        print("\n") 
                        print("Above is the invoice for the land(s) you recently inquired about.") 
                        print("\n") 
                    
                except Exception as e:
                    print("An error occurred while generating the bill:", e)
            else:
                    print("No lands have been rented or returned, so no bill is generated.")

 
    # Writing all land details to a file
    for_writting_file("land_dic_details.txt", dic)

#to only display the main file(hero)

hero()
