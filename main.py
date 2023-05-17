class vehicle():

  def __init__(self, input_make, input_model, vehicle_type):
    self.vehiclemake = input_make.title()
    self.vehiclemodel = input_model.title()
    self.vehicletype = vehicle_type
    self.vehiclefullname = '{} {}'.format(self.vehiclemake, self.vehiclemodel)

  def displayOption(self):
    print("The vehicle is a", self.vehiclefullname)


class truck(vehicle):

  def __init__(self, input_make, input_model, vehicle_type, input_extra):
    super().__init__(input_make, input_model, vehicle_type)
    self.bedlength = input_extra

  def displayOption(self):
    print(
      f"\nThe {self.vehicletype} is a {self.vehiclefullname} with a {self.bedlength} foot bed."
    )
    print(f"This {self.vehicletype} has been added to the garage.\n")


class car(vehicle):

  def __init__(self, input_make, input_model, vehicle_type, input_extra):
    super().__init__(input_make, input_model, vehicle_type)
    self.doors = input_extra

  def displayOption(self):
    print(
      f"\nThe {self.vehicletype} is a {self.vehiclefullname} with {self.doors} doors."
    )
    print(f"This {self.vehicletype} has been added to the garage.\n")


def main():

  while True:
    argument = input(
      "\nEnter 1 to make a truck, 2 to make a car, or 3 to quit: ")

    if argument == "1":
      vehicle_type = "truck"
      extra_parameter = "bed length"
      addvehicletogarage(argument, vehicle_type, extra_parameter)
      main()
    elif argument == "2":
      vehicle_type = "car"
      extra_parameter = "number of doors"
      addvehicletogarage(argument, vehicle_type, extra_parameter)
      main()
    elif argument == "3":
      print("\nThank you. Toodles!")
      quit()
    else:
      print("**** INVALID INPUT ****")
  return


def addvehicletogarage(argument, vehicle_type, extra_parameter):
  input_make = input(f"\nPlease enter the {vehicle_type} make: ")
  input_model = input(f"Please enter the {vehicle_type} model: ")
  input_extra = input(f"Please enter the {extra_parameter}: ")

  if argument == "1":
    new_truck = truck(input_make, input_model, vehicle_type, input_extra)
    new_truck.displayOption()
    return
  elif argument == "2":
    new_car = car(input_make, input_model, vehicle_type, input_extra)
    new_car.displayOption()
    return


print("Welcome to Corri's Virtual Garage!")
main()
