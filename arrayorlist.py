beatles = ['George', 'Ringo', 'John', 'Paul','Raynoldo the Great']

def printathing(instring):
    "This print the argument it is passed"
    print(instring)
    return

printathing(beatles)
printathing("The length of the Beatles array is " + str(len(beatles)))
printathing(beatles[4] + " is the greatest Beatle.")