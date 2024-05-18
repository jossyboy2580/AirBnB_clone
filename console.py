#!/usr/bin/python3

"""
This module contains the entry point of the command
intepreter
"""
import json
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A command intepreter for the aurbnb console
    """
    quote = "(hbnb)"
    my_classes = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return (True)

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
        elif line not in HBNBCommand.my_classes:
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
        if obj[0] not in HBNBCommand.my_classes:
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
        all_objs = storage.all()
        all_cls_dict = HBNBCommand.my_classes
        if not line:
            for key in all_objs:
                obj_cls, obj_id = key.split(".")
                obj = all_cls_dict[obj_cls](**all_objs[key])
                print(obj)
        elif line and line not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            args = ".".join(line.split())
            for key in all_objs:
                if key == args:
                    obj_cls, obj_id = key.split(".")
                    obj = all_cls_dict[obj_cls](**all_objs[key])

    def do_update(self, line):
        """
        Update command to update an attribute of our instance
        """

        cls_dict = HBNBCommand.my_classes
        immutable_attrib = ["created_at", "id", "updated_at"]

        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in cls_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        storage_dict = storage.all()
        try:
            obj = storage_dict[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return
        else:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            if args[2] in immutable_attrib:
                return
            else:
                obj[args[2]] = args[3]

    def emptyline(self):
        """
        What happens when a user executes an empty line
        """
        pass

    # Help methods for all the commands

    def help_quit(self):
        """
        Quit command to exit the program
        """
        print("Quit command to exit the program")

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
        Help for the all command
        """
        print("This command displays objects from a storage")
        print("Usage: all")
        print("or")
        print("Usage: all ModelName")

    def help_update(self):
        """
        Help for the update command
        """
        print("This command updates an attribute of an instance")
        print("Usage: update <class_name> <id> <attribute> <value>")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
