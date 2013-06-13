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
import time,  pygvoicelib, getpass
#-----------------------------------------------------------------------------
#Takes a username, password, number, and message
def sendSms(user, passwd, number, msg):
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
    time.sleep(15)
    state = voice.get_state()
    repr(state)
    print state
    return
#-----------------------------------------------------------------------------
if __name__ == '__main__':
        #print 'enter your username: '
        user = 'nathan.bland@gmail.com'
        print 'enter your password: '
        passwd = getpass.getpass()
        print 'enter the number to text: '
        textNumber = '3039561667,7203417006'#raw_input()
        print 'enter text to send:\n'
        msg = 'This awesome text is being sent through a python script.'#raw_input()

        sendSms(user, passwd, textNumber, msg)

