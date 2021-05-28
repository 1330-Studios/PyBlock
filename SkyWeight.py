# skills
mining = int(input("Whats your mining level?: "))
foraging = int(input("Whats your foraging level?: "))
enchanting = int(input("Whats your enchanting level?: "))
farming = int(input("Whats your farming level?: "))
combat = int(input("Whats your combat level?: "))
fishing = int(input("Whats your fishing level?: "))
alchemy = int(input("Whats your alchemy level?: "))
taming = int(input("Whats your taming level?: "))
# slayers
zombie = int(input("Whats your Revenant Horror level?: "))
spider = int(input("Whats your Tarantula Broodfather level?: "))
wolf = int(input("Whats your Sven Packmaster level?: "))
# dungeons
d_level = int(input("Whats your catacombs level?: "))
# misc
fairySouls = int(input("How many fairy souls do you have?: "))

weight = 0

# calc

weight += mining*1.33 + foraging*2.35 + enchanting*1.25 + farming*2.03 + combat*3.03 + fishing*3.9 + alchemy*1.4 + taming*1.1
weight += (zombie+spider+wolf)*3.5

for level in range(d_level):
    weight += level/50

weight += (fairySouls/227)*10.2

print(f'Your account weight is: {round(weight*100)/100}')

# My account's weight is 558.66
# My friend's account's weight is 487.33
# Refraction's account's weight is 925.08
# Thouqhtz's account's weight is 967.55
