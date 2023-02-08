import streamlit as st
import functions
##commit: add del todo capblty into webapp sec:19

todos=functions.get_todo_file()

def add_todo():
    todo=st.session_state['-NewTodo-'].strip()
    if todo!='':
        todos.append(todo.capitalize())
        functions.write_todo_file(todos)
    # print(todo)

def del_todo(index):
    todos.pop(index)
    functions.write_todo_file(todos)

st.title('My Todo App')
app='!!'
st.subheader(f'This is a todo app{app}')
st.write('This app will increase your productivity')

# for todo in todos:
# #     st.checkbox(todo,on_change=del_todo,args=todo,key=todo)

for index,todo in enumerate(todos):
    st.checkbox(todo,key=index,on_change=del_todo,kwargs={'index':index})

st.text_input(label='New Todo',label_visibility='collapsed',
            key='-NewTodo-',placeholder='Add a todo...',
            on_change=add_todo)

# print('Marker----')
# st.session_state
