#Get xpath username from list_link_xpath.txt
def GetXpathUserName():
    FILE = open('list_link_xpath.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        xpath_user_name = LINES[1]
        return xpath_user_name

#Get xpath user work from list_link_xpath.txt
def GetXpathUserWork():
    FILE = open('list_link_xpath.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        xpath_user_work = LINES[3]
        return str(xpath_user_work)

#Get xpath user education from list_link_xpath.txt
def GetXpathUserEducation():
    FILE = open('list_link_xpath.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        xpath_user_education = LINES[5]
        print(xpath_user_education)
        return str(xpath_user_education)

#Get xpath user live from list_link_xpath.txt
def GetXpathUserLive():
    FILE = open('list_link_xpath.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        xpath_user_live = LINES[7]
        return str(xpath_user_live)

#Get xpath user hometown from list_link_xpath.txt
def GetXpathUserHometown():
    FILE = open('list_link_xpath.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        xpath_user_hometown = LINES[9]
        return str(xpath_user_hometown)

#Get xpath user hometown from list_link_xpath.txt
def GetXpathUserRelationship():
    FILE = open('list_link_xpath.txt','r')
    LINES = FILE.readlines()

    if len(LINES) > 0:
        LINES = [line.strip() for line in LINES]
        xpath_user_relationship = LINES[11]
        return str(xpath_user_relationship)