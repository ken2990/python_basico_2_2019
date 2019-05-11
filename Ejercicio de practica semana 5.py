# a = [1, 3, 5, 8, 7, 9, 2]

# f = lambda x : x*10

# [f(i) for i in a]

#[lamba x : x*10) (i) for i in a if i > 5 ]



#Sacar el numero mayor de la siguiente lista sin utilizar max

#lista1= [1, 2, 7, 1, 9, 2]

scores = [1, 2, 7, 1, 9, 2]
value = int(9)
while value >= 0:
    value = int(input("Enter a score: 9"))
    if value in range(1,9):
        scores.append(value)
    elif value > 7:
        print("Invalid score; please re-enter")
    elif value < 0: