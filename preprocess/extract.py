import win32com.client
import os
import pandas as pd
outlook=win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
inbox=outlook.GetDefaultFolder(6) #Inbox default index value is 6
folder = outlook.Folders[1]





#method to get all messages from outlook into a readable format
#connects to outlook through pywin32
#return array of message dictionaries with format:
#to
#subject
#body
#recipients
#sender
#senderAddress
def getMessagesFromOutlook():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
    root = outlook.Folders[1]
    sentItems = folder.Folders[1]
    messages = sentItems.items
    messageDictArr = []
    for message in messages:
        messageDict = {}
        messageDict['to'] = message.To
        messageDict['subject'] = message.Subject
        messageDict['body'] = message.Body
        messageDict['recipients'] = message.Recipients
        messageDict['sender'] = message.Sender
        messageDict['senderAddress'] = message.Sender.Address
        print(messageDict['to'])
        messageDictArr.append(messageDict)

    return messageDictArr


getMessagesFromOutlook()



def dictToPandas(messageDicts):
    dict = {'col1' : [], 'col2' : []}
    for message in messageDicts:
        dict['col1'].append(message['body'])
        dict['col2'].append(message['label'])

    df = pd.DataFrame.from_dict(dict)
    return df









