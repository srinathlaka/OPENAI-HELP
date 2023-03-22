animals = ["Tiger", "Lion", "Zebra", "Ox"]

def length_function(animals):
    chars = 0
    for name in animals:
        chars += len(name)
    
    return("Total characters : {}, Average length {}".format(chars, chars/len(animals) ))


print(length_function(animals))