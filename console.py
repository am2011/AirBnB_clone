#!/usr/bin/python3
"""This file contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import storage



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None
    #new code added
    __classes = ["BaseModel", "City", "State", "User", "Place", "Review", "Amenity"]

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
    
    #new code added 
    def do_destroy(self, arg):
        """Deletes the instance that has the cmd arg (class name and id)"""
        arg_list = arg.split(" ")
        if not arg_list:
            print("** class name missing **")
            return None
        elif (arg_list[0] not in HBNBCommand.__calsses):
            print("** class doesn't exist **")
            return None
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


    #new code added
    def do_count(self, arg):
        """ print the count of instances of a class """
        count = 0
        for key in storage.all().keys():
            if arg in key:
                count += 1
        print(count)

    #new code added
    def do_all(self, arg):
        """Prints all string repr. of
        all instances based or not on the class name"""
        arg_list = arg.split(" ")
        obj_list = []

        if len(arg_list) == 0:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)

        elif (arg_list[0] not in HBNBCommand.__calsses):
            print("** class doesn't exist **")

        else:
            for key, value in storage.all().items():
                if arg_list[0] in key:
                    obj_list.append(storage.all()[key].__str__())
                else:
                    return

            print(obj_list)

    
    #new code added
    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        arg_list = arg.split(" ")
        if len(arg_list) == 0:
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.__calsses):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if (key not in obj):
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                setattr(obj[key], arg_list[2], arg_list[3])
                storage.save()






if __name__ == "__main__":
    HBNBCommand().cmdloop()
