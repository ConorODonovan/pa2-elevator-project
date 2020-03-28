from Building import Building
from Customer import Customer
import random

if __name__ == "__main__":

    floors_entered = False
    num_floors = 0
    num_customers_entered = False
    num_customers = 0
    customers_waiting = []
    customers_in_elevator = []
    customers_on_correct_floor = []

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

    # Create customers and add to waiting list
    for i in range(num_customers):
        customer = Customer(random.randint(1, num_floors), random.randint(1, num_floors))
        customers_waiting.append(customer)

    # Testing stuff
    print("Number of floors: {}".format(building.floors))
    print("Number of customers: {}".format(num_customers))

    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))
    elevator.move()
    print("Elevator current floor: {}".format(elevator.current_floor))

    # for i in customers_waiting:
    #     print("Customer start floor: {}".format(i.start_floor))
    #     print("Customer destination floor: {}".format(i.destination_floor))
