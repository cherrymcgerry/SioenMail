import win32com.client

# import pandas as pd
# import xlrd

import os
import pandas as pd
import SioenMail.businessRules.businessrule

outlook= win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
inbox= outlook.GetDefaultFolder(6) #Inbox default index value is 6
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
    print("getting emails from outlook")
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
        SioenMail.businessRules.businessrule.getKeywordsFromBody(messageDict['body'])
        messageDictArr.append(messageDict)

    return messageDictArr

getMessagesFromOutlook()




def dictToPandas(messageDicts):
    print("mapping dictionaries to panda dataframe")

    dict = {'col1' : [], 'col2' : []}
    try:
        for message in messageDicts:
            if 'label' in message and 'body' in  message:
                dict['col1'].append(message['body'])
                dict['col2'].append(message['label'])
    except Exception as ex:
        print(ex)

    df = pd.DataFrame.from_dict(dict)
    return df




#todo split into test and train, split into sentences instead of whole body(messagesToDicts)
def getDataInDataframe():
    print("getting data")

    messagesDict = getMessagesFromOutlook()
    messagesWLabelsDict = matchDictWithLabel(messagesDict)
    df = dictToPandas(messagesWLabelsDict)
    return df



def getDictionaryFromExcel():
    print("getting departments")
    print(os.getcwd())
    projectPath = os.getcwd()
    file_path = projectPath + '/Sioen Del 20 departments.xlsx'
    df = pd.read_excel(file_path, encoding='utf-16')
    dfSliced = df.loc[:,'To':'Department']

    return dfSliced

def matchDictWithLabel(messageDictArr):
    print("matching messages with departments")
    dfLabels = getDictionaryFromExcel()
    for message in messageDictArr:

        try:
            to = message['to']
            loc = dfLabels.loc[dfLabels['To']==to].index[0]
            department = dfLabels.iloc[loc,1]
            #TODO change department into int!!
            #message['label'] = department
            message['label'] = 1

        except Exception as ex:
            print(ex)
    return messageDictArr

print(getDataInDataframe())
test()
getDictionaryFromExcel()
getMessagesFromOutlook()

