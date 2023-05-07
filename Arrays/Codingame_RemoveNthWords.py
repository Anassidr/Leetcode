the_original_phrase = "The map is clearly pretty messed up isn't it"
kids_hearing_deficits = "3 2"

words = the_original_phrase.split(" ")
indexes = kids_hearing_deficits.split(" ")


for index in indexes:
    indices = []
    i = 1
    while i*int(index) <= len(words):
        indices.append(i*int(index))
        i += 1
        
    [words.pop(x-1) for x in sorted(indices, reverse=True)]

print(*words)