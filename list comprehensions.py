multiples = []
for x in range(1,21):
    multiples.append(x*10)
    
print(multiples)

#Easy way is list comprehensions in single line


multiples = [x*10 for x in range(1,21)]
print(multiples)


#printing lengths

languages = ["Telugu", "Tamil", "German", "Hindi"]
lengths = [len(language) for language in languages]

print("Language length".capitalize())
print(lengths)