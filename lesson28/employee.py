

class employee:

    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called")


def create_obj():
    print("creating an object...")
    obj = employee()
    print("the function end..")
    return obj

print("calling create_obj() function....")
obj = create_obj()
print("program ends.....")

