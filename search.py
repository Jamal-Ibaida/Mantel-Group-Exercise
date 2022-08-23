import csv

# CSV file reader
def csv_reader(id):

    found = 0

    # Opening file with correct encoding
    with open("sets.csv", encoding="utf8") as data:

        # Saving csv data as Dict
        read = csv.DictReader(data)

        # Search through rows until id is found then set values
        for row in read:
            if row["set_id"] == id:
                name = row["name"] 
                year = row["year"] 
                theme_id = row["theme_id"]
                num_parts = row["num_parts"]
                found = 1

    if found == 0:
        print("This set_id does not exist, Try again")
        return ''

    with open("themes.csv", encoding="utf8") as data:
        read = csv.DictReader(data)
        for row in read:
            if row["id"] == theme_id:
                theme = row["name"]
    
    str_print = "\nResult\n------------------" + "\nName: " + name + "\nYear released: " + year + "\nTheme name: " + theme + "\nNumber of parts: " + num_parts + "\n------------------\n"
    return str_print

def main():

    done = False
    while done == False:
        set_id = input("Enter set_id or type 'exit' to end program: ")
        
        if set_id == "exit":
            done = True
        else:
            result = csv_reader(set_id)

            print(result)
        

main()