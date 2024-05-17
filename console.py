#!/usr/bin/python3

"""
This module contains the entry point of the command
intepreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A command intepreter for the aurbnb console
    """
    quote = "(hbnb)"

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

    def emptyline(self):
        """
        Do nothing
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
