Describe and explain how you used a range of good programming practices in your project. Label each practice used and include a screenshot or code snippet that clearly shows its use related to your description and explanation.
- clear and uncluttered mainline
- one logical task per subroutine
- use of stubs
- use of control structures and data structures
- ease of maintenance
- version control
- regular backup


# My response
The program has a clear and uncluttered mainline that loops the program making it easy and simple to follow. This is because it prints the animals from the farm_animal dictionary, gets the user input, and calls the appropriate method. This is seen in this snippet of the code:

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
Each method does one thing, such as feeding an animal or introducing or greeting it, showing that there is a logical task for the subroutine.

    def feed(self):
        self.fatPoints += 1
        print(f"{self.animal} has been fed. Fat Points: {self.fatPoints}")
        print("")
When I was originally planning my code, I did use stubs for the classes I wasn't sure how do program yet. This was seen with the method of "pass". This helped me still work on the code without there being an error message.

    class farmAnimal:
        pass
The code also consisted of loops, if/else statements, and a dictionary to help manage aninals:

    animal_farm = {
        "cow": cow,
        "pig": pig,
        ...
    }
The ease of maintenance is seen as I have organised my code into classes and methods. This allows it to be easier to update or add new animal types without changing the main loop.

My version control I used was originally thonny to create the code, however I have moved it to Github for the assignment.

Regular backup within my files for thonny as well as in guithub has allowed the code to be saved well and consistently.

Overall,
I have done my best to use good programming practices so that my work is easy for me to understnad and work on.



