#!/usr/bin/python3
"""
    The AirBnB Console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ A simple commandline interpreter for the console """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """ Exits the console """
        return True

    def do_EOF(self, line):
        """ Exits the console """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
