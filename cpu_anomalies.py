import time
import random
import connection_file as cf


def execute_CPUStress(conn, percentage, cores, duration):
    server = "Linux"
    if server == "Linux":
        print("Executing stress")
        stdin, stdout, stderr = conn.exec_command("stress-ng -c {cores} -l {percentage}% -t {duration}".format(cores=cores, percentage=percentage, duration=duration))
        print(stdout.read().decode().strip())
    

def execute_CPUSpikesFixed(conn, no_of_spikes, duration_of_each_spike, cores, spike_percentage, sleep):
    # install_stressng(conn)
    k = 0
    for i in range(int(no_of_spikes)):
        print(f"Executing stress #{k+1}")
        execute_CPUStress(conn, str(spike_percentage), str(cores), str(duration_of_each_spike))
        time.sleep(int(sleep))
        k += 1


def execute_CPUSpikesRandom(conn, cores, no_of_spikes, minSpikePercentage, maxSpikePercentage, DurationOfEachSpike, sleep):
    # install_stressng(conn)
    i = 0
    while i<int(no_of_spikes):
        perc = random.randint(int(minSpikePercentage), int(maxSpikePercentage))
        print(f"Executing stress #{i+1}")
        execute_CPUStress(conn, perc, cores, DurationOfEachSpike)
        time.sleep(int(sleep))
        i += 1


def install_stressng(conn):
    try:
        stdin, stdout, stderr = conn.exec_command("yum install -y stress-ng")
        print(stdout.read().decode().strip())
        print("Installation successful")
    except:
        stdin, stdout, stderr = conn.exec_command("apt install -y stress-ng")
        print(stdout.read().decode().strip())
        print("Installation successful")
