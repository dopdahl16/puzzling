'''
What is the largest number that can be made using the integers from 1 to 10 under the following conditions:

    Addition, subtraction, division are allowed.
    Multiplication and other operations are not allowed
    All numbers must be used exactly once
    You can't divide by 0
'''
#https://puzzling.stackexchange.com/questions/128194/largest-number-possible-with-%c3%b7


integers = [1,2,3]
operands = ['+','*']
statements = []



def f(ints_remaining, statement):
    if len(ints_remaining)==1:
        statements.append(statement + str(ints_remaining[0]))
        return
    
    for i in ints_remaining:
        # f(ints_remaining[:ints_remaining.index(i)]+ints_remaining[ints_remaining.index(i)+1:], statement + str(i) + ' + ')
        # f(ints_remaining[:ints_remaining.index(i)]+ints_remaining[ints_remaining.index(i)+1:], statement + str(i) + ' - ')
        f(ints_remaining[:ints_remaining.index(i)]+ints_remaining[ints_remaining.index(i)+1:], statement + str(i) + ' * 1/')
        f(ints_remaining[:ints_remaining.index(i)]+ints_remaining[ints_remaining.index(i)+1:], statement + ' * 1/' + str(i))
        # if statement[-2:] == " ":



        # statements.append(i + (-1)*f(ints_remaining[:ints_remaining.index(i)]+ints_remaining[ints_remaining.index(i)+1:]))
        # statements.append(i * (1/(f(ints_remaining[:ints_remaining.index(i)]+ints_remaining[ints_remaining.index(i)+1:]))))
    return


f(integers, "")
print(statements)