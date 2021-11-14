from datetime import datetime



#this function generate the next primary key based on given previous used primary key 
def getNewPrimaryKey(pStr):
    vStr=pStr
    vLength=len(vStr)
    vDatePartComing=vStr[0:8]
    vConstantPart=vStr[8:9]
    vIncrementPart=vStr[9:vLength]
    vIncrementPartLength=len(vIncrementPart)
    vAfterIncrement=int(vIncrementPart)+1
    vDigitsInNumber=getDigitCount(vAfterIncrement)
    vAppendZero=vLength-9-vDigitsInNumber
    vTmpStr=""
    for i in range(vAppendZero):
        vTmpStr=vTmpStr+"0"
    vIncrementedPart=vTmpStr+str(vAfterIncrement)

    vDate = datetime.now()
    vDatePartToday=vDate.strftime("%Y")+ vDate.strftime("%m")+vDate.strftime("%d")
    if vDatePartToday==vDatePartComing:
        vPrimaryKey=vDatePartComing+vConstantPart+vIncrementedPart
    else:
        vTmpStr=""
        for i in range(vIncrementPartLength-1):
            vTmpStr=vTmpStr+"0"
        vTmpStr=vTmpStr+"1"    
        vPrimaryKey=vDatePartToday+vConstantPart+vTmpStr 
    return vPrimaryKey

#--This function returns the number of digit in a gaven number e.g 523 has 3 digit 
def getDigitCount(pNumber):
    count=0
    while (pNumber > 0):
        pNumber = pNumber//10
        count = count + 1
    return count


# print(getNewPrimaryKey('20210704E0001'))

# vStr='20210705E0123' 
# vLength=len(vStr)
# vDatePart=vStr[0:8]
# vConstantPart=vStr[8:9]
# vIncrementPart=vStr[9:vLength]
# vIncrementPartLength=len(vIncrementPart)
# vAfterIncrement=int(vIncrementPart)+1
# vDigitsInNumber=get_digits(vAfterIncrement)
# vAppendZero=vLength-9-vDigitsInNumber
# vTmpStr=""
# for i in range(vAppendZero):
#     vTmpStr=vTmpStr+"0"
# vIncrementedPart=vTmpStr+str(vAfterIncrement)
# print("Given: ",vStr)
# print("Date Part: ",vDatePart)
# print("Constant Part: ",vConstantPart)
# print("Length of String: ",vLength)
# print("Increment Part Number : ",vIncrementPart)
# print("incremented: ",vAfterIncrement)
# print("increment part length =",vIncrementPartLength)
# print("Digits in increment part: ",vDigitsInNumber)
# print("incremented part into string: ",str(vAfterIncrement))
# print("Append Zeros: ",vAppendZero)
# print("Append",vTmpStr)
# print("Incremented Number Part : ",vIncrementedPart)
# print("Next Primary Key: ",vDatePart+vConstantPart+vIncrementedPart)    