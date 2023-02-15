import streamlit as st
import functions

todos=functions.get_todos('todos.txt')
def add_todo():
    todo = st.session_state['new_todo'] + '\n' #dictionary syntax has key= new_todo
    todos.append(todo)
    functions.write_todos('todos.txt',todos)

todos=functions.get_todos('todos.txt')

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo..", on_change=add_todo, key='new_todo')

st.session_state