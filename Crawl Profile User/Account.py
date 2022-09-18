#Get username from account.txt
def GetUsername():
    FILE = open('account.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        ID = LINES[0]
        return str(ID)

#Get password from account.txt
def GetPassWord():
    FILE = open('account.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        PASS = LINES[1]
        return str(PASS)
