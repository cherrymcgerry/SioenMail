import win32com.client
import os
outlook=win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
inbox=outlook.GetDefaultFolder(6) #Inbox default index value is 6
folder = outlook.Folders[1]






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


getMessagesFromOutlook()