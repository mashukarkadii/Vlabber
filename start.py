import os
import platform
import hashlib
import random
import API



def getHwid():
    info = []
    info.append(platform.processor())
    info.append(platform.machine())
    info.append(platform.node())
    info.append(platform.platform())
    info.append(platform.version())
    info.append(platform.system())
    hash_object = hashlib.sha256()
    hash_object.update("".join(info).encode('utf-8'))
    hardware_id = hash_object.hexdigest()
    return hardware_id


def getNewFlags():
    newFlags = []
    rangeF = random.randint(3, 10)
    for i in range(rangeF):
        flag = f"{random.randint(10000000000000, 90000000000000)}"
        newFlags.append(flag)
    return newFlags


def getRandomId():
    while True:
        myId = random.randint(1000000000000000000, 9000000000000000000)
        api=API.api(args={"myId": myId})
        res=api.checkId()
        if res:
            return myId


def getId():
    file="vdata\\s90d839kd9s833s.vdt"
    with open(file, "r", encoding="utf-8") as f:
        myId=f.readline()
        return myId

def startAccount():
    hwid=getHwid()
    flags=getNewFlags()
    flagsNew = ""
    for flag in flags:
        flagsNew += flag + ","
    flagsNew=flagsNew[:-1]
    myId=getRandomId()
    api=API.api(args={"myId": myId, "hwid": hwid, "flags": flagsNew})
    res=api.getAccount()
    if res:
        os.makedirs("vdata")
        for flag in flags:
            fl=open(f"vdata\\{flag}.flags", 'a', encoding='ansi')
            fl.write("%**$4#@%*\n*&\n()^%$*")
            fl.close()
        fl=open("vdata\\s90d839kd9s833s.vdt", 'a', encoding='utf-8')
        fl.write(f"{myId}")
        fl.close()
        

def getFlags():
    VDIR = "vdata"
    flags = []
    for filename in os.listdir(VDIR):
        file_path = os.path.join(VDIR, filename)
        if file_path.endswith(".flags"):
            flagO = filename.split(".")[0]
            flags.append(flagO)
    return flags

def start_messager():
    vdir="vdata"
    myId = ""
    if os.path.isdir(vdir):
        file="vdata\\s90d839kd9s833s.vdt"
        if os.path.isfile(file):
            with open(file, "r", encoding="utf-8") as f:
                myId=f.readline()
            newFlags = getNewFlags()
            apI = API.api(args={"myId": myId, "hwid": getHwid()})
            res=apI.reSetFlags(newFlags)
            if res:
                return True
            else:
                return False
    else:
        startAccount()

        

        
                