# Example: user selects number of lights
lights = int(input("Enter number of lights on your battery: "))

if lights == 0:
    # 60-minute timer
    import time
    total_minutes = 60
    for remaining in range(total_minutes, 0, -1):
        print(f"{remaining} minute(s) remaining...", end='\r')
        time.sleep(60)
    print("Time's up! Battery should be fully charged.")

elif lights == 1:
    # 40-minute timer
    import time
    total_minutes = 40
    for remaining in range(total_minutes, 0, -1):
        print(f"{remaining} minute(s) remaining...", end='\r')
        time.sleep(60)
    print("Time's up! Battery should be fully charged.")

elif lights == 2:
    # 20-minute timer
    import time
    total_minutes = 20
    for remaining in range(total_minutes, 0, -1):
        print(f"{remaining} minute(s) remaining...", end='\r')
        time.sleep(60)
    print("Time's up! Battery should be fully charged.")

elif lights == 3:
    print("Battery is already fully charged.")
    
else:
    print("Invalid input. Please enter a number between 0 and 3.")# DeWalt Battery Charging Timer
