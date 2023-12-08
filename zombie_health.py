import time
level = 1
zombie_health = 100
while level > 0:
    if level <= 9:
        time.sleep(2)
        level += 1
        zombie_health = 100 * level

    elif level >= 10:
        time.sleep(2)
        level += 1
        zombie_health = zombie_health + (zombie_health // 10)
    print(level)
    print(zombie_health)


