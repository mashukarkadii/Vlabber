API_DOMAIN = "http://127.0.0.1:5000"
VDIR = "vdata"
from pathlib import Path
import os
import requests

def ExP(path) -> bool:
    if os.path.isdir(path):
        return True
    else:
        return False

class rqstAPI:
    def __init__(self, url):
        self.url = url

    def get(self):
        response = requests.get(self.url)
        return response

class api:
    def __init__(self, args = dict):
        self.args = args

    def reSetFlags(self, newFlagsArray = list):
        flags = newFlagsArray
        myId=self.args[f"myId"]
        hwid=self.args[f"hwid"]
        itog_Flags = ""
        old_Flags = ""
        if ExP(VDIR):
            for filename in os.listdir(VDIR):
                file_path = os.path.join(VDIR, filename)
                if file_path.endswith(".flags"):
                    flagO = filename.split(".")[0]
                    old_Flags += flagO + ","
                    os.remove(file_path)
            for flag in flags:
                fl=open(f"{VDIR}\\{flag}.flags", "a", encoding='ansi')
                fl.write("%**$4#@%*\n*&\n()^%$*")
                fl.close()
                itog_Flags += flag + ","
            itog_Flags = itog_Flags[:-1]
            old_Flags = old_Flags[:-1]
            url=f"{API_DOMAIN}/api/setFlags?oldFlags={old_Flags}&newFlags={itog_Flags}&myId={myId}&hwid={hwid}"
            r=rqstAPI(url)
            t=r.get()
            if t.text == "200":
                return True
            else:
                return False
            
            
                    
                    
    def sendMessage(self):
        args = self.args
        flagsNum = args[f"flagsNum"]
        messageText = args[f"messageText"]
        randomFlag = args[f"randomFlag"]
        hwid = args[f"hwid"]
        myId = args[f"myId"]
        adrId = args[f"adrId"]
        url=f"{API_DOMAIN}/api/sendMessage?flagsNum={flagsNum}&messageText={messageText}&randomFlag={randomFlag}&hwid={hwid}&myId={myId}&adrId={adrId}"
        r = rqstAPI(url)
        response = r.get()
        if response.text == "1":
            return True
        else:
            return False
        
  

    def getUpdates(self):
        args = self.args
        flagsNum = args[f"flagsNum"]
        randomFlag = args[f"randomFlag"]
        hwid = args[f"hwid"]
        myId = args[f"myId"]
        adrId=args[f"adrId"]
        url=f"{API_DOMAIN}/api/getUpdates?flagsNum={flagsNum}&randomFlag={randomFlag}&hwid={hwid}&myId={myId}&adrId={adrId}"
        r = rqstAPI(url)
        response = r.get()
        return response
    
    def addContact(self):
        a=self.args
        flagsNum = a[f"flagsNum"]
        randomFlag = a[f"randomFlag"]
        hwid = a[f"hwid"]
        myId = a[f"myId"]
        adrId=a[f"adrId"]
        url=f"{API_DOMAIN}/api/addContact?flagsNum={flagsNum}&randomFlag={randomFlag}&hwid={hwid}&myId={myId}&adrId={adrId}"
        r = rqstAPI(url)
        response = r.get()
        if response.text == "200":
            return True
        else:
            return False
        
    def getAccount(self):
        a=self.args
        hwid=a[f"hwid"]
        myId=a[f"myId"]
        flags=a[f"flags"]
        url=f"{API_DOMAIN}/api/getAccount?hwid={hwid}&flags={flags}&myId={myId}"
        rt=rqstAPI(url=url)
        t=rt.get()
        text = t.text
        if text=="200":
            return True
        else:
            return False
        
    def checkId(self):
        myId=self.args[f"myId"]
        url=f"{API_DOMAIN}/api/getId?myId={myId}"
        rt=rqstAPI(url)
        t=rt.get()
        if t.text=="yes":
            return False
        else:
            return True
        
    def getChatUpdates(self):
        args = self.args
        flagsNum = args[f"flagsNum"]
        randomFlag = args[f"randomFlag"]
        hwid = args[f"hwid"]
        myId = args[f"myId"]
        url=f"{API_DOMAIN}/api/getChatUpdates?flagsNum={flagsNum}&randomFlag={randomFlag}&hwid={hwid}&myId={myId}"
        r = rqstAPI(url)
        response = r.get()
        return response

        
