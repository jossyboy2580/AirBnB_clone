#!/usr/bin/python3

"""
This module contains the entry point of the command
intepreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A command intepreter for the aurbnb console
    """
    quote = "(hbnb)"
    my_classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return (True)

    def help_quit(self):
        """
        Quit command to exit the program
        """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """
        Ctrl_D triggers a program exit
        """
        return (True)

    def do_create(self, line):
        """
        Create command to create an instance of an object
        """

        if not line:
            print("** class name missing **")
            pass
        elif not line in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            pass
        else:
            obj = HBNBCommand.my_classes[line]()
            obj.save()
            print(obj.id)

    def help_create(self):
        """
        Help statement for the create command
        """
        print("Create command to create a BaseModel object")

    def do_show(self, line):
        """
        Show command to display an object
        """
        if not line:
            print("** class name missing **")
            pass
        obj = line.split()
        if not obj[0] in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            pass
        if len(obj) < 2:
            print("** instance id missing **")
            pass

        my_storage_objects = storage.all()
        try:
            my_obj = my_storage_objects["{}.{}".format(obj[0], obj[1])]
        except KeyError:
            print("** no instance found **")
            pass
        else:
            # my_obj_model = BaseModel(my_obj)
            print(my_obj)

    def do_destroy(self, line):
        """
        Destroy command to remove an object from storage
        """
        if not line:
            print("** class name missing **")
            pass
        obj = line.split()
        if not obj[0] in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            pass
        if len(obj) < 2:
            print("** instance id missing **")
            pass

        my_storage_objects = storage.all()
        try:
            my_obj = my_storage_objects["{}.{}".format(obj[0], obj[1])]
        except KeyError:
            print("** no instance found **")
            pass
        else:
            # my_obj_model = BaseModel(my_obj)
            print(my_obj)
    def help_show(self):
        """
        Help statement for the show command
        """
        print("This command prints an object by Classname and id")
        print("Usage: show <Model> <id>")

    def emptyline(self):
        """
        Do nothing
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
