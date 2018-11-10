#!/usr/bin/python3
"""Console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Console Class
    """

    prompt = '(hbnb) '
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
