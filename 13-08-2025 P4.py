class MyClass:
    def print_func(self, pos1, pos2, a, b=0, *args, **kwargs):

        print(f"parameters received are {pos1}, {pos2}")
        
        print(f"positional args are {a}, {b}")
        
        if args:
            print(f"args are {list(args)}")
        else:
            print("args are []")
        
        if kwargs:
            print(f"kwargs are {kwargs}")
        else:
            print("kwargs are {}")


obj = MyClass()

obj.print_func(1, 2, a=4, b=5, *["a", "c", 45], m="d", l=5)
print()

obj.print_func(1, 2, a=4, *["a", 45], m="d", l=5)
