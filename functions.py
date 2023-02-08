FILEPATH='./todo.txt'
# dir(functions)

def get_todo_file(todofile:str=FILEPATH)->list:
    try:
        with open(todofile,'rt') as tfile:
            todo=[item.strip('\n') for item in tfile.readlines()] #list comprehension!!!
            # print('Read from todo file!!!')
            return(todo)
    except FileNotFoundError:
        return([])

def write_todo_file(todo:list,todofile:str=FILEPATH)->None:
    with open(todofile,'wt') as tfile:
        tfile.writelines([f'{item}\n' for item in todo])
        # print('Written to todo file!!!')

def add_todo()->str:
    """Get input from user for todo""" # docstring -- help()!!!
    userin=input('Enter a todo: ').strip()
    return(userin.capitalize())

def edit_del_todo(tlen:int,act:str='blabla')->int: # default param, non def param need to come first!!!
    """helper function for edit and del to get todo index input"""
    user_opt=input(f'Enter todo index to {act}: ')
    while not user_opt.isnumeric() or int(user_opt)>tlen or int(user_opt)==0:
        user_opt=input(f'Enter index from list to {act}: ')
    return(int(user_opt)-1)

def show_todo(a:list)->None:
    print('Todo list:\n------------')
    for index, item in enumerate(a,1): #enumerate !!!
        # print(str(index+1)+'. '+item.title())
        print(f"{index}. {item}") # fstring contains {var} !!!
    print(" ")

if __name__ == "__main__":
    print(f"Here is the todo list from file:\n\
        \n{get_todo_file('todo.txt')}")