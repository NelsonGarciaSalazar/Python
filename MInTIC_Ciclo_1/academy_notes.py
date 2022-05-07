''''
    Build a program in python, that given the notes of the retos (5 retos), English and coaching determited
    the qualification of an alumno. In case note be mayor or eqyal than 3.0 must print on screen "passed" The challenge
    aquals to 80%. English to 10% and coaching to 10% of the note. 
'''

note_1 = float(input("Intro note one: "))
note_2 = float(input("Intro note two: "))
note_3 = float(input("Intro note there: "))
note_4 = float(input("Intro note four: "))
note_5 = float(input("Intro note five: "))

notePython = (note_1 + note_2 + note_3 + note_4 + note_5) / 5.0
noteEnglish = float(input("Intro note English: "))
noteCoaching = float(input("Intro note Coaching: "))

noteFinal = (notePython * 0.8) + (noteEnglish * 0.1) + (noteCoaching * 0.1)

if noteFinal >= 3.0:
    print("Your passed the course with final note:", round(noteFinal,2))
else:
    print("Your don't passed the course with final note:", round(noteFinal,))