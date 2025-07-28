Include the following in this file or folder:
- DFD – draw a DFD showing the designed external entities, internal processes, methods or
algorithms and data stores as well as any data flowing between them

- Structure chart – draw a structure chart showing the hierarchical plan of subprograms and
methods including data passed between them, loops and decisions

- Data dictionary – show a table of planned variables each with their data types, format,
description, validation and example value

- Pseudocode – communicate a planned algorithm or method using pseudocode



BEGIN
Create all animal objects(cow,pig,sheep,chicken,dog,cat,horse,bird)
Add all animal objects to a dictionary called animal_farm
choice=""
WHILE choice is not "exit"
    Display all animal names in animal_farm
    Ask user which animal to feed (or type 'exit' to quit)
    Get user input and convert to lowercase

    If user input is "exit"
        Print exit message
    ELSE IF user input is in animal_farm
        call the feed() method for the chosen
    ELSE
        Print "That animal is not on the farm"
END

METHOD feed()
    Increase fatPoints by 1
    Print animal fed message

METHOD introduce()
    Print animal introduction

METHOD greet(other_animal)
    IF other_animal is not the same species
        Print greeting to other animal
    ELSE
        Print greeting to same species

- Flowchart – draw a flowchart of a planned algorithm or method



- Desk check – show a table of changing values that you used to desk check an algorithm or
method

- Test data – show a table of test data used to test an algorithm or method, each with its
reason for inclusion for an algorithm or method

| Test Case | Input(s)                | Expected Output(s)                                      |
|-----------|-------------------------|---------------------------------------------------------|
| TC1       | dog                     | dog has been fed. Fat Points: 2                         |
| TC2       | cow (10 times)          | cow is fat enough and will be butchered.Pig has been butchered. |
| TC3       | bird (10 times)         | bird is too fat! Stop feeding it.                       |
| TC4       | Koala                   | That animal is not on the farm.                         |
| TC5       | exit                    | Exiting farm... Goodbye!                                |

- Class diagram – show the planned class and inheritance hierarchy with attributes and
methods for all classes

