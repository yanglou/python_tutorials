wizard = "Wizard"
elf = "Elf"
human = "Human"
fairy = "Fairy"

wizard_hp = 70
elf_hp = 100
human_hp = 150
fairy_hp = 40
my_hp = 0

wizard_damage = 150
elf_damage = 100
human_damage = 20
fairy_damage = 180
my_damage = 0

dragon_hp = 300
dragon_damage = 50
character = 'placeholder'

while character != '5' and character != 'exit':
    print("1)   Wizard")
    print("2)   Elf")
    print("3)   Human")
    print("4)   Fairy")
    print("5)   Exit")
    character = input("Choose your character: ").lower()

    while True:
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character == "4" or character == "fairy":
            character = fairy
            my_hp = fairy_hp
            my_damage = fairy_damage
            break
        if character == "5" or character == "exit":
            break
        print("Unkown character")
        break
    if character == "5" or character == "exit":
        break

    print(character)
    print("HP: " + str(my_hp))
    print("Attack: " + str(my_damage))

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The ", character, "damaged the Dragon!")
        print("Dragon HP: ", dragon_hp)
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at ", character)
        print(character, " HP: ", my_hp)
        if my_hp <= 0:
            print(character, " has lost the battle.")

            break
    character = 'exit'
