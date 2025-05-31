from random import choice

answers = ('It is certain', 'As I see it, yes.', 'Reply hazy, try again.', 'Do not count on it.', 'It is decidedly so.', 'Most likely.', 'Ask me again later.', 'My sources say no.')

# Number 1 - It is certain.
# Number 2 - As I see it, yes.
# Number 3 - Reply hazy, try again.
# Number 4 - Do not count on it.
# Number 5 - It is decidedly so.
# Number 6 - Most likely.
# Number 7 - Ask me again later.
# Number 8 - My sources say no.

def shaking(times):
  count = 0

  while count < times:
    print('Shaking...')
    count += 1

print("**Welcome to Magic 8 Ball!**")
print(input("What is on your mind? Enter a question and press ENTER to shake\n"))
shaking(4)
print("My choice is", choice(answers))