
def fb():
    lst = []
    for i in range(1,101):
        if(i % 5 == 0 and i % 3 == 3):
            lst.append("FizzBuzz")
        elif(i % 3 == 0):
            lst.append("Fizz")
        elif(i % 5 == 0):
            lst.append("Buzz")
        else:
            lst.append(str(i))
    return lst