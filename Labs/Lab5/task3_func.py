# Write a program to solve a classic puzzle: We count 35 heads and 94 legs 
# among the chickens and rabbits in a farm. How many rabbits and how many 
# chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    rabbit = (numlegs - 2*numheads) / 2
    chicken = numheads - rabbit
    print("Number of rabbits: ", rabbit, "\nNumber of chickens: ", chicken)


numheads = 35
numlegs = 94
solve(numheads, numlegs)
