import datetime
# Function to write billing information to a file

def for_writting_bill(name, address, contact, to_rent_lands, to_return_lands):  
    """
    Getting current date and time
    adding year, month, day, hour and minute to the date
    and generating a unique bill ID based on the current date and time
    """
    date = datetime.datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    hour = str(date.hour)
    minute = str(date.minute)
    id_ = year + month + day + hour + minute
    
    # Generating file name based on customer name and bill ID
    file_name = name +id_ +".txt"

    # Opening the file in write mode
    with open(file_name, "w") as file:
        # Writing company information to the file
        file.write("\n\n" +
                   "                                             Techno Property Nepal\n " +
                   "                                          Address: Kathmandu, Nepal\n " +
                   "                                             Contact No: 071-59999\n"+
                   "                                    Email: NepalTechnoProperty12@gmail.com\n"  
                   "                                   ---------------------------------------\n ");
                  
        
        # Writing date and billing information to the file
        file.write("\n")
        file.write("Bill ID: " + str(id_) + "\n")
        file.write("Customer Name: " + name + "\n");
        file.write("Customer Address: " + address  + "\n");
        file.write("Customer Contact: " + contact + "\n");
           

        Total = 0
        
         # heading for the bill details
        file.write("\n");
        file.write("Kitta\t|\tCity\t\t|\tPrice\t|\tStatus\t|\tduration\t|\tCost\n" );
        file.write("-------------------------------------------------------------------------------------------------------------\n ");
       

    # Displaying rented lands and calculating total cost
        for a, b in to_rent_lands.items():
            duration = b["duration"]
            Cost = b["Cost"]
            Total += Cost
            file.write(f"{a}\t{b['City']}\t{b['Price']}\t\tRented\t\t{duration}  \t\t\t{Cost}\n");
        
     # Displaying returned lands and calculating total cost
        for a, b in to_return_lands.items():
            duration = b["duration"]
            rentcost = b["rental_cost"]
            fine = b["Fine"]
            returncost = rentcost + fine
            Total += returncost
            file.write(f"{a}\t{b['City']}\t\t{b['Price']}\t     Rented\t\t  {duration} \t\t\t{returncost}\n");    
            file.write("\n");
            file.write("-------------------------------------------------------------------------------------------------------------\n ");
            file.write(f"                                                                                 | Fine = {fine}\t\n ");         
        file.write(f"                                                                                | Total = {Total}\t")  
        file.write("------------------------------------------------------------------------------------------------------------- ");
        file.write("\n");   
           