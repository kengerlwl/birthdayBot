import yaml
import os




def getPeople():
    curPath = os.path.dirname(os.path.realpath(__file__))
    peoplePath = os.path.join(curPath, "../config/people.yaml")
    peopleFile = open(peoplePath, 'r', encoding='utf-8')
    peopleDict = yaml.load(peopleFile.read(), Loader=yaml.FullLoader)
    return peopleDict["People"]


def getTemplate():
    
    curPath = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(curPath, "../config/config.yaml")
    configFile = open(configPath, 'r', encoding='utf-8')
    confiDict = yaml.load(configFile.read(), Loader=yaml.FullLoader)

    print(confiDict)

    # 
    botEmail = os.environ.get('botEmail')
    SMTPPwd = os.environ.get('SMTPPwd')
    print("botEmail", botEmail)
    if botEmail:
        confiDict['Send']['Email'] = botEmail
    if SMTPPwd:
        confiDict['Send']['SMTPPwd'] = SMTPPwd

    return confiDict["Template"]