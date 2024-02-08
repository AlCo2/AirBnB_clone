#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    the command processor
    """

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

    def emptyline(line):
        """
        if the line is empty, do nothing
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
