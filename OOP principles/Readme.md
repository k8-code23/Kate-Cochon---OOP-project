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
The OPP principle of Classes was used to as a blueprint for creating my objects. The class I used as a base class was called "farmAnimal" to repersent the animals. This is shown here in my code.
    class farmAnimal:
    .....
I also have two other classes called "AnimalForProduction" and "DomesticAnimal" which uses the OOP principle of inheritance to inherit the features made in the base class "farmAnimal".
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
With all these different classes, polymorphism was used with the same method name with different behaviour. This was seen with both animal types(AnimalForProduction and DomesticAnimal) having their own feed() method.
    cow.feed()
    dog.feed()
When feed is called, it uses the base class to feed the animal as well as the feed method for that animal depending on which class it is from. For example, when feeding a dog, this object is part of the DomesticAnimal class, so it relies on the feed method for this class produces a message of (f"{self.animal} is too fat! Stop feeding it.") when the fatPoints for the DomesticAnimal reaches 10. For the AnimalForProduction, it gives the message print(f"{self.animal} is fat enough and will be butchered.") where it will then go to the butcher() method and make the self.alive==false.

Finally, Generalisation has been used as I created a general base class called farmAnimal that has contained shared attributes and methods for all animals. This class is used to act as a template for other specific animal types such as the AnimalsForProduction(cow, pig, sheep, etc) and DomesticAnimal(dog, cat, bird). This base class defines common features like animal, legs, sound, and methods such as feed(), introduce() and greet().