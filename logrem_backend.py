import os


def getSize(fileNameWithPath):
    size_of_file = os.stat(fileNameWithPath).st_size
    return size_of_file

def getExtension(filename):
    extension = filename.split(".")[-1]
    return extension.lower().strip()

def remove_logs(pathLogFolder, maxSizeLimit, unitOfSize, extensions):
    extensions = extensions.lower().strip()
    maxS = 0
    elist = []
    unitOfSize = unitOfSize.lower().strip()
    
    for x in extensions.split(","):
        elist.append(x.strip())

    files = os.listdir(pathLogFolder)
    files_with_specific_extensions = []
    
    for f in files:
        if getExtension(f.strip()) in elist:
            files_with_specific_extensions.append(f.strip())
    
    files_with_path = []
    
    for x in files_with_specific_extensions:
        files_with_path.append(os.path.join(pathLogFolder, x))
    
    if unitOfSize == "gb":
        maxS = float(maxSizeLimit)*1024*1024*1024
    elif unitOfSize == "mb":
        maxS = float(maxSizeLimit)*1024*1024
    elif unitOfSize == "kb":
        maxS = float(maxSizeLimit)*1024
    elif unitOfSize == "b":
        maxS = float(maxSizeLimit)

    total_released_space = 0
    files_to_be_deleted = []

    for x in files_with_path:
        if float(getSize(x)) >= maxS:
            total_released_space += float(getSize(x))
            files_to_be_deleted.append(x)
    
    for x in files_to_be_deleted:
        print(x)
        os.remove(x)
    
    output_nodes = {
        "heading" : "",
        "listOfFiles" : "",
        "footer" : ""
    }
    
    output_nodes["heading"] = "FILES EXCEEDING MAXIMUM SIZE LIMIT"
    k = 1
    for x in files_to_be_deleted:
        output_nodes["listOfFiles"] += os.path.basename(x) + "\n\n"
    
    output_nodes["listOfFiles"] += "="*10
    output_nodes["footer"] = f"TOTAL DISK SPACE RELEASED = {int(total_released_space)} Bytes"

    return output_nodes
    


