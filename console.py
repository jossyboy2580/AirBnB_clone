#!/usr/bin/python3

"""
This module contains the entry point of the command
intepreter
"""
import json
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
            return
        obj = line.split()
        if not obj[0] in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        if len(obj) < 2:
            print("** instance id missing **")
            return

        my_storage_objects = storage.all()
        try:
            my_obj = my_storage_objects["{}.{}".format(obj[0], obj[1])]
        except KeyError:
            print("** no instance found **")
            return
        else:
            # my_obj_model = BaseModel(my_obj)
            print(my_obj)

    def do_destroy(self, line):
        """
        Destroy command to remove an object from storage
        """
        if not line:
            print("** class name missing **")
            return
        obj = line.split()
        if not obj[0] in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        if len(obj) < 2:
            print("** instance id missing **")
            return

        my_storage_objects = storage.all()
        try:
            del my_storage_objects["{}.{}".format(obj[0], obj[1])]
        except KeyError:
            print("** no instance found **")
            return
        else:
            with open(storage.file_path, 'w', encoding="utf-8") as fp:
                json.dump(my_storage_objects, fp)

    def do_all(self, line):
        """
        Show command to display all objects
        """
        if not line:
            try:
                with open(storage.file_path, 'r', encoding="utf-8") as fp:
                    objs_dict = json.load(fp)
                    for key in objs_dict:
                        obj = objs_dict[key]
                        obj_model = HBNBCommand.my_classes[obj["__class__"]](**obj)
                        print(obj_model)
            except FileNotFoundError:
                return
        elif line and line not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            try:
                with open(storage.file_path, 'r', encoding="utf-8") as fp:
                    objs_dict = json.load(fp)
                    for key, value in objs_dict.items():
                        if value["__class__"] == line:
                            obj_model = HBNBCommand.my_classes[value["__class__"]](**value)
                            print(obj_model)
            except FileNotFoundError:
                return

    def help_show(self):
        """
        Help statement for the show command
        """
        print("This command prints an object by Classname and id")
        print("Usage: show <Model> <id>")

    def help_destroy(self):
        """
        Help statement for the destroy command
        """
        print("This command destroys an object by Classname and id")
        print("Usage: destroy <Model> <id>")

    def help_all(self):
        """
        Helpt for the all command
        """
        print("This command displays objects from a storage")
        print("Usage: all")
        print("or")
        print("Usage: all ModelName")

    def emptyline(self):
        """
        Do nothing
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
