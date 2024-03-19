from enum import *
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self) -> str:
        return self.suit + " " + self.value


def scoreHand(hand, cut_card):
    total_points = 0
    cards = hand + [cut_card]
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
hands_seen = set()
indicies_of_cards_in_play = set()
for cut_card_index in range(len(deck)):
    indicies_of_cards_in_play.add(cut_card_index)

    for card1_index in range(len(deck)):
        if card1_index not in indicies_of_cards_in_play:
            indicies_of_cards_in_play.add(card1_index)

            for card2_index in range(len(deck)):
                if card2_index not in indicies_of_cards_in_play:
                    indicies_of_cards_in_play.add(card2_index)

                    for card3_index in range(len(deck)):
                        if card3_index not in indicies_of_cards_in_play:
                            indicies_of_cards_in_play.add(card3_index)

                            for card4_index in range(len(deck)):
                                if card4_index not in indicies_of_cards_in_play:
                                    indicies_of_cards_in_play.add(card4_index)

                                    for card5_index in range(len(deck)):
                                        if card5_index not in indicies_of_cards_in_play:
                                            indicies_of_cards_in_play.add(card5_index)

                                            for card6_index in range(len(deck)):
                                                if card6_index not in indicies_of_cards_in_play:
                                                    indicies_of_cards_in_play.add(card6_index)


                                                    if indicies_of_cards_in_play not in hands_seen:

                                                        hand = [deck[card1_index],deck[card2_index],deck[card3_index],deck[card4_index],deck[card5_index],deck[card6_index]]
                                                        cut_card = deck[cut_card_index]
                                                        # print(cut_card, hand)
                                                        # print(len(hands_seen))
                                                        score = scoreHand(hand, cut_card)

                                                        if score == highest_score:
                                                            highest_scoring_hands.append(frozenset(hand + [cut_card]))

                                                        if score > highest_score:
                                                            highest_score = score
                                                            highest_scoring_hands = [frozenset(hand + [cut_card])]


                                                        all_scores.append(score)

                                                        hands_seen.add(frozenset(indicies_of_cards_in_play))


                                                    indicies_of_cards_in_play.remove(card6_index)

                                            indicies_of_cards_in_play.remove(card5_index)

                                    indicies_of_cards_in_play.remove(card4_index)

                            indicies_of_cards_in_play.remove(card3_index)

                    indicies_of_cards_in_play.remove(card2_index)

            indicies_of_cards_in_play.remove(card1_index)

    indicies_of_cards_in_play.remove(cut_card_index)
    print("new cut card")
    print(cut_card)
    
print(max(all_scores))
print()