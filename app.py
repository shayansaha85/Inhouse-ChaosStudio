from flask import *
import connection_file as cf
import cpu_anomalies as cpu
import disk_anomalies as disk
import memory_anomalies as memory
import logrem_backend

chaosStudio = Flask(__name__, static_url_path="/static")

credentials =  {
    'username' : "",
    'password' : "",
    "ip" : ""
}

@chaosStudio.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    p = "o"
    if request.method == 'POST':
        p = "o"
        credentials['username'] = request.form.get("username")
        credentials['password'] = request.form.get("password")
        credentials['ip'] = request.form.get("ip")
        
        if(cf.loginCheck(credentials)):
            print("DEBUG : Login Successful")
            return redirect(url_for('tools'))
        else:
            msg = "false" 
            print("DEBUG : Login Failed")

        print(msg)
        print(credentials)
    return render_template("login_page.html", msg=msg, p=p)


@chaosStudio.route("/tools", methods = ["GET", "POST"])
def tools():
    return render_template("tools.html")

@chaosStudio.route("/tools_page", methods=["GET", "POST"])
def tools_page():    
    return render_template("tools_page.html")

@chaosStudio.route("/sre_tools", methods = ["GET" , "POST"])
def sre_tools():
    return render_template("sre_tools.html")

@chaosStudio.route("/logrem", methods = ["GET", "POST"])
def logrem():
    q = ""
    heading = ""
    listOfFiles = ""
    footer = ""

    if request.method == "POST":
        pathLogFolder = request.form.get("pathLogFolder")
        maxSizeLimit = request.form.get("maxSizeLimit")
        unitOfSize = request.form.get("unitOfSize")
        extensions = request.form.get("extensions")
    
        output_nodes = logrem_backend.remove_logs(pathLogFolder, maxSizeLimit, unitOfSize, extensions)
        heading = output_nodes["heading"]
        listOfFiles = output_nodes["listOfFiles"]
        footer = output_nodes["footer"]
        q = "true"


    return render_template("logrem.html", heading=heading, listOfFiles=listOfFiles, footer=footer,q=q)

@chaosStudio.route("/cpu_utilities", methods=["GET", "POST"])
def cpu_utilities():
    conn = cf.get_conn(credentials)
    if request.method == "POST":
        # variables for cpu stress
        cpuStress_cores = request.form.get("cpuStress_cores")
        cpuStress_percentage = request.form.get("cpuStress_percentage")
        cpuStress_duration = request.form.get("cpuStress_duration")

        # variables for random cpu spike stress
        cpuSpikeRandom_cores = request.form.get("cpuSpikeRandom_cores")
        cpuSpikeRandom_number = request.form.get("cpuSpikeRandom_number")
        cpuSpikeRandom_percentage_min = request.form.get("cpuSpikeRandom_percentage_min")
        cpuSpikeRandom_percentage_max = request.form.get("cpuSpikeRandom_percentage_max")
        cpuSpikeRandom_duration = request.form.get("cpuSpikeRandom_duration")
        cpuSpikeRandom_timegap = request.form.get("cpuSpikeRandom_timegap")

        # variables for fixed cpu spike stress
        cpuSpikeFixed_cores = request.form.get("cpuSpikeFixed_cores")
        cpuSpikeFixed_number = request.form.get("cpuSpikeFixed_number")
        cpuSpikeFixed_percentage = request.form.get("cpuSpikeFixed_percentage")
        cpuSpikeFixed_duration = request.form.get("cpuSpikeFixed_duration")
        cpuSpikeFixed_timegap = request.form.get("cpuSpikeFixed_timegap")

        if cpuStress_cores != None and cpuStress_percentage != None and cpuStress_duration != None:
            cpu.execute_CPUStress(conn, cpuStress_percentage, cpuStress_cores, cpuStress_duration)
  
        if cpuSpikeRandom_cores != None and cpuSpikeRandom_number != None and cpuSpikeRandom_percentage_min != None and cpuSpikeRandom_percentage_max != None and cpuSpikeRandom_duration != None and cpuSpikeRandom_timegap != None:
            cpu.execute_CPUSpikesRandom(conn, cpuSpikeRandom_cores, cpuSpikeRandom_number, cpuSpikeRandom_percentage_min, cpuSpikeRandom_percentage_max, cpuSpikeRandom_duration, cpuSpikeRandom_timegap)
        
        if cpuSpikeFixed_cores != None and cpuSpikeFixed_number != None and cpuSpikeFixed_percentage != None and cpuSpikeFixed_duration != None and cpuSpikeFixed_timegap != None:
            cpu.execute_CPUSpikesFixed(conn, cpuSpikeFixed_number, cpuSpikeFixed_duration, cpuSpikeFixed_cores, cpuSpikeFixed_percentage, cpuSpikeFixed_timegap)

    return render_template("cpu_utilities.html")


