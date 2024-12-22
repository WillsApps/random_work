import subprocess
from time import sleep

while True:
    some_command = "/Users/will.burdett/projects/random_work/src/macbook_utils/move_notifications.scpt"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    # This makes the wait possible
    p_status = p.wait()
    print(p_status)
    sleep(10)
