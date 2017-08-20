from random import choice

class WordBot(object):
    def __init__(self, words, answer):
        self.letters = list('etaoinsrhldcumfpgwybvkxjqz')
        self.possible_words = []
        for word in words:
            # print(len(word), len(answer))
            if len(word) == len(answer):
                self.possible_words.append(word)
        # print(len(words), len(self.possible_words))

    def guess(self, answer):
        guess_letter = ''
        guess_letter = self.letters.pop(0)
        # print(guess_letter, end=" ")
        return guess_letter

looping = True
words = []
count = 10
won = True

with open('words.txt', 'r') as fp:
    for word in fp:
        words.append(word)

word = choice(words).lower().strip('\n')
answer = []

for i in range(len(word)):
    out = '_'
    if word[i] == " ":
        out = " "
    answer.append(out)

bot = WordBot(words, answer)

while count > 0:
    print(''.join(answer))
    #user_input = input("Let's play hangman. ")
    user_input = bot.guess(answer)
    if user_input in word:
        for i in range(len(word)):
            if word[i] == user_input:
                answer[i] = word[i]
        won = True
    else:
        count -= 1
    if '_' in answer:
        won = False
    # print(user_input, word, ''.join(answer), word == ''.join(answer))
    if word == ''.join(answer):
        count = 0
if won:
    print("HUZZAH!!!")
else:
    print("you lose. The word was {}".format(word))
