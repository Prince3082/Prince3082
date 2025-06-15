number = int(input("\033[92mPlease Enter your number here: \033[0m"))
counter = 1
total_sum = 0  

while counter <= 10:
    result = number * counter
    print(f'{number} x {counter} = {result}')
    total_sum += result 
    counter += 1

print(f"\033[94mTotal sum of all results is: {total_sum}\033[0m")
