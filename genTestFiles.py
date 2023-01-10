
import random, os

i = 0

e = [".log", ".temp", ".c", ".tmp"]

randomExtension = ""
filename = ""

while i<=100:
    randomExtension = e[random.randint(0,len(e)-1)]
    filename = str(i) + randomExtension
    open(os.path.join("sampleFolder", filename), "w")
    i=i+1

print("FILES GENERATED")
