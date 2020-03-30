from Building import Building

if __name__ == "__main__":

    floors_entered = False
    num_floors = 0
    num_customers_entered = False
    num_customers = 0

    # User entering number of floors
    while not floors_entered:
        floors_input = input("How many floors does the building have?")

        try:
            num_floors = int(floors_input)
            if num_floors < 1 or num_floors > 10:
                print("Invalid number of floors!")
                continue
            elif num_floors == 1:
                print("The building must have at least two floors!")
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
            num_customers = int(num_customers_input)
            if num_customers < 1 or num_customers > 10:
                print("Invalid number of floors!")
                continue
            else:
                num_customers_entered = True
                continue
        except:
            print("This is not a valid entry")
            continue

    # Create building
    building = Building(num_floors)
    elevator = building.create_elevator()
    building.create_customers(num_customers)
    print("sdfgjhklsdhgkl: {}".format(building.customers_waiting))

    # Primary loop for checking customers and moving elevator
    while True:
        if len(building.customers_waiting) == 0 and len(elevator.customers_in_elevator) == 0:
            print("All customers arrived!")
            break

        # Check customers waiting and move them into elevator
        for i in building.customers_waiting:
            if i.start_floor == elevator.current_floor:
                building.customers_waiting.remove(i)
                elevator.enter(i)

        # Check customers in elevator and move them onto correct floor
        for i in elevator.customers_in_elevator:
            if i.destination_floor == elevator.current_floor:
                elevator.exit(i)
                building.customers_arrived.append(i)

        # For testing
        print("Current floor: {}".format(elevator.current_floor))
        print("Customers waiting: {}".format(building.customers_waiting))
        print("Customers in elevator: {}".format(elevator.customers_in_elevator))
        print("Customers arrived: {}".format(building.customers_arrived))

        elevator.move()

    # Testing stuff
    print("Number of floors: {}".format(building.floors))
    print("Number of customers: {}".format(num_customers))
