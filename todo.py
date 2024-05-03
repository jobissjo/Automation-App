# import streamlit as st
# from db import ToDo
# from sqlalchemy.orm import Session

# completed_list:list[dict] = []

# def marked_completed(db: Session):
#     global completed_list
#     for li in completed_list:
#         is_complete = li.get('completed', False)
#         print("is complete",is_complete )
#         if li.get('completed', False):
#             index = li.get('task').id

#             todo = db.query(ToDo).filter(ToDo.id == index).first()
#             if todo:
                
#                 todo.completed = True
#                 db.commit()
#                 db.refresh(todo)
#     db.commit()


# def delete_tasks(completed_task_list: list, db:Session):
#     print("HERE", completed_task_list)
#     for task in completed_task_list:
#         print(task)
#         index_id = task.id
#         if index_id:
#             print("true i am find it")
#             todo = db.query(ToDo).filter(ToDo.id ==index_id).first()
#             if todo:
#                 db.delete(todo)
#     db.commit()

# def update_task(db: Session):
#     global completed_list
#     all_tasks = db.query(ToDo).all()
#     if all_tasks:
#         st.write("## Tasks")
#         completed_tasks = []
#         for i, task in enumerate(all_tasks):
#             if not task.completed:
#                 val = st.checkbox(f"Task {i+1}: {task.task}", 
#                                         key=i)
#                 completed_list.append({'task':task, 'completed': val})
#             else:
#                 completed_tasks.append(task)
#         if len(completed_tasks):
#             st.write("Completed Tasks")
#             for i,task in enumerate(completed_tasks):
#                 st.checkbox(f"Task {i+1}: {task.task}", 
#                                         key=f"completed_{i}", value=True)
#             st.button("Delete complete tasks", on_click=delete_tasks(completed_tasks, db))

#     else:
#         st.write("Your to-do list is empty.")



# def add_task(text,  db: Session):

#     todo = ToDo(task=text,completed=False)
#     db.add(todo)
#     db.commit()


# def clear_task(db: Session):
#     db.query(ToDo).delete()
#     db.commit()


# def complete_task(task_list):
#     task_list = [task for task in task_list if not task["completed"]]
#     return task_list

# def todo_list(db:Session):
#     global completed_list
#     print("I am on todo list")
#     st.title("📝 To-Do List")
#     tasks = st.text_area("Enter your task here:", "")
#     task_str = tasks.strip()
    
#     if st.button("Add Task"):
#         add_task(task_str,db)
#     if st.button("Clear List"):
#         clear_task(db)
#     if st.button("Marked Completed"):
#         marked_completed(db)

#     update_task(db)



# from sqlalchemy.orm import sessionmaker
# from db import Base
# from todo import todo_list



# engine = create_engine('sqlite:///taskmaster.db') 
#create database engine
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)

# def create_session():
#     session = Session(engine)
#     try:
#         yield session
#     finally:
#         session.close()
# elif selected_option == "To Do":
#     session = Session()
#     todo_list(session)


# from sqlalchemy import create_engine, Column, Integer, String,Boolean, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime, timezone
# from sqlalchemy import create_engine

# Base = declarative_base()

# class ToDo(Base):
#     __tablename__= 'todo'

#     id = Column(Integer, primary_key=True)
#     task = Column(String, nullable=False)
#     completed = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.now(timezone.utc))

