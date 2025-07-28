Include the following in this file or folder:
- DFD – draw a DFD showing the designed external entities, internal processes, methods or
algorithms and data stores as well as any data flowing between them

- Structure chart – draw a structure chart showing the hierarchical plan of subprograms and
methods including data passed between them, loops and decisions

- Data dictionary – show a table of planned variables each with their data types, format,
description, validation and example value

| Variable Name | Data Type | Description                                      | Example Value      | Validation/Allowed Values         |
|---------------|-----------|--------------------------------------------------|--------------------|-----------------------------------|
| animal        | String    | Name/type of the animal                          | "Cow"              | Any string                        |
| eyes          | Integer   | Number of eyes (default 2)                       | 2                  | >= 0                              |
| legs          | Integer   | Number of legs                                   | 4                  | >= 0                              |
| sound         | String    | Sound the animal makes                           | "Moo"              | Any string                        |
| fatPoints     | Integer   | Tracks how much the animal has been fed          | 1                  | >= 1                              |
| alive         | Boolean   | If the animal is alive (production animals only) | True               | True or False                     |
| animal_farm   | Dict      | Dictionary of animal objects by name             | {"cow": cow, ...}  | Keys: animal names; Values: objects|
| choice        | String    | User input for animal selection or "exit"        | "pig"              | Animal name or "exit"             |

- Pseudocode – communicate a planned algorithm or method using pseudocode


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