@chaosStudio.route("/memory_utilities", methods=["GET", "POST"])
def memory_utilities():
    conn = cf.get_conn(credentials)
    if request.method == "POST":
        # variables for memory stress
        memoryStress_size = request.form.get("memoryStress_size")
        memoryStress_duration = request.form.get("memoryStress_duration")

        # variables for memory spikes random
        memorySpikeRandom_number = request.form.get("memorySpikeRandom_number")
        memorySpikeRandom_size_min = request.form.get("memorySpikeRandom_size_min")
        memorySpikeRandom_size_max = request.form.get("memorySpikeRandom_size_max")
        memorySpikeRandom_duration = request.form.get("memorySpikeRandom_duration")
        memorySpikeRandom_timegap = request.form.get("memorySpikeRandom_timegap")

        # variables for memory spikes fixed
        memorySpikeFixed_number = request.form.get("memorySpikeFixed_number")
        memorySpikeFixed_size = request.form.get("memorySpikeFixed_size")
        memorySpikeFixed_duration = request.form.get("memorySpikeFixed_duration")
        memorySpikeFixed_timegap = request.form.get("memorySpikeFixed_timegap")

        if memoryStress_size != None and memoryStress_duration != None:
            memory.execute_MemoryStress(conn, memoryStress_size, memoryStress_duration)
       
        if memorySpikeRandom_number != None and memorySpikeRandom_size_min != None and memorySpikeRandom_size_max != None and memorySpikeRandom_duration != None and memorySpikeRandom_timegap != None:
            memory.execute_MemorySpikeRandom(conn, memorySpikeRandom_number, memorySpikeRandom_size_min, memorySpikeRandom_size_max, memorySpikeRandom_duration, memorySpikeRandom_timegap)
       
        if memorySpikeFixed_number != None and memorySpikeFixed_size != None and memorySpikeFixed_duration != None and memorySpikeFixed_timegap != None:
            memory.execute_MemorySpikeFixed(conn, memorySpikeFixed_number, memorySpikeFixed_size, memorySpikeFixed_duration, memorySpikeFixed_timegap)

    return render_template("memory_utilities.html")


@chaosStudio.route("/disk_utilities", methods=["GET", "POST"])
def disk_utilities():
    conn = cf.get_conn(credentials)
    if request.method == "POST":
        # variable for disk stress
        diskStress_percentage = request.form.get("diskStress_percentage")
        diskStress_duration = request.form.get("diskStress_duration")

        # variable for disk spikes random
        diskSpikeRandom_number = request.form.get("diskSpikeRandom_number")
        diskSpikeRandom_percentage_min = request.form.get("diskSpikeRandom_percentage_min")
        diskSpikeRandom_percentage_max = request.form.get("diskSpikeRandom_percentage_max")
        diskSpikeRandom_duration = request.form.get("diskSpikeRandom_duration")
        diskSpikeRandom_timegap = request.form.get("diskSpikeRandom_timegap")

        # variables for disk spikes fixed
        diskSpikeFixed_number = request.form.get("diskSpikeFixed_number")
        diskSpikeFixed_percentage = request.form.get("diskSpikeFixed_percentage")
        diskSpikeFixed_duration = request.form.get("diskSpikeFixed_duration")
        diskSpikeFixed_timegap = request.form.get("diskSpikeFixed_timegap")

        if diskStress_percentage != None and diskStress_duration != None:
            disk.execute_DiskStress(conn, diskStress_percentage, diskStress_duration)
        
        if diskSpikeRandom_number != None and diskSpikeRandom_percentage_min != None and diskSpikeRandom_percentage_max != None and diskSpikeRandom_duration != None and diskSpikeRandom_timegap != None:
            disk.execute_DiskStressRandom(conn, diskSpikeRandom_number, diskSpikeRandom_percentage_min, diskSpikeRandom_percentage_max, diskSpikeRandom_duration, diskSpikeRandom_timegap)
        
        if diskSpikeFixed_number != None and diskSpikeFixed_percentage != None and diskSpikeFixed_duration != None and diskSpikeFixed_timegap != None:
            disk.execute_DiskStressFixed(conn, diskSpikeFixed_number, diskSpikeFixed_percentage, diskSpikeFixed_duration, diskSpikeFixed_timegap)
    
    return render_template("disk_utilities.html")


if __name__ == "__main__":
    chaosStudio.run(debug=True, host="0.0.0.0")