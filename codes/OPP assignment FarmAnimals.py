class farmAnimal:
    def __init__(self, animal, legs, sound): #-> Constructor
        self.animal = animal
        self.eyes = 2
        self.legs = legs
        self.sound = sound
        self.fatPoints = 1

    def introduce(self): 
        #introducing themselves
        print(f"I am a {self.animal} and have {self.legs} legs.")
        #e.g => cow.introduce()

    def greet(self, farmAnimal):
        if farmAnimal.animal != self.animal:
            # greeting another animal
            print(f"Hello {farmAnimal.animal}. I am a {self.animal}.")
            #e.g => cow.greet(dog)
        else:
            # animal greets another animal of its species. e.g cow greeting cow
            print(f"Hello fellow {self.animal}!")

    def animalSound(self):
        return self.sound
        # e.g => cow.animalSound()

    def feed(self): #-> Method
        self.fatPoints += 1
        print(f"{self.animal} has been fed. Fat Points: {self.fatPoints}")
        print("")


class AnimalForProduction(farmAnimal):
    def __init__(self, animal, legs, sound):
        super().__init__(animal, legs, sound)
        self.alive = True

    def feed(self):
        if not self.alive:
            print(f"{self.animal} is already butchered.")
            print("")
            return

        super().feed()
        if self.fatPoints >= 10:
            print(f"{self.animal} is fat enough and will be butchered.")
            print("")
            self.butcher()

    def butcher(self):
        self.alive = False
        print(f"{self.animal} has been butchered.")
        print("")



class DomesticAnimal(farmAnimal):
    def feed(self):
        if self.fatPoints >= 10:
            print(f"{self.animal} is too fat! Stop feeding it.")
            print("")
        else:
            super().feed()


# Production animals
cow = AnimalForProduction("Cow", 4, "Moo")
pig = AnimalForProduction("Pig", 4, "Oink!")
sheep = AnimalForProduction("Sheep", 4, "BAAAaa")
chicken = AnimalForProduction("Chicken", 2, "Bawk BAWK!")

# Domestic animals
dog = DomesticAnimal("Dog", 4, "Bark!")
cat = DomesticAnimal("Cat", 4, "Meow")
horse = DomesticAnimal("Horse", 4, "Neigh")
bird = DomesticAnimal("Bird", 2, "Tweet")

# Dictionary to look up animals by name
animal_farm = {
    "cow": cow,
    "pig": pig,
    "sheep": sheep,
    "chicken": chicken,
    "dog": dog,
    "cat": cat,
    "horse": horse,
    "bird": bird
}

# MAIN LOOP
choice = ""
while choice != "exit":
    print("Animals on the farm:", ", ".join(animal_farm.keys()))
    choice = input("What animal do you want to feed? (or type 'exit' to quit): ").lower()
    print("")

    if choice == "exit":
        print("Exiting farm... Goodbye!")
    elif choice in animal_farm:
        animal_farm[choice].feed()
    else:
        print("That animal is not on the farm.")
        print("")
        