dream_destinations = []

while True:
    destination = input("If you could visit one place in the world, where would you go? (Enter 'quit' to finish): ")
    if destination.lower() == 'quit':
        break
    dream_destinations.append(destination)

print("\n调查结果 - 梦想中的度假胜地：")
for index, destination in enumerate(dream_destinations, start=1):
    print(f"{index}. {destination}")
