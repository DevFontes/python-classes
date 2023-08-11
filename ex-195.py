# Create and manipulate task in json file

import os
import json

option       = ''
redo_tasks   = []
FILE_PATH    = 'ex-195.json'

def list_tasks(tasks_list):
    if not tasks_list:
        print("No Tasks!")
        return

    os.system('clear')
    print('Tasks:')
    for i in tasks_list:
        print(f'\t{i}')

def add(task, tasks_list):
    tasks.append(task)

def undo(redo_tasks, task_list):
    if not task_list:
        print('No task to undo')
        return

    task = task_list.pop()
    redo_tasks.append(task)

def redo(redo_tasks, task_list):
    if not redo_tasks:
        print('No task to redo')
        return

    task = redo_tasks.pop()
    task_list.append(task)

def read_file(tasks, file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('The file dont exist!')
        save_file(tasks, FILE_PATH)
    return data

def save_file(tasks, file_path):
    with open(file_path, 'w') as file:
        data = json.dump(tasks, file, indent=2, ensure_ascii=False)
    return data

tasks = read_file([], FILE_PATH)

while option != 'e':
    print('JSON Module\n(L)ist - (U)ndo - (R)edo - (E)xit\n')
    option = input('Chose one option or inform one Task:')

    commands = {
        'l': lambda: list_tasks(tasks),
        'u': lambda: undo(redo_tasks, tasks),
        'r': lambda: redo(redo_tasks, tasks),
        'add': lambda: add(option, tasks),
    }

    command = commands.get(option) if commands.get(option) is not None else commands['add']
    command()
    save_file(tasks, FILE_PATH)

    # if option.lower() == 'l':
    #     list_tasks(tasks) 
    # elif option.lower() == 'u':
    #     undo(redo_tasks, tasks)
    # elif option.lower() == 'r':
    #     redo(redo_tasks, tasks)
    # elif option.lower() == 'e':
    #     break
    # else:
    #     add(option, tasks)