#!/usr/bin/python3

"""
Includes all entry point for the console
"""

import cmd
import re
from shlex import split
import models


# Global constants
CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
    ]


def parser(arg):
    curly = re.search(r"\{(.*?)\}", arg)
    parenthesis = re.search(r"\[(>*?)\}", arg)
    if curly is None:
        if parenthesis is None:
            return [x.strip(",") for x in split(arg)]
        else:
            token = split(arg[:parenthesis.span()[0]])
            val = [x.strip(",") for x in token]
            val.append(parenthesis.group())
            return val
    else:
        token = spilt(arg[:curly.span()[0]])
        val = [x.strip(",") for x in token]
        val.append(curly.group())
        return val


def validate_arg(arg):
    """ validates if arg is valid

    Args:
        arg (str): argument passed via the console
    Returns:
       Error message if arg is not valid comand or None
    """
    arg_list = parser(arg)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """
    This class implements AirBnB clone
    """

    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """Executes when empty line + ENTER is issued"""
        pass

    def do_EOF(self, argv):
        """EOF command exits the program"""
        print()
        return True

    def do_quit(self, argv):
        """quit command exists the console"""
        return True

    def default(self, arg):
        """Default behavior for invalid input"""
        cmd_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            ar = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?\)", ar[1])
            if match:
                cmd = [ar[1][:match.span()[0]], match.group()[1, -1]]
                if cmd[0] in cmd_map:
                    ref = "{} {}".format(ar[0], cmd[1])
                    return cmd_map[cmd[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, argv):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        """
        arg = validate_arg(argv)
        if arg:
            print(eval(arg[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        arg = validate_arg(argv)
        if arg:
            if len(arg) != 2:
                print("** instance id missing **")
            else:
                ref = "{}.{}".format(arg[0], arg[1])
                if ref not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[ref])

    def do_destroy(self, argv):
        """
        Deletes an instance based on the class name and id
        """
        arg = validate_arg(argv)
        if arg:
            if len(arg) != 2:
                print("** instance id missing **")
            else:
                ref = "{}.{}".format(*arg)
                if ref in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, argv):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg = split(argv)
        objects = self.storage.all().values()
        if not arg:
            print([str(obj) for obj in objects])
        else:
            if arg[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects if arg[0] in str(obj)])

    def do_update(self, argv):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        arg = validate_arg(argv)
        if arg:
            if len(arg) != 2:
                print("** instance id missing **")
            else:
                ref = "{}.{}".format(arg[0], arg[1])
                if ref in self.storage.all():
                    if len(arg) == 2:
                        print("** attribute name missing **")
                    elif len(arg) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[ref]
                        if arg[2] not in type(obj).__dict__:
                            setattr(obj, arg[2], arg[3])
                        else:
                            val = type(obj.__class__.__dict__[arg[2]])
                            setattr(obj, arg[2], val(arg[3]))

            self.storage.save()

    def do_count(self, arg):
        """Gets a class instances count"""
        ar = parser(arg)
        count = 0
        for obj in models.storage.all().values():
            if ar[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
