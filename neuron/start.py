import os
import traceback
import logging
import sys

sys.tracebacklimit = 0
EXISTING_LABS = os.listdir('./solves')





Lab_Number = str(int(input("Enter # of lab to run: ")))


try:
    if EXISTING_LABS.index(Lab_Number) >= 0:
        print('Found the lab!')

    lab_tasks = os.listdir('./solves/'+Lab_Number)
    lab_tasks.sort()
    print('Found this tasks: ', lab_tasks)

    def run_task(task_file_name):
        print('\n\nTask ' + task)
        task_file_path = './solves/' + Lab_Number + '/' + task_file_name
        try:
            exec(open(task_file_path).read())
        except Exception as e:
            logging.error(traceback.format_exc())
        print('\nDone with task ' + task_file_name + '\n')

    for task in lab_tasks:
        run_task(task)


except ValueError:
    print('Unknown lab specified')
