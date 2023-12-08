import time
level = 1
num_zombie = 4
while level > 0:
    time.sleep(2)
    level += 1
    num_zombie += 5

    print(level)
    print(num_zombie)
