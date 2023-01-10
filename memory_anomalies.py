import time
import connection_file
import random

def execute_MemoryStress(conn, Memtoburn, Memory_duration):
    t_end = time.time() + 1 * int(Memory_duration)
    stdin, stdout, stderr = conn.exec_command('dd if=/dev/zero bs={MemoryMB}M of=/dev/null'.format(MemoryMB = Memtoburn))
    print('dd if=/dev/zero bs={MemoryMB}M of=/dev/null'.format(MemoryMB = Memtoburn))
    # print(stdout.read().decode().strip())
    Memorycmd = ('dd if=/dev/zero bs={MemoryMB}M of=/dev/null'.format(MemoryMB = Memtoburn))
    Memorycmd1 = "'"+Memorycmd+"'"
    pscmd = ('/bin/ps -C {Memorycmd2} -o pid='.format(Memorycmd2 = Memorycmd1))
    stdin, stdout, stderr = conn.exec_command('/bin/ps -C {Memorycmd2} -o pid='.format(Memorycmd2 = Memorycmd1))
    processid = stdout.read().decode().strip()
    print("find the process ID below")
    print("process id length -->",len(str(processid)))
    print(processid)
    time.sleep(int(Memory_duration))
    conn.exec_command('kill {processid1}'.format(processid1 = processid))


def execute_MemorySpikeRandom(conn, noOfSpike, SpikeMinimumSize, SpikeMaximumSize, SpikeDuration, SleepDuration):
    SpikeMinimumSize = int(SpikeMinimumSize)*1024
    SpikeMaximumSize = int(SpikeMaximumSize)*1024
    i = 0
    while i<int(noOfSpike):
        spikeSize = random.randint(SpikeMinimumSize, SpikeMaximumSize)
        print("max size :",SpikeMinimumSize)
        print("min size :",SpikeMaximumSize)
        print("random size generated :",spikeSize)
        print(f"Executing memory stress #{i+1}")
        execute_MemoryStress(conn, spikeSize, SpikeDuration)
        print("execute_MemoryStress() method completed")
        time.sleep(int(SleepDuration))
        i += 1

def execute_MemorySpikeFixed(conn, noOfSpike, SpikeSize, SpikeDuration, SleepDuration):
    i = 0
    while i<int(noOfSpike):
        print(f"Executing memory stress #{i+1}")
        execute_MemoryStress(conn, SpikeSize, SpikeDuration)
        time.sleep(int(SleepDuration))
        i += 1
