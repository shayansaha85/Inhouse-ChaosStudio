import time
import math
import random
import connection_file

def execute_DiskStress(conn, disk_perc, duration):
    stdin, stdout, stderr = conn.exec_command('df -h /')
    disk_info = stdout.readlines()[-1]
    available = disk_info.split()[3]
    available_GB = float(available.strip('G'))
    size_to_occupy = available_GB * (int(disk_perc)/100)
    conn.exec_command("fallocate -l {size_to_occupy}M testfile".format(size_to_occupy = math.ceil(size_to_occupy*1024)))
    time.sleep(int(duration))
    conn.exec_command("rm testfile")


def execute_DiskStressRandom(conn, noOfSpike, minSpikePercentage, maxSpikePercentage, durationSpike, timeGap):
    i = 0
    random_perc = 0
    while i<int(noOfSpike):
        random_perc = random.randint(int(minSpikePercentage), int(maxSpikePercentage))
        execute_DiskStress(conn, random_perc, durationSpike)
        time.sleep(int(timeGap))
        i += 1

def execute_DiskStressFixed(conn, noOfSpike, spikePerc, durationSpike, timeGap):
    i = 0
    
    while i<int(noOfSpike):
        execute_DiskStress(conn, spikePerc, durationSpike)
        time.sleep(timeGap)
        i += 1