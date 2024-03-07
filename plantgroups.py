#better scoring system: find distance from plant to every other plant and scale score/deduction based on distance from plant
#better swapping system: instead of generating a random new grid layout, have plants with the worst score swap places - or maybe find optimal order for each row and column as is, then swap whole rows and columns?

import random

class Plant:
    def __init__(self, name, friends, enemies):
        self.name = name
        self.friends = friends
        self.enemies = enemies
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self):
        return str(self)


def randomly_populate_grid(dimensions, plants):
    # area (product of dimensions, e.g., 4x3=12) must equal number of elements in plants
    grid = []
    for i in range(dimensions[0]):
        row = []
        for j in range(dimensions[1]):
            selected_plant = random.choice(plants)
            row.append(selected_plant)
            plants.remove(selected_plant)
        grid.append(row)
    return grid

def get_neighbors(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y),(x+1,y-1)]

def score_grid(grid):
    score = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            current_plant = grid[x][y]
            neighbors = get_neighbors((x,y))
            for neighbor in neighbors:
                try:
                    neighbor_plant = grid[neighbor[0]][neighbor[1]]
                    if neighbor_plant.name.lower().replace(" ","") in current_plant.friends:
                        score += 1
                    if neighbor_plant.name.lower().replace(" ","") in current_plant.enemies:
                        score -= 1
                except:
                    pass
    return score

def print_grid(grid):
    for x in grid:
        for y in x:
            print('{0:<16}'.format(y.name), end='')
        print()

# make sure checks for friends and enemies are spelled correctly and are normalized 

cucumbers = Plant('cucumbers', ['cucumbers','bellpeppers', 'bananapeppers', 'beans', 'broccoli', 'cabbage', 'carrots', 'catnip', 'chives', 'corn', 'dill', 'eggplant', 'garlic', 'onions', 'parsnips', 'sunflowers', 'tomatoes'], ['basil', 'potatoes', 'rosemary', 'sage', 'watermelon', 'zinnia'])
eggplant = Plant('eggplant', ['eggplant','basil', 'beans', 'bellpeppers', 'bananapeppers', 'cucumbers', 'marjoram', 'potatoes', 'peas', 'spinach', 'tomatoes'], ['corn', 'fennel', 'onions'])
rhubarb = Plant('rhubarb', ['rhubarb','bellpeppers', 'bananapeppers', 'broccoli', 'cabbage', 'catnip', 'chives', 'garlic', 'lavender', 'marjoram', 'onions', 'rosemary', 'sage', 'sunflowers', 'thyme'], ['beans', 'peas'])
broccoli = Plant('broccoli', ['broccoli','beans', 'carrots', 'catnip', 'celery', 'cucumbers', 'dill', 'lavender', 'marjoram', 'mint', 'onions', 'potatoes', 'rhubarb', 'rosemary', 'sage', 'watermelon'], ['bellpeppers', 'basil', 'cabbage', 'fennel', 'tomatoes'])
cabbage = Plant('cabbage', ['cabbage','beans', 'carrots', 'celery', 'chamomile', 'corn', 'cucumbers', 'dill', 'garlic', 'lavender', 'marjoram', 'onions', 'parsnips', 'peas', 'potatoes', 'rhubarb', 'rosemary', 'sage', 'spinach', 'sunflowers', 'thyme'], ['bellpeppers', 'bananapeppers', 'basil', 'broccoli', 'tomatoes'])
lemongrass = Plant('lemongrass', ['lemongrass','bellpeppers', 'bananapeppers','basil', 'hops', 'sage', 'thyme', 'tomatoes'], ['zinnia'])
sunflowers = Plant('sunflowers', ['sunflowers','squash', 'beans', 'cabbage', 'corn', 'cucumbers', 'marjoram', 'rhubarb', 'watermelon'], ['potatoes', 'zinnia'])
bellPeppers = Plant('bellpeppers', ['bellpeppers','squash', 'basil', 'carrots', 'cucumbers', 'eggplant', 'garlic', 'marjoram', 'onions', 'parsnips', 'rhubarb', 'spinach', 'tomatoes'], ['bananapeppers', 'beans', 'cabbage', 'fennel', 'potatoes'])
dill = Plant('dill', ['dill','broccoli', 'cabbage', 'corn', 'cucumber', 'hops', 'marjoram', 'onions', 'spinach', 'squash', 'sweetpotatoes', 'watermelon'], ['carrots', 'fennel', 'parsnips'])
bananaPeppers = Plant('bananapeppers', ['bananapeppers','squash', 'basil', 'carrots', 'cucumbers', 'eggplant', 'garlic', 'marjoram', 'onions', 'parsnips', 'rhubarb', 'spinach'], ['beans', 'bellpeppers', 'broccoli', 'cabbage', 'fennel', 'potatoes'])
watermelon = Plant('watermelon', ['watermelon','squash', 'basil', 'broccoli', 'catnip', 'chives', 'corn', 'dill', 'garlic', 'hops', 'marjoram', 'onions', 'parsnips', 'peas', 'sage', 'sunflowers', 'tomatoes'], ['cucumbers', 'potatoes'])
celery = Plant('celery', ['celery','beans', 'broccoli', 'cabbage', 'marjoram', 'onions', 'peas', 'spinach', 'tomatoes'], ['carrots', 'parsnips', 'potatoes'])
basil = Plant('basil', ['basil', 'bellpeppers', 'bananapeppers', 'carrots', 'catnip', 'eggplant', 'garlic', 'hops', 'hotpeppers', 'lemongrass', 'marjoram', 'parsnips', 'potatoes', 'watermelon'], ['broccoli', 'cabbage', 'cucumbers'])
spinach = Plant('spinach', ['spinach','bellpeppers', 'bananapeppers', 'beans', 'cabbage', 'carrots', 'celery', 'corn', 'dill', 'eggplant', 'garlic', 'marjoram', 'onions', 'peas', 'squash', 'tomatoes'], ['fennel', 'potatoes'])
garlic = Plant('garlic', ['garlic','bellpeppers', 'bananapeppers', 'basil', 'cabbage', 'cucumbers', 'hops', 'marjoram', 'parsnips', 'potatoes', 'rhubarb', 'spinach', 'tomatoes', 'watermelon'], ['beans', 'onions', 'peas', 'sage'])
all_plants = [cucumbers, cucumbers, rhubarb, rhubarb, eggplant, eggplant, sunflowers, lemongrass, sunflowers, sunflowers, garlic, broccoli, broccoli, spinach, spinach, basil, basil, basil, dill, dill, dill, watermelon, watermelon, celery, bellPeppers, bellPeppers, cabbage, bananaPeppers] 


grid = randomly_populate_grid((4,7),all_plants)
print_grid(grid)
print(score_grid(grid))

best_grid = grid
for i in range(10000000):
    all_plants = [cucumbers, cucumbers, rhubarb, rhubarb, eggplant, eggplant, sunflowers, lemongrass, sunflowers, sunflowers, garlic, broccoli, broccoli, spinach, spinach, basil, basil, basil, dill, dill, dill, watermelon, watermelon, celery, bellPeppers, bellPeppers, cabbage, bananaPeppers] 
    new_grid = randomly_populate_grid((4,7),all_plants)
    if score_grid(new_grid) > score_grid(best_grid):
        best_grid = new_grid

print_grid(best_grid)
print(score_grid(best_grid))
