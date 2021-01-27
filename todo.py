#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdout, argv
import os.path
from datetime import datetime

def help():
    h = \
        """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    stdout.buffer.write(h.encode('utf8'))

def display():
    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as current:
            todo = current.readlines()
        n_task = len(todo)
        if n_task == 0:
            stdout.buffer.write('No pending task. Type "./todo help" for help...'.encode('utf8'))
        show = ''
        for task in todo:
            show += '[{}] {}'.format(n_task, task)
            n_task -= 1
        stdout.buffer.write(show.encode('utf8'))
    else:
        stdout.buffer.write('There are no pending todos!'.encode('utf8'))
        
def add(task):
    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as prev:
            todo = prev.read()
    else:
        todo = ''
    with open('todo.txt', 'w') as current:
        current.write(task + '\n' + todo)
    stdout.buffer.write('Added todo: "{}"'.format(task).encode('utf8'))

def delete(n):
    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as prev:
            todo = prev.readlines()
        n_task = len(todo)
        if n > 0 and (n <= n_task):
            with open('todo.txt', 'w') as current:
                for task in todo:
                    if n_task != n:
                        current.write(task)
                    n_task -= 1
            stdout.buffer.write('Deleted todo #{}'.format(n).encode('utf8'))
        else:
            stdout.buffer.write('Error: todo #{} does not exist. Nothing deleted.'.format(n).encode('utf8'))
    else:
        stdout.buffer.write('Error: todo #{} does not exist. Nothing deleted.'.format(n).encode('utf8'))

def mark(n):
    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as prev:
            todo = prev.readlines()
        n_task = len(todo)
        if n > 0 and n <= n_task:
            with open('todo.txt', 'w') as current:
                if os.path.isfile('done.txt'):
                    with open('done.txt', 'r') as done:
                        done_todo = done.read()
                    with open('done.txt', 'w') as done_new:
                        for task in todo:
                            if n_task == n:
                                done_new.write('x '+ datetime.today().strftime('%Y-%m-%d') + ' ' + task)
                            else:
                                current.write(task)
                            n_task -= 1
                        done_new.write(done_todo)
                else:
                    with open('done.txt', 'w') as done_new:
                        for task in todo:
                            if n_task == n:
                                done_new.write('x '+ datetime.today().strftime('%Y-%m-%d') + ' ' + task)
                            else:
                                current.write(task)
                            n_task -= 1
            stdout.buffer.write('Marked todo #{} as done.'.format(n).encode('utf8'))
        else:
            stdout.buffer.write('Error: todo #{} does not exist.'.format(n).encode('utf8'))
    else:
        stdout.buffer.write('Error: todo #{} does not exist.'.format(n).encode('utf8'))

def report():
    c_Todo = 0
    c_Done = 0
    if os.path.isfile('todo.txt'):
        with open('todo.txt', 'r') as current:
            todo = current.readlines()
        c_Todo = len(todo)

    if os.path.isfile('done.txt'):
        count = 0
        with open('done.txt', 'r') as done:
            done_todo = done.readlines()
            for x in done_todo:
                item = x.split()
                if item[1] == str(datetime.today().strftime('%Y-%m-%d')):
                    count += 1
    line = datetime.today().strftime('%Y-%m-%d') \
        + ' Pending : {} Completed : {}'.format(c_Todo, count)
    stdout.buffer.write(line.encode('utf8'))

    
def main():

    if len(argv) == 1:
        help()

    elif argv[1] == 'help':
        if len(argv) == 2: 
            help()
        else:
            stdout.buffer.write('SYNTAX ERROR: Invalid Input. Type "./todo help" for more help...'.encode('utf8'))
        
    elif argv[1] == 'add':
        if len(argv) == 3:
            add(argv[2])
        else:
            stdout.buffer.write('Error: Missing todo string. Nothing added!'.encode('utf8'))

    elif argv[1] == 'del':
        if len(argv) == 3:
            try:
                n = float(argv[2])
                if n == int(n):
                    delete(int(n))
                else:
                    stdout.buffer.write('Error: Use Integer value after "del". Type "./todo help" for more help...'.encode('utf8'))
            except:
                stdout.buffer.write('Error: Use Integer value after "del". Type "./todo help" for more help...'.encode('utf8'))
        else:
            stdout.buffer.write('Error: Missing NUMBER for deleting todo.'.encode('utf8'))

    elif argv[1] == 'done':
        if len(argv) == 3:
            try:
                n = float(argv[2])
                if n == int(n):
                    mark(int(n))
                else:
                    stdout.buffer.write('Error: Use Integer value after "done". Type "./todo help" for more help...'.encode('utf8'))
            except:
                stdout.buffer.write('Error: Use Integer value after "done". Type "./todo help" for more help...'.encode('utf8'))
        else:
            stdout.buffer.write('Error: Missing NUMBER for marking todo as done.'.encode('utf8'))
    
    elif argv[1] == 'ls':
        if len(argv) == 2:
            display()
        else:
            stdout.buffer.write('SYNTAX ERROR: Invalid Input. Type "./todo help" for more help...'.encode('utf8'))
        
    elif argv[1] == 'report':
        if len(argv) == 2:
            report()
        else:
            stdout.buffer.write('SYNTAX ERROR: Invalid Input. Type "./todo help" for more help...'.encode('utf8'))
    else:
        stdout.buffer.write('SYNTAX ERROR: Invalid Input. Type "./todo help" for help...'.encode('utf8'))

if __name__ == '__main__':
    main()