games = ["Dark Souls Franchise", "The Elder Scrolls V: Skyrim", 
"Half-Life Franchise", "Papers, Please"]

print(games[-1])

print(games[2:4])

some_numbers = [5, 1, 52, 74, 55, 9]

games.extend(some_numbers)

print(games)

# add an item to the list
games.append("Infectonator")

# add a item to a specific index on the list, without remove the item on index
games.insert(1, "Welcome to the game")
games.insert(4, "Welcome to the game")

some_numbers.sort()

games.reverse()

print(str(games) + "\n" + str(some_numbers))

games2 = games.copy()


games.remove(1)

# pop remove the last item of the list
games.pop()

games.clear()

