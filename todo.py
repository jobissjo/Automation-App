import streamlit as st

def checkbox_changed(task_list:list[dict], index:int):
    task_list.pop(index)
    

def update_task(task_list:list[dict]):
    if task_list:
        st.write("## Tasks")
        for i, task in enumerate(task_list):
            st.checkbox(f"Task {i+1}: {task.get('text', '')}", 
                                        key=i,on_change=checkbox_changed(task_list, i))
      
    else:
        st.write("Your to-do list is empty.")



def add_task(text, task_list):
    task_list.append({"text": text, "completed": False})
    return task_list

def clear_task(task_list):
    task_list.clear()
    return task_list

def complete_task(task_list):
    task_list = [task for task in task_list if not task["completed"]]
    return task_list

def todo_list():
    st.title("📝 To-Do List")
    tasks = st.text_area("Enter your task here:", "")
    task_str = tasks.strip()
    
    session_state = st.session_state
    if "task_list" not in session_state:
        session_state.task_list = []

    task_list = session_state.task_list

    if st.button("Add Task"):
        task_list = add_task(task_str, task_list)
    if st.button("Clear List"):
        task_list = clear_task(task_list)
    if st.button("Mark Completed"):
        task_list = complete_task(task_list)

    session_state.task_list = task_list
    update_task(task_list)