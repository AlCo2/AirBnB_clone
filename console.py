#!/usr/bin/python3
"""
    The AirBnB Console
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ A simple commandline interpreter for the console """

    prompt = "(hbnb) "

    class_list = ["BaseModel"]

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

    def do_create(self, line):
        """
        Creates a new instance of a class
        """
        if line:
            try:
                model = eval(f"{line}")()
                model.save()
                print(model.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if line:
            result = line.split()
            if result[0] in self.class_list:
                if len(result) > 1:
                    storage_list = models.storage.all()
                    class_key = result[0] + '.' + result[1]
                    if class_key in storage_list:
                        print(storage_list[class_key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        if line:
            result = line.split()
            if result[0] in self.class_list:
                if len(result) > 1:
                    storage_list = models.storage.all()
                    class_key = result[0] + '.' + result[1]
                    if class_key in storage_list:
                        del storage_list[class_key]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
