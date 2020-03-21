from Building import Building

if __name__ == "__main__":

    floors_entered = False
    floors_input_int = 0
    num_customers_entered = False
    num_customers_input_int = 0

    # User entering number of floors
    while not floors_entered:
        floors_input = input("How many floors does the building have?")

        try:
            floors_input_int = int(floors_input)
            if floors_input_int < 1 or floors_input_int > 10:
                print("Invalid number of floors!")
                continue
            else:
                floors_entered = True
                continue
        except:
            print("This is not a valid entry")
            continue

    # User entering number of customers
    while not num_customers_entered:
        num_customers_input = input("How many customers are in the building?")

        try:
            num_customers_input_int = int(num_customers_input)
            if num_customers_input_int < 1 or num_customers_input_int > 10:
                print("Invalid number of floors!")
                continue
            else:
                num_customers_entered = True
                continue
        except:
            print("This is not a valid entry")
            continue

    # Testing stuff
    my_building = Building(floors_input_int)
    print("Number of floors: {}".format(my_building.floors))
    print("Number of customers: {}".format(num_customers_input_int))
