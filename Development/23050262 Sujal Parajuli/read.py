"""
below is a function for writing land details to a file
this will write the land details to a .txt file in the folder that we have this read.py file
"""
def for_writting_file(filename, lands):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Writing headers to the file
        file.write("Kitta     |  \tCity              |   \tDirection        |  \tAnna    |  \tPrice       |\tAvailability |\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------\n")
        # Writing land details to the file
        for a, b in lands.items():
            file.write(f"{a}\t{b[0]}\t{b[1]}\t\t{b[2]}\t{b[3]}\t\t{b[4]}\n")
    