

def DictOperations():
    myDict = {}

    myDict["lakesh"] = 3
    myDict["lucky"] =2

    if "lakesh" in myDict:
        myDict["lakesh"] = myDict["lakesh"] -1


    for k,v in myDict.items():
        print(k,v)
        print(f"{k} and {v}")


DictOperations()



