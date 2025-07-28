Describe and explain how you used a range of OOP principles in your project. For each principle, include a very small code snippet that highlights the principle.
- Classes
- Constructors
- Methods
- Objects
- Inheritance
- Polymorphism
- Generalisation


# My Response
In my code, I used a range of OOP principles in my project. 
The OPP principle of classes was used to as a blueprint for creating my objects. The class I used as a base class was called "farmAnimal" to repersent the animals. This is shown here in my code.
    class farmAnimal:
    .....
I also have two other classes called "AnimalForProduction" and "DomesticAnimal" which uses the OOP principle of inheritance to use the features made in the base class "farmAnimal".
    class AnimalForProduction(farmAnimal): 
    .....
Within the base class "farmAnimal", I used a constructor in my code with the __init__ method to initialises animal attributes.
    def __init__(self, animal, legs, sound):
        self.animal = animal
In this same base class, I used the method feed() to feed the animlal.
    def feed(self): #-> Method
            self.fatPoints += 1
            print(f"{self.animal} has been fed. Fat Points: {self.fatPoints}")
            print("")
Each animal has a beginning fatPoint of 1, so this adds 1 fatPoint when the animal is being fed.
Objects where also used as part of instances of a class. I created the objects for each animal depending on what they are.
    cow = AnimalForProduction("Cow", 4, "Moo")
    dog = DomesticAnimal("Dog", 4, "Bark!")
With all these different classes, polymorphism used the same method name with different behaviour. This was seen with both animal types having their own feed() method.
    cow.feed()
    dog.feed()