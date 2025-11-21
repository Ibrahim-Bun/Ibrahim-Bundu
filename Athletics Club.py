print("Welcome to the Athletics Race Records!")

laneorder_men = []
laneorder_women = []


#input validation for number of athletes
while True:
    try:
        num_athletes = int(input("Enter number of athletes in race: "))
        if 4<= num_athletes <=8:
            break
        else:
            print("Try again, enter number between 4 and 8: ")
    except ValueError:
            print("Invalid input, please enter a number: ")
        

#input validation for gender
while True:
    try:
        choice = int(input("Enter [1] for male or [2] for female: "))
        if choice == 1 or choice == 2:
            break
        else:
            print("Choose either male (1) or female(2): ")
    except ValueError:
            print("Invalid input, please enter a number: ")
            
        
#mens 100m
if choice == 1:
    for i in range(num_athletes):
        finish_time = float(input(f"Enter finishing time for male athlete in lane {i+1}: "))
        laneorder_men.append(finish_time)
        
    
        if finish_time <9.58:
            print("Men's 100m World record achieved!")
        elif finish_time <9.86:
            print("Men's 100m European record achived!")
        elif finish_time <9.87:
            print("Men's 100m British record achieved!")

    laneorder_men.sort()      

    print("Men's 100m race results fastest to slowest" ,laneorder_men)


#womens 100m
elif choice == 2:
    for i in range(num_athletes):
        finish_time = float(input(f"Enter finishing time for female athlete in lane {i+1}: "))
        laneorder_women.append(finish_time)

                    
        if finish_time <10.49:
            print("Women's 100m World record achieved!")
        elif finish_time <10.73:
            print("Women's 100m European record achived!")
        elif finish_time <10.99:
            print("Women's 100m British record achieved!")
            
#sorting list fastest to slowest
    laneorder_women.sort()  

    print("Women's 100m race results fastest to slowest" ,laneorder_women)
            
