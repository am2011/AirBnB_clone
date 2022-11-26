#############!/usr/bin/python3
"""This file contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import storage



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True
    
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True
    
    def emptyline(self):
        """ENTER will print emptyline.\n"""
        print(end="")
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        if not arg:
            print("** class name missing")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            storage.save()
            print(new_model.id)
    
    def do_show(self, arg):
        """Prints the string representaton of an instance based on the class name and id"""
        try:
            if not arg:
                raise SyntaxError
            arg_list = arg.split(" ")
            if arg_list[0] != "BaseModel":
                raise NameError
            if not arg_list[1]:
                raise IndexError

            instances = storage.all()
            key = arg_list[0] + "." + arg_list[1]

            if key in instances:
                print(instances[key])
            else:
                raise KeyError

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
                    


if __name__ == "__main__":
    HBNBCommand().cmdloop()
