from enum import *
from itertools import combinations
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self) -> str:
        return self.suit + " " + self.value


def scoreHand(cards):
    total_points = 0
    combos = generateSets(cards)
    total_points += countFifteens(combos)
    total_points += countPairs(combos)
    total_points += countRuns(cards)
    total_points += countFlush(cards)
    return total_points

def countFifteens(combos):
    points = 0
    for combo in combos:
        total = 0
        if len(combo) > 1:
            for card in combo:
                total += values_map[card.value]
            if total == 15:
                points += 2
    return points

def countPairs(combos):
    points = 0
    for combo in combos:
        if len(combo) == 2 and combo[0].value == combo[1].value:
            points += 2
    return points

def countRuns(cards):
    points = 0
    sequential_lists = []
    cards = sorted(cards, key=lambda x: values_order[x.value])

    current_sequence = [cards[0]]
    for i in range(1, len(cards)):
        if values_order[cards[i].value] == values_order[current_sequence[-1].value] + 1 or values_order[cards[i].value] == values_order[current_sequence[-1].value]:
            current_sequence.append(cards[i])
        else:
            if len(current_sequence) > 1:
                sequential_lists.append(current_sequence)
            current_sequence = [cards[i]]
    if len(current_sequence) > 1:
        sequential_lists.append(current_sequence)

    for lst in sequential_lists:
        runs = generateRuns(lst)
        for run in runs:
            points += len(run)
    return points

def countFlush(cards):
    points = 0
    hearts = []
    clubs = []
    diamonds = []
    spades = []
    for card in cards:
        if card.suit == "Hearts":
            hearts.append(card)
        if card.suit == "Clubs":
            clubs.append(card)
        if card.suit == "Diamonds":
            diamonds.append(card)
        if card.suit == "Spades":
            spades.append(card)
    if len(hearts) > 3:
        points += len(hearts)
    if len(clubs) > 3:
        points += len(clubs)
    if len(diamonds) > 3:
        points += len(diamonds)
    if len(spades) > 3:
        points += len(spades)
    return points

def generateSets(elements):
    all_sets = []

    def generate(current_set, remaining_elements):
        if len(remaining_elements) == 0:
            all_sets.append(current_set)
            return

        generate(current_set + [remaining_elements[0]], remaining_elements[1:])
        generate(current_set, remaining_elements[1:])

    generate([], elements)
    return all_sets

def generateRuns(elements):
    all_sets = []

    def generate(current_set, remaining_elements):
        if len(remaining_elements) == 0:
            if len(current_set) > 2:
                all_sets.append(tuple(current_set))
            return
        if current_set[-1].value == remaining_elements[0].value:
            generate(current_set[:-1] + [remaining_elements[0]], remaining_elements[1:])
            generate(current_set, remaining_elements[1:])
        else:
            generate(current_set + [remaining_elements[0]], remaining_elements[1:])
    
    generate([elements[0]], elements[1:])
    all_unique_runs = list(set(all_sets))
    return all_unique_runs



deck = []
suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
card_names = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
values_map = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10}
values_order = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":11,"Queen":12,"King":13}
hand = []
cut_card = 0

for suit in suits:
    for name in card_names:
        deck.append(Card(suit, name))


# Code block to randomly draw a cut card and a hand from a 52 card deck
        
# cut_card = random.choice(deck)
# deck.remove(cut_card)

# for i in range(6):
#     card = random.choice(deck)
#     hand.append(card)
#     deck.remove(card)
        
# scoreHand(hand, cut_card)

        
# Code block to determine highest scoring MEGA hand and cut card
        
all_scores = []
highest_score = 0
highest_scoring_hands = []

all_hands = combinations(deck, 7)

for hand in all_hands:
    score = scoreHand(hand)

    if score == highest_score:
        highest_scoring_hands.append(hand)

    if score > highest_score:
        highest_score = score
        highest_scoring_hands = [hand]

    all_scores.append(score)

    
print(max(all_scores))
print()