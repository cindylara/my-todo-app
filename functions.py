FILEPATH = "todos.txt"


# Default arguments
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    # We cannot perform ead action on files hat do no exist
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list """
    # On write mode if the file does not exist it will be created
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# The below print out will be only visible into this functions file
if __name__ == "__main__":
    print(get_todos())
