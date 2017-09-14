cards = []
for suite in ["Spades", "Clubs", "Hearts", "Diamonds"]:
    for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
        cards.append(f'{rank} of {suite}')
print(len(cards))

for i in range(1, 10):
    print(f"    >i = {i}")

