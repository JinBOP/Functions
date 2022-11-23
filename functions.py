# Conversion Calculator
# By: Jin Starks

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user
valid_data = True

def user_parser(user_input):
    global valid_data
    # Separate the number from unit
    values = user_input.rsplit(" ")
    
    number = values[0]

    if number.isdigit():
        number = float(number)
    else:
        print("not a valid number")
        valid_data = False
    
    unit = values[1]

    if unit != 'in' and unit != 'mm':
        print("not a valid unit")
        valid_data = False

    return number,unit, valid_data


while True:
    user_input = input("number and unit to convert ")
    user_number, user_unit, valid_data = user_parser(user_input)
    # check if there are invalid messages
    if valid_data:
        print("User number", user_number)
        print("User unit", user_unit)
# while True:
#   user_number = input("What number to convert? ")
#   if user_number.isdigit():
#       user_number = float(user_number)
#       break
#   else:
#       print ('please use a number')
#       user_unit = input("What unit is your number?")

# if(user_unit == 'in'):
#   #perform in to mm
#   conv_number = user_number * 25.4
#   conv_unit = 'mm'
#   break
# elif(user_unit == 'mm'):
#   #perform mm to in
#   conv_number = user_number / 25.4
#   conv_unit = 'in'
#   break
# else:
#   print('That is not a valid unit')

# print(conv_number, conv_unit)