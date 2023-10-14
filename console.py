#!/usr/bin/python3
"""
console.py contains the entry point
of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the AirBnB command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Use it to quit the interpreter"""
        return True

    def do_EOF(self, arg):
        """Ctrl-D exits the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        return False

    def do_create(self, arg):
        """Create a new instance from the BaseModel class"""
        if arg == "":
            print("** class name missing **")
        elif arg == "BaseModel":
            from models.base_model import BaseModel
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        arguments = arg.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif arguments[0] == "BaseModel" and arguments[1]:
            found = False
            from models import storage
            all_objects = storage.all()
            for key, value in all_objects.items():
                if value.id == arguments[1]:
                    found = True
                    print(f'{str(value)}')
                    break
            if not found:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arguments = arg.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif arguments[0] == "BaseModel" and arguments[1]:
            found = False
            from models import storage
            all_objects = storage.all()
            for key, value in all_objects.items():
                if value.id == arguments[1]:
                    found = True
                    del all_objects[key]
                    storage.save()
                    break
            if not found:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of all instances based on the class name"""
        from models import storage
        from models.base_model import BaseModel
        args = arg.split()
        result = []
        if len(args) != 0:
            if args[0] != "BaseModel":
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for key, value in storage.all().items():
                result.append(value.__str__())
        print(result)

    def do_update(self, arg):
        """Updates the attributes of an object based on the class name and the id"""
        arguments = arg.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] == "BaseModel":
            if len(arguments) == 1:
                print("** instance id missing **")
            elif len(arguments) == 2:
                print("** attribute name missing **")
            elif len(arguments) == 3:
                print("** value missing **")
            else:
                instance_found = False
                from models import storage
                all_objects = storage.all()
                for key, value in all_objects.items():
                    if value.id == arguments[1]:
                        instance_found = True
                        setattr(value, arguments[2], arguments[3])
                        storage.save()
                if not instance_found:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
