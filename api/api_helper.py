import os
import pathlib
import json

def getAccount(myId, flags, hwid):
    users_dir = pathlib.Path("users")
    myIdPath = users_dir / f"{myId}"
    os.makedirs(myIdPath)

    user_dir = pathlib.Path(f"users\\{myId}")
    user_file = user_dir / f"{myId}.json"
    j=open(user_file, 'a', encoding='utf-8')

    uflags = flags.split(',')
    user_data = {
        "myId": myId,
        "chats": [],
        "flags": uflags,
        "hwid": hwid
    }
    json.dump(user_data, j, indent=4, ensure_ascii=False)




    jj=open("users.json", 'r', encoding='utf-8')
    data=json.load(jj)
    users=data["users"]
    users.append(myId)

    jjj=open("users.json", 'w', encoding='utf-8')
    json.dump(data, jjj, indent=4, ensure_ascii=False)
    return "200"


def getId(myId):
    j=open("users.json", 'r', encoding='utf-8')
    data=json.load(j)
    users=data["users"]
    if myId not in users:
        return "no"
    else:
        return "yes"


def getChatUpdates(myId, randomFlag, flagsNum, hwid):
    user_dir = pathlib.Path(f"users\\{myId}")
    user_file = user_dir / f"{myId}.json"
    
    j=open(user_file, "r", encoding='utf-8')
    data=json.load(j)
    uhwid=data["hwid"]
    uflags=data["flags"]
    print(uhwid)
    

    if len(uflags) == int(flagsNum) and randomFlag in uflags and hwid == uhwid:
        chats = data["chats"]
        return chats
    else:
        return "[]"
    


def addContact(myId, randomFlag, flagsNum, hwid, adrId):
    user_dir = pathlib.Path(f"users\\{myId}")
    user_file = user_dir / f"{myId}.json"
    
    j=open(user_file, "r", encoding='utf-8')
    data=json.load(j)
    uhwid=data["hwid"]
    flags=data["flags"]
    

    if len(flags) == int(flagsNum) and randomFlag in flags and hwid == uhwid:
        data["chats"].append(adrId)
        jj=open(user_file, "w", encoding='utf-8')
        json.dump(data, jj, indent=4, ensure_ascii=False)
        return "200"
    return "400"


def comined(id1, id2):
    return int(id1) + int(id2)


def getUpdates(myId, randomFlag, flagsNum, hwid, adrId):
    user_dir = pathlib.Path(f"users\\{myId}")
    user_file = user_dir / f"{myId}.json"
    
    j=open(user_file, "r", encoding='utf-8')
    data=json.load(j)
    uhwid=data["hwid"]
    flags=data["flags"]

    if len(flags) == int(flagsNum) and randomFlag in flags and hwid == uhwid:
        comb = comined(myId, adrId)
        mesFile = user_dir / f"{comb}.json"
        data = None
        if os.path.isfile(mesFile):
           jj=open(mesFile, 'r', encoding='utf-8')
           data=json.load(jj)
        else:
           jjj=open(mesFile, 'a', encoding='utf-8')
           jjj.write("[]")
           jjj.close()
           jj=open(mesFile, 'r', encoding='utf-8')
           data=json.load(jj)
        return data
    return "[]"


def sendMessage(myId, randomFlag, flagsNum, hwid, adrId, messageText):
    user_dir = pathlib.Path(f"users\\{myId}")
    user_file = user_dir / f"{myId}.json"
    
    j=open(user_file, "r", encoding='utf-8')
    data=json.load(j)
    uhwid=data["hwid"]
    flags=data["flags"]

    if len(flags) == int(flagsNum) and randomFlag in flags and hwid == uhwid:
        comb = comined(myId, adrId)
        mesFile = user_dir / f"{comb}.json"
        jj=open(mesFile, 'r', encoding='utf-8')
        data=json.load(jj)
        message = {
            "start_id": myId,
            "message": messageText,
            "message_id": len(data) + 1
        }
        data.append(message)
        jjj=open(mesFile, 'w', encoding='utf-8')
        json.dump(data, jjj, indent=4, ensure_ascii=False)
        return "1"
    return "2"


def checkFlags(old, now):
    print(old)
    print(now)
    count = 0
    for flag in old:
        if flag in now:
            count = count + 1
    if count == len(now):
        return True



def setFlags(myId, oldFlags, newFlags, hwid):
    user_dir = pathlib.Path(f"users\\{myId}")
    user_file = user_dir / f"{myId}.json"
    
    j=open(user_file, "r", encoding='utf-8')
    data=json.load(j)
    uhwid=data["hwid"]
    flags=data["flags"]
    
    res = checkFlags(oldFlags.split(','), flags)
    Newflags = newFlags.split(',')
    if uhwid == hwid and res == True:
        print("ddfsdfsdfsdfsdfsdf")
        data["flags"].clear()
        for flag in Newflags:
            data["flags"].append(flag)
        jj=open(user_file, 'w', encoding='utf-8')
        json.dump(data, jj, indent=4, ensure_ascii=False)
        return "200"
    return "400"