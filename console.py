#!/usr/bin/python3
"""Entry to command interpreter"""

import cmd
import ast
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Entry point of HBNB console"""

    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program with Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Does nothing when empty arg is entered"""
        pass

    def do_create(self, arg):
        """command to create instance of basemodel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            obj = storage.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints string representation of an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            argv = arg.split(' ')
            if argv[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argv[0], argv[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroys a basemodel instance based on class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            argv = arg.split(' ')
            if argv[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argv[0], argv[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances"""
        if arg != "":
            argv = arg.split(" ")
            if argv[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                strform = [str(obj) for key, obj in storage.all().items()
                           if type(obj).__name__ == argv[0]]
                print(strform)
        else:
            strform = [str(obj) for key, obj in storage.all().items()]
            print(strform)

    def do_update(self, arg):
        """
        Updates an instance based on class name and id
        by adding or updating attribute
        then save it to JSON file
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            argv = arg.split(' ')
            if argv[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            elif len(argv) < 3:
                print("** attribute name missing **")
            elif len(argv) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(argv[0], argv[1])
                if key in storage.all():
                    obj = storage.all()[key]
                    attr_name = argv[2]
                    attr_value = argv[3]
                    setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** no instance found **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            argv = arg.split(' ')
            if argv[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                count = len(storage.all())
                instances = [obj for obj in storage.all().values()
                             if type(obj).__name__ == argv[0]]
                print(len(instances))

    def default(self, arg):
        """Accepts class name followed by an argument"""
        argv = arg.split('.')
        arg = argv[0]
        if len(argv) == 1:
            print("*** Unknown syntax: {}".format(arg))
            return
        try:
            argv = argv[1].split('(')
            command = argv[0]
            if command == 'all':
                self.do_all(arg)
            elif command == 'count':
                self.do_count(arg)
            elif command == 'show':
                argv = argv[1].split(')')
                id_arg = argv[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = arg + ' ' + id_arg
                self.do_show(arg)
            elif command == 'destroy':
                argv = argv[1].split(')')
                id_arg = argv[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = arg + ' ' + id_arg
                self.do_destroy(arg)
            elif command == 'update':
                argv = argv[1].split(',')
                id_arg = argv[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = argv[1].strip(',')
                val_arg = argv[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                self.do_update(arg)
            else:
                print("*** Unknown syntax: {}".format(arg))
        except IndexError:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
