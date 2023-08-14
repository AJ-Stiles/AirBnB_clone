# AirBnB Clone - The Console

## Description

The "AirBnB clone - The console" project is a simplified version of the popular Airbnb platform. The project aims to build a command-line interface (CLI) that allows users to manage AirBnB objects, including users, properties, bookings, and more. The command interpreter interacts with the user, taking commands to create, update, delete, and view AirBnB objects.

## Command Interpreter

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:
``
git clone <repository_url>
cd AirBnBConsole
``

2. Ensure you have Python 3.8.5 or later installed on your system.

3. Run the command interpreter by executing the `console.py` script:

``./console.py``


### How to Use the Command Interpreter

The command interpreter has a prompt `(hbnb)` where you can enter various commands. The interpreter supports both interactive and non-interactive modes.

#### Interactive Mode:

In interactive mode, the command interpreter waits for user input at the prompt. You can enter commands and get immediate feedback. To exit the interpreter, use the `quit` command or press Ctrl + D.

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
EOF help quit
(hbnb) quit
$


#### Non-Interactive Mode:

In non-interactive mode, you can provide a list of commands in a file and pass it to the command interpreter using pipes. The interpreter will execute the commands one by one and exit when done.

$ cat commands.txt
help
quit
$ cat commands.txt | ./console.py
(hbnb) Documented commands (type help <topic>):
EOF help quit
(hbnb)


### Examples

Here are some examples of commands you can use with the command interpreter:

1. Creating a new User:
```(hbnb) create User```

2. Updating a User's attribute:
```(hbnb) update User <user_id> first_name "John"```

3. Showing information about a User:
```(hbnb) show User <user_id>```

4. Deleting a User:
```(hbnb) destroy User <user_id>```

5. Listing all Users:
```(hbnb) all User```

## Unit Tests

The project includes unit tests to ensure the functionality and correctness of the classes and command interpreter. To run the tests, use the following command:

```$ python3 -m unittest discover tests```
