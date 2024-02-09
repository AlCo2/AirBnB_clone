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
    storage_list = models.storage.all()

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
            Usage: create <object id>
        """
        if line:
            try:
                model = eval(f"{line}")()
                model.save()
                print(model.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id
            Usage: show <object id>
        """
        if line:
            result = line.split()
            if result[0] in self.class_list:
                if len(result) > 1:
                    class_key = result[0] + '.' + result[1]
                    if class_key in self.storage_list:
                        print(self.storage_list[class_key])
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
            Usage: destroy <object id>
        """
        if line:
            result = line.split()
            if result[0] in self.class_list:
                if len(result) > 1:
                    class_key = result[0] + '.' + result[1]
                    if class_key in self.storage_list:
                        del self.storage_list[class_key]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
            Displays all instance of a class
            Usage: all <optional: class>
        """
        if line:
            if line not in self.class_list:
                print("** class doesn't exist **")
                return
        str_all = "["
        for i, obj in enumerate(self.storage_list.values()):
            str_all += '"' + str(obj) + '"'
            if (i != len(self.storage_list) - 1):
                str_all += ', '
        str_all += "]"
        print(str_all)

    def do_update(self, line):
        """
            Adds & Updates special attributes to an instance
            Usage: update <class> <id> <attribute> <value>
        """
        if line:
            command = line.split()
            n_cmd = len(command)

            if command[0] in self.class_list:

                if n_cmd < 2:
                    print("** instance id missing **")
                    return
                elif n_cmd < 3:
                    print("** attribute name missing **")
                    return
                elif n_cmd < 4:
                    print("** value missing **")
                    return

                obj_id = command[0] + '.' + command[1]
                if obj_id in self.storage_list:
                    obj = self.storage_list[obj_id]
                    setattr(obj, f'{command[2]}', eval(command[3]))
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
