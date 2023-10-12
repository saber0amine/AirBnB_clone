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
        "use it to quit the interpreter\n"
        return True

    def do_EOF(self, arg):
        """Ctrl - D exit the program\n"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn't execute anything"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()