describe = print("""Hi!Let\'s play something cool:
you told me every sentance you want,
and i told you how many words have:""")
question = str(input())
words = len(question.split())
rezult = "You just told me a sentence of" +" " + str(words) + "  words"
print(rezult)
 