def PutQuotes(s):
    return s.lower().replace(" ","").split(',')

print(PutQuotes('peppers, beans, broccoli, cabbage, carrots, catnip, chives, corn, dill, eggplant, garlic, onions, parsnips, sunflowers, tomatoes'))