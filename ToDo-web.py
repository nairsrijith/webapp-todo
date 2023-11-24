import streamlit as webpage
import functions


todos = functions.get_todos()


def add_todo():
    todo = webpage.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    webpage.session_state["new_todo"] = ""


webpage.title("My ToDo App")
webpage.header("This is my todo app.")
webpage.write("This will simplify your task tracking")

for index, todo in enumerate(todos):
    checkbox = webpage.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del webpage.session_state[todo]
        webpage.rerun()

webpage.text_input(label="Enter or modify a todo item here:",
                   label_visibility="hidden",
                   placeholder="Add new todo...",
                   on_change=add_todo, key="new_todo")
