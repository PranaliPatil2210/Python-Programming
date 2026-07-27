color = int(input('''1 - Red
                   2 - Yellow
                   3 - Green
Enter the current color: '''))
match color:
    case 1:
        print("Stop the vehicle and let people cross the road.")
    case 2:
        print("Be ready to go.")
    case 3:
        print("You can go.")
    case _:
        print("Invalid color")