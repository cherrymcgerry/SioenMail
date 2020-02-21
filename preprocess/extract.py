import win32com.client
import pandas as pd
import xlrd
import os
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
        #print(messageDict['to'])
        messageDictArr.append(messageDict)

    return messageDictArr



def getDictionaryFromExcel():
    print(os.getcwd())
    projectPath = os.getcwd()
    file_path = projectPath + '/Sioen Del 20 departments.xlsx'
    df = pd.read_excel(file_path, encoding='utf-16')
    dfSliced = df.loc[:,'To':'Department']

    return dfSliced

def matchDictWithLabel():
    for message in messageDictArr:
        message['label'] = sales

def test():

    # Opvragen departementen
    dfSliced = getDictionaryFromExcel()
    for department in dfSliced:
        department = dfSliced['Department']
        print(department)

    # Opvragen persoonsnamen in to
    messageDictArr = getMessagesFromOutlook()
    for message in messageDictArr:
        name = message['to']

        if name in dfSliced[key]:
            message['to'] = ts
            print(message)

#test()
#getDictionaryFromExcel()
#getMessagesFromOutlook()

