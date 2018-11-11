#!/usr/bin/python3
"""Console module
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNB Console Class
    """

    prompt = '(hbnb) '
    class_list = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                  "Review"]

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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
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
                    del temp[token[0] + "." + token[1]]
                    FileStorage._FileStorage__objects = temp
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name"""
        temp = storage.all()
        if not arg:
            print([str(eval("{}(**{})".format(value["__class__"], value))) for
                   key, value in temp.items()])
        else:
            token = shlex.split(arg)
            if token[0] not in HBNBCommand.class_list:
                print("** class doesn't exist ** ")
            else:
                print([str(eval("{}(**{})".format(value["__class__"], value)))
                       for key, value in temp.items() if value['__class__'] ==
                       token[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute
        """
        token = shlex.split(arg)
        if len(token) < 1:
            print("** class name missing **")
        elif token[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        elif token[1] not in [x.split(".")[-1] for x in storage.all().keys()]:
            print("** no instance found **")
        elif len(token) < 3:
            print("** attribute name missing **")
        elif len(token) < 4:
            print("** value missing **")
        else:
            temp = storage.all()
            x = eval("{}(**{})".format(token[0], temp[token[0] + "." +
                     token[1]]))
            setattr(x, token[2], token[3])
            temp[token[0] + "." + token[1]] = x.to_dict()
            FileStorage._FileStorage__objects = temp
            storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
