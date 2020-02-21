from multi_rake import Rake
#Rake library om keyworden te extraheren uit een string

rake = Rake()
def getKeywordsFromBody(var):
    keywords = rake.apply(var)
    print(keywords[:10])

    #Declaratie mogelijke keywords
    vacature = ['Bachelor', 'master ', 'manager', 'vacature', 'spontane sollicitatie', 'veel ervaring', 'CV', 'kennis en vaardigheden', "sollicitatie"]
    sponsering = ['Sponsering', 'sponsor', 'sponser', 'reclame', 'ondersteunen', 'steunen', 'sponsorbrief', 'sponserbrief']
    offerte= ['pricing', 'offerte', 'prijsaanvraag', 'quotation request', 'prijsvraag', 'enquiring', 'quote',
             'catalogus', 'prijs lijst', 'beste prijzen', 'prijslijst'
             'verzendtijd', 'levertijd', 'levertermijn', 'delivery conditions', 'request for quotation']
    aanmaning= ['tweede herinnering', 'aanmaning', 'deurwaarder', 'openstaande factuur', 'vandaag de nodige betalingen te verrichten']
    array = [vacature,sponsering,offerte,aanmaning]
    arrayWordcounter = []
    #Opsplitsen van body in kleinere strings
    wordlist = var.split()
    # n = 5
    # newText = [' '.join(wordlist[i:i + n]) for i in range(0, len(wordlist), n)]

    wordCounter = 0

    # print(newText)
    # for word in vacature:
    #     for sentence in newText:
    #         if sentence.__contains__(word):
    #
    #             wordCounter= wordCounter + 1
    #             print("word: " + str(word) + " counter: " + str(wordCounter)
    arraynumber = 0
    for subarray in array:
        for word in subarray:
            wordCounter += wordlist.count(word)
            if wordlist.__contains__(word):
                print(word)
        arrayWordcounter.append(wordCounter)
        wordCounter = 0
    print(arrayWordcounter)

    return keywords