from flask import Flask, request
import api_helper

application = Flask(__name__)



@application.route('/api/getAccount', methods = ['GET'])
def getAccount():
    hwid = request.args.get('hwid')
    flags = request.args.get('flags')
    myId = request.args.get('myId')
    if hwid == None or flags == None or myId == None:
        return "404"
    return api_helper.getAccount(myId=myId, flags=flags, hwid=hwid)


@application.route('/api/getId', methods = ['GET'])
def getId():
    myId = request.args.get('myId')
    return api_helper.getId(myId=myId)


@application.route('/api/getChatUpdates', methods = ['GET'])
def getChatUpdates():
    flagsNum = request.args.get('flagsNum')
    randomFlag = request.args.get('randomFlag')
    hwid = request.args.get('hwid')
    myId = request.args.get('myId')
    if hwid == None or randomFlag == None or myId == None or flagsNum == None:
        return "[]"
    return api_helper.getChatUpdates(myId=myId, flagsNum=flagsNum, randomFlag=randomFlag, hwid=hwid)


@application.route('/api/addContact', methods = ['GET'])
def addContact():
    flagsNum = request.args.get('flagsNum')
    randomFlag = request.args.get('randomFlag')
    hwid = request.args.get('hwid')
    myId = request.args.get('myId')
    adrId = request.args.get('adrId')
    if hwid == None or randomFlag == None or myId == None or flagsNum == None or adrId == None:
        return "400"
    return api_helper.addContact(myId=myId, flagsNum=flagsNum, randomFlag=randomFlag, hwid=hwid, adrId=adrId)



@application.route('/api/getUpdates', methods = ['GET'])
def getUpdates():
    flagsNum = request.args.get('flagsNum')
    randomFlag = request.args.get('randomFlag')
    hwid = request.args.get('hwid')
    myId = request.args.get('myId')
    adrId = request.args.get('adrId')
    if hwid == None or randomFlag == None or myId == None or flagsNum == None or adrId == None:
        return "['error_args']"
    return api_helper.getUpdates(myId=myId, flagsNum=flagsNum, randomFlag=randomFlag, hwid=hwid, adrId=adrId)
    

@application.route('/api/sendMessage', methods = ['GET'])
def sendMessage():
    flagsNum = request.args.get('flagsNum')
    randomFlag = request.args.get('randomFlag')
    hwid = request.args.get('hwid')
    myId = request.args.get('myId')
    adrId = request.args.get('adrId')
    messageText = request.args.get('messageText')

    if hwid == None or randomFlag == None or myId == None or flagsNum == None or adrId == None or messageText == None: 
        return "error"
    return api_helper.sendMessage(myId=myId, flagsNum=flagsNum, randomFlag=randomFlag, hwid=hwid, adrId=adrId, messageText=messageText)

@application.route('/api/setFlags', methods = ['GET'])
def setFlags():
    hwid = request.args.get('hwid')
    myId = request.args.get('myId')
    newFlags = request.args.get('newFlags')
    oldFlags = request.args.get('oldFlags')
    if hwid == None or newFlags == None or myId == None or oldFlags == None:
        return "400"
    return api_helper.setFlags(hwid=hwid, myId=myId, newFlags=newFlags, oldFlags=oldFlags)
    
if __name__ == '__main__':
    application.run(host="0.0.0.0")