arr = []

while True:
    arr_amount = int(input("Enter amount of numbers to enter into list: "))
    if -100<arr_amount<100:
        break
    else:
        print("Invalid input, enter an amount from -100 to 100: ")
    


for i in range(arr_amount):
    n = int(input(f"Enter score {i+1} "))
    if 2<= n <= 10:
        arr.append(n)  
    else:
        print("Invalid input, enter a number from 2 to 10: ")

arr.sort(reverse = False)

runner_up = arr[1]

print(runner_up)
print(arr)



