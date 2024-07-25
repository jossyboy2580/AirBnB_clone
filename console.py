#!/usr/bin/python3

"""
This module contains the entry point of the command
intepreter
"""
import json
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A command intepreter for the aurbnb console
    """
    prompt = "(hbnb) "
    my_classes = {"BaseModel": BaseModel, "User": User,
                  "City": City, "Place": Place,
                  "State": State, "Amenity": Amenity,
                  "Review": Review}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return (True)

    def do_EOF(self, line):
        """
        EOF (Ctrl+D) signal to exit the program.
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
            key = obj[0] + "." + obj[1]
            del storage.__class__._FileStorage__objects[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, line):
        """
        Show command to display all objects
        """
        storage.reload()
        all_objs = storage.all()
        cls_dict = HBNBCommand.my_classes
        if not line:
            for key, obj in all_objs.items():
                print(obj)
        else:
            if line in cls_dict:
                for key, obj in all_objs.items():
                    cls_nm = key.split(".")[0]
                    if line == cls_nm:
                        print(obj)
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """
        count command to display count objects
        of a certaim class
        """
        all_objs = storage.all()
        cls_dict = HBNBCommand.my_classes
        count = 0
        if line:
            if line not in HBNBCommand.my_classes:
                print("** class doesn't exist **")
            else:
                for key, obj in all_objs.items():
                    obj_cls, obj_id = key.split(".")
                    if obj_cls == line:
                        count += 1
            print(count)

    def do_update(self, line):
        """
        Update command to update an attribute of our instance
        """

        cls_dict = HBNBCommand.my_classes
        immutable_attrib = ["created_at", "id", "updated_at"]

        if not line:
            print("** class name missing **")
            return
        args = line.split(maxsplit=3)
        if args[0] not in cls_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
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
                obj.__setattr__(args[2], args[3])
                obj.save()

    def emptyline(self):
        """
        What happens when a user executes an empty line
        """
        pass

    def default(self, line):
        """
        Handle inputs of type
        User <id> {attributes list}
        """
        valid_commands = {"show": self.do_show, 'update': self.do_update,
                          'destroy': self.do_destroy, 'count': self.do_count,
                          'all': self.do_all}
        #  Extract the class name
        cls_name, remaining = line.split('.', maxsplit=1)
        if cls_name not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        command, remaining = remaining.split('(', maxsplit=1)
        if not command in valid_commands:
            print("** invalid command **")
            return
        if command in ('count', 'all'):
            valid_commands[command](cls_name)
            return
        remaining = remaining[:-1]
        if command in ('show', 'destroy'):
            valid_commands[command](f'{cls_name} {eval(remaining)}')
            return
        cls_id, remaining = remaining.split(', ', maxsplit=1)
        if '{' in remaining:
            attrs = eval(remaining)
            for key, val in attrs.items():
                argz = f'{cls_name} {eval(cls_id)} {key} {val}'
                self.do_update(argz)
        else:
            try:
                attr, val = remaining.split(', ')
            except Exception as exc:
                return
            else:
                argz = f'{cls_name} {eval(cls_id)} {attr} {val}'
                self.do_update(argz)

    # Help methods for all the commands

    def help_quit(self):
        """
        Quit command to exit the program.
        """
        print("Quit command to exit the program.")

    def help_EOF(self):
        """
        Help for EOF
        """
        print("EOF (Ctrl+D) signal to exit the program.")

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
