import smtplib
import datetime
from time import sleep


def sendMessages(hostUsername, hostPassword, yourSleepyFriendPhoneEmail, message, numMessages):
    # Log into server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(hostUsername, hostPassword)
    
    # Send messages
    for i in range(numMessages):
        print("Message #: ", str(i + 1))
        server.sendmail(hostUsername, yourSleepyFriendPhoneEmail, message)


def setAlarm(hostUsername, hostPassword, yourSleepyFriendRingTime, host_to_yourSleepyFriend_timeDiff,
        yourSleepyFriendPhoneEmail, message, numMessages):
    # Run until time is found
    while True:
        
        # Get the current hour, minute, and second
        hostTimeStamp = str(datetime.datetime.now())
        hostMinute = int(hostTimeStamp.split(":")[1])
        hostHour = int(hostTimeStamp.split(":")[0].split(" ")[1])
        
        # Adjust for yourSleepyFriend's time zone
        yourSleepyFriendHour = (hostHour + host_to_yourSleepyFriend_timeDiff) % 24
        
        # Pring present time info
        print("Host Time:\t", str(hostHour) + ":" + str(hostMinute))
        print("Your sleepy friend's Time:\t", str(yourSleepyFriendHour) + ":" + str(hostMinute))
        print("Alarm Time:\t", str(yourSleepyFriendRingTime[0]) + ":" + str(yourSleepyFriendRingTime[1]))
        print("")
        sleep(15)
        
        # If Your sleepy friend's RingTime is reached, then send texts
        if (yourSleepyFriendHour == yourSleepyFriendRingTime[0]) and (hostMinute == yourSleepyFriendRingTime[1]):
            
            # Send text messages
            sendMessages(hostUsername, hostPassword, yourSleepyFriendPhoneEmail,
                         message, numMessages)
            
            # Break out of while loop
            break


if __name__ == "__main__":
    
    ''' Text bombing email account details
    	Host email must allow less secure apps before SMTP server usage:
    	https://www.google.com/settings/security/lesssecureapps'''
    
    hostUsername = "yourEmail@gmail.com"
    hostPassword = "yourEmailsPassword"
    
    # Obviously, change the above for your own needs and do not share!!!
    
    # yourSleepyFriend alarm time details
    yourSleepyFriendRingTime = [1, 10]  # Use military time [hour, minute]
    host_to_yourSleepyFriend_timeDiff = 3  # In hours
    
    # yourSleepyFriend phone details
    #	Details on constructing the proper email address:
    #	http://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/
    
    yourSleepyFriendPhoneEmail = "youryourSleepyFriendsPhone@messaging.sprintpcs.com"
    
    # Text message parameters
    message = "Ring!"
    numMessages = 50  # or 100, or 200, 300, 500, 1000......how badly do you wanna keep your friend?
    
    # Set text bomb alarm clock
    setAlarm(hostUsername, hostPassword, yourSleepyFriendRingTime, host_to_yourSleepyFriend_timeDiff,
             yourSleepyFriendPhoneEmail, message, numMessages)
