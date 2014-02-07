#-------------------------------------------------------------------------------
# Name:        ClubMessenger
# Purpose:
#
# Author:      nathan Bland
#
# Created:     13/06/2013
# Copyright:   (c) nbland 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
import time,  pygvoicelib, getpass, MySQLdb

#-----------------------------------------------------------------------------
def connectToDatabaseAndGetData():
    db = MySQLdb.connect(host="techtc.org",
                         user="",
                         passwd="", #Good bits removed ;)
                         db="")

    cur = db.cursor()
    cur.execute("SELECT * FROM members")

    return cur.fetchall()

#-----------------------------------------------------------------------------
def getNamesFromData(data):
    pass

#-----------------------------------------------------------------------------
def getNumbersFromData(data):
    numbers = []
    for row in data:
        pass

#-----------------------------------------------------------------------------
def getNamesAndNumbersFromData(data):
    nan = dict()
    for idx, row in enumerate(data):
        if not str(row[1]) == "Barry":
			nan[str(row[4])] = str(row[1])
    print nan
    return nan

def sendTextToDict(d, msg):
    x = dict()
    myString = str()
    for key, value in d.iteritems():
        if not value=="Joel" or not value=="Laura":
                print key, value
                name = value.capitalize()
                ourText = name+", "+msg
##                ourText = msg
                sendSms(key, ourText)
    #Limited at first to test workability
    #ONLY SELECTING NUMBERS WE KNOW


#-----------------------------------------------------------------------------
#Takes a username, password, number, and message
def sendSms(number, msg):
    user = ''
    passwd = ''
    voice = pygvoicelib.GoogleVoice(user, passwd)
    try:
        phoneList = voice.get_numbers()
    except pygvoicelib.LoginError, e:
        print 'Failed to login. Reason: %s' % (e.reason)
        print 'Reasons Legend:'
        print '  failed -> Invalid credentails'
        print '  captcha -> Account is captcha locked'
        print '  error -> Unknown/Other errors'
        return
    from_num = ''
    for num in phoneList:
        if num.isdigit() and phoneList[num]['verified']:
                from_num = num
    print 'Login Successful'
    if not from_num:
        print 'Unable to find a validated phone'
        return
    print 'attempting to send sms -> ' + repr(voice.send(number, msg))
    print 'waiting'
    time.sleep(0)
    state = voice.get_state()
    repr(state)
    print state
    print ''
    return
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    #print 'enter your username: '
    data = connectToDatabaseAndGetData()
    #print data
    dataDict = getNamesAndNumbersFromData(data)
    print dataDict
    msg = " game night tonight @ 7:30 in D.B. #302."
    sendTextToDict(dataDict, msg)

##        user = raw_input()
##        print 'enter your password: '
##        passwd = getpass.getpass()
##        print 'enter the number to text: '
##        textNumber = raw_input()
##        print 'enter text to send:\n'
##        msg = raw_input()
##
##        sendSms(user, passwd, textNumber, msg)

