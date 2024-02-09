#!/usr/bin/python3
"""
    The AirBnB Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A simple commandline interpreter for the console """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        quit: stop the program from running
        """
        return True

    def do_EOF(self, line):
        """
        EOF: make the program stop
        """
        return True

    def emptyline(self):
        """
        if the line is empty, do nothing
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
