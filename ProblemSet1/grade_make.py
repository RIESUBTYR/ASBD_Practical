X = PassingMean - PassingMinimum

Scoff = MaxMark - 0.1*(MaxMark-PassingMean)

Y = Scoff - PassingMean

Acoff = PassingMean+Y*5/8
Bcoff = PassingMean+Y*2/8
Ccoff = PassingMean-X*2/8
Dcoff = PassingMean-X*5/8
Ecoff = PassingMinimum

#Grader function
def Grader(marks :int):
    if(marks>=Scoff):
        return('S')
    elif(marks>=Acoff):
        return('A')
    elif(marks>=Bcoff):
        return('B')
    elif(marks>=Ccoff):
        return('C')
    elif(marks>=Dcoff):
        return('D')
    elif(marks>=Ecoff):
        return('E')
    return 'U'