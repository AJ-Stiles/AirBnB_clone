#!/usr/bin/python3
"""
Console module: Defines the HBNBCommand class for the command interpreter.
"""

import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class implements the command interpreter.
    """

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, User, State, City, Amenity, Place, or Review,
        saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

        if arg not in classes:
            print("** class doesn't exist **")
            return

        try:
            cls = eval(arg)  # Convert class name to class reference
            instance = cls()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            del objs[key]
            models.storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all or all <class name>
        """
        objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif arg in models.CLASSES:
            print([str(obj) for key, obj in objs.items() if key.split('.')[0] == arg])
        else:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        objs = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs:
            obj = objs[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

