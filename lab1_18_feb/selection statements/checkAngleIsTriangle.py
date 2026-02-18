right_angle = int(input("Enter the right angle: "))
if(right_angle <= 0):
    print("angle should be positive")
    exit()
else:
    left_angle = int(input("Enter the left angle: "))
    if(left_angle < 0):
        print("angle should be positive")
        exit()
    else:
        bottom_angle = int(input("Enter the bottom angle: "))
        if(bottom_angle < 0):
            print("angle should be positive")
            exit()
        else:
            if(right_angle + left_angle + bottom_angle == 180):
                print("This is triangle")
            else:
                print("Not triangle")

# angle_total = right_angle + left_angle + bottom_angle