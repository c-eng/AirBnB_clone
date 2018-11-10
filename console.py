#!/usr/bin/python3
"""Console module
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNB Console Class
    """

    prompt = '(hbnb) '
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """Quit console
        """
        return True

    def do_EOF(self, arg):
        """Alternative quit console
        """
        return True

    def emptyline(self):
        """Does Nothing
        """
        pass

    def do_create(self, arg):
        """ creates instance of a specifified class
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                x = eval("{}()".format(arg))
                print(x.id)
            except(NameError):
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
        class name and id """
        if not arg:
            print("** class name missing **")
        else:
            token = shlex.split(arg)
            if token[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif len(token) < 2:
                print("** instance id missing **")
            else:
                temp = storage.all()
                if token[0] + "." + token[1] not in temp:
                    print("** no instance found **")
                else:
                    new = temp[token[0] + "." + token[1]]
                    print(eval("{}(**new)".format(token[0])))








if __name__ == '__main__':
    HBNBCommand().cmdloop()
