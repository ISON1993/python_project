import random
def makeRandomStr(count,length):
    str = "abcdefghijklmnopqrstuvwxyz0123456789"
    result = []
    for x in range(count):
        randomStr = ''
        for y in range(length):
            randomStr = randomStr + random.choice(str)
        result.append(randomStr)

    print(result)
makeRandomStr(5,10)
