describe = print("""Hi!Let\'s play something cool:
you tell me any sentence you want
and I will tell you how many words it contains:""")
question = str(input())
words = len(question.split())
rezult = "You just told me a sentence made of" +" " + str(words) + "  words"
print(rezult)
 
