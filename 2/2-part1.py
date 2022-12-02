rock = 1
paper = 2
scissors = 3
draw = 3
win = 6
total = 0
n = 0
with open ("input") as f:
    input = f.readlines()
    for i in input:
        if input[n] == "A Y\n":
            total = total + paper + win
        elif input[n] == "A X\n":
            total = total + rock + draw
        elif input[n] == "A Z\n": 
            total = total + scissors
        elif input[n] == "B X\n": 
            total = total + rock
        elif input[n] == "C Z\n": 
            total = total + scissors + draw         
        elif input[n] == "B Z\n": 
            total = total + scissors + win
        elif input[n] == "C Y\n": 
            total = total + paper
        elif input[n] == "B Y\n": 
            total = total + paper + draw
        elif input[n] == "C X\n": 
            total = total + rock + win
        n = n + 1
    print(f'Answer: {total}')