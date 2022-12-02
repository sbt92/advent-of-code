with open ("input") as f:
    input = f.readlines()
    n = 0
    calories = 0
    food=[]
    for i in input:
        if input[n] != '\n':
            calories = calories + int(input[n])
        else:
            food.append(calories)
            calories = 0
        n = n + 1
    calories = max(food)
    print(f'Part 1 Answer: {calories}')
    food_sorted=sorted(food, reverse=True)
    top_three_calories_total=food_sorted[0] + food_sorted[1] + food_sorted[2]
    print(f'Part 2 Answer: {top_three_calories_total}')