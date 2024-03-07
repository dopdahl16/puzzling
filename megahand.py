# from itertools import combinations

# def score_hand(hand):
#     """
#     Function to score a hand in cribbage.
#     """
#     scores = 0
#     pairs = 0
#     hand.sort()  # Sort the hand to make it easier to find runs and pairs

#     # Find pairs
#     for i in range(len(hand) - 1):
#         if hand[i] == hand[i + 1]:
#             pairs += 1
#             scores += 2

#     # Find runs
#     for r in range(3, 6):  # Runs can be of length 3, 4, or 5
#         for combo in combinations(hand, r):
#             if len(set(combo)) == r:  # If all cards are distinct
#                 scores += r

#     # Find 15s
#     for r in range(2, 6):
#         for combo in combinations(hand, r):
#             if sum(combo) == 15:
#                 scores += 2

#     # Find flushes (assuming all cards are of the same suit)
#     if len(set([card[1] for card in hand])) == 1:
#         scores += len(hand)

#     # Add points for His Nobs
#     for card in hand:
#         if card[0] == 'J' and card[1] == 'H':
#             scores += 1

#     return scores

# def max_cribbage_score(hand):
#     """
#     Function to calculate the maximum points possible in a round of cribbage for a given hand.
#     """
#     max_score = 0
#     for combo in combinations(hand, 4):
#         crib_hand = [card for card in hand if card not in combo]
#         score = score_hand(list(combo)) + score_hand(crib_hand)
#         max_score = max(max_score, score)
#     return max_score

# # Example usage
# hand = [('5', 'H'), ('5', 'C'), ('5', 'D'), ('J', 'H'), ('Q', 'S')]  # Example hand
# print("Maximum points possible:", max_cribbage_score(hand))



def score_hand(hand):
    """
    Function to score a hand in cribbage.
    """
    scores = 0
    pairs = 0
    hand.sort()  # Sort the hand to make it easier to find runs and pairs

    # Find pairs
    for i in range(len(hand) - 1):
        if hand[i] == hand[i + 1]:
            pairs += 1
            scores += 2

    # Find runs
    for i in range(len(hand) - 2):
        for j in range(i + 2, len(hand)):
            if all(hand[x] == hand[x - 1] + 1 for x in range(i + 1, j)):
                scores += j - i

    # Find 15s
    for i in range(1, 1 << len(hand)):
        if sum(hand[j] for j in range(len(hand)) if i & (1 << j)) == 15:
            scores += 2

    # Find flushes (assuming all cards are of the same suit)
    if len(set([card[1] for card in hand])) == 1:
        scores += len(hand)

    # Add points for His Nobs
    for card in hand:
        if card[0] == 'J' and card[1] == 'H':
            scores += 1

    return scores

def max_cribbage_score(hand):
    """
    Function to calculate the maximum points possible in a round of cribbage for a given hand.
    """
    max_score = 0
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                for l in range(k + 1, len(hand)):
                    crib_hand = [card for idx, card in enumerate(hand) if idx != i and idx != j and idx != k and idx != l]
                    score = score_hand([hand[i], hand[j], hand[k], hand[l]]) + score_hand(crib_hand)
                    max_score = max(max_score, score)
    return max_score

# Example usage
hand = [('5', 'H'), ('5', 'C'), ('5', 'D'), ('J', 'H'), ('Q', 'S')]  # Example hand
print("Maximum points possible:", max_cribbage_score(hand))
