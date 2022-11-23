# Conversion Calculator
# By: Jin Starks

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user
valid_data = True

def user_parser(user_input):
    global valid_data
    valid_data = True
    # Separate the number from unit
    values = user_input.rsplit(" ")
    
    number = values[0]

    if number.isdigit():
        number = float(number)
    else:
        print("not a valid number")
        valid_data = False
    
    unit = values[1]

    if unit != 'in' and unit != 'mm' and unit != 'ft':
        print("not a valid unit")
        valid_data = False

    return number,unit, valid_data


while True: #continue program until user exits
    while True: #check for valid data
        user_input = input("number and unit to convert ")
        user_number, user_unit, valid_data = user_parser(user_input)
        # check if there are invalid messages
        if valid_data:
            break
    #perform calculations
    if(user_unit == 'in'):
        #perform in to mm
        conv_number = user_number * 25.4
        conv_unit = 'mm'
    elif(user_unit == 'mm'):
        #perform mm to in
        conv_number = user_number / 25.4
        conv_unit = 'in'
    elif(user_unit == 'ft'):
        # perform ft to in
        conv_number = user_number * 12
        conv_unit = 'in'
    print(conv_number, conv_unit)