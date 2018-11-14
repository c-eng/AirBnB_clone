#!/usr/bin/python3
""" Console module
"""
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models import *
from models import storage
from models import __all__ as model_classes



class HBNBCommand(cmd.Cmd):
    """HBNB Console Class
    """

    prompt = '(hbnb) '

    class_list = model_classes

    def do_quit(self, arg):
        """Quit console
        """
        return True

    def do_EOF(self, arg):
        """Alternative quit console
        """
        print()
        return True

    def emptyline(self):
        """Does Nothing
        """
        pass

    def do_create(self, arg):
        """ creates instance of a specifified class
        """
        if self.validator(1, arg) is not None:
            x = eval(arg)()
            storage.save()
            print(x.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
        class name and id """
        token = self.validator(2, arg)
        if token is not None:
            new = storage.all().get(token[0] + "." + token[1])
            print(eval("{}(**new)".format(token[0])))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        token = self.validator(2, arg)
        if token is not None:
            storage.all().pop(token[0] + "." + token[1])
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name"""
        if not arg:
            print([str(eval("{}(**{})".format(value["__class__"], value))) for
                   key, value in storage.all().items()])
        else:
            token = self.validator(1, arg)
            if token is not None:
                print([str(eval("{}(**{})".format(value["__class__"], value)))
                       for key, value in storage.all().items() if
                       value['__class__'] == token[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute
        """
        token = self.validator(4, arg)
        if token is not None:
            temp = storage.all()
            kwargs = temp[token[0] + "." + token[1]]
            kwargs.update({token[2]: token[3]})
            x = eval("{}(**{})".format(token[0], kwargs))
            x.save()

    def validator(self, count, arg):
        """ checks for good argument string
        """
        token = shlex.split(arg)
        if count >= 1 and len(token) < 1:
            print("** class name missing **")
        elif count >= 1 and token[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif count >= 2 and len(token) < 2:
            print("** instance id missing **")
        elif count >= 2 and (token[0] + "." + token[1] not in
                             storage.all().keys()):
            print("** no instance found **")
        elif count >= 3 and len(token) < 3:
            print("** attribute name missing **")
        elif count >= 4 and len(token) < 4:
            print("** value missing **")
        else:
            return token


if __name__ == '__main__':
    HBNBCommand().cmdloop()
