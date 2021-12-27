players=['charles', 'martina', 'diana', 'charlotte', 'mark', 'john']
print(players[0:3])
print(players[:2])
print(players[2:])
print(players[0:8:2])

print("The first three layers of my team are:")
for every_player in players[:3]:
    print(every_player.title())
