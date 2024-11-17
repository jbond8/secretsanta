from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random
import os
import shutil
import datetime
import string
from mangum import Mangum

users_db = {}

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
handler = Mangum(app)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.mount("/img", StaticFiles(directory="templates/img"), name="img")

templates = Jinja2Templates(directory="templates")

base_logins_store = []
new_logins_store = {}
giftDic_store = []

onering =""
choices = string.punctuation + string.digits + string.ascii_letters
for digit in range(10):
    choice = random.choice(choices)
    onering += choice

print(f"One Ring Inscribed '{onering}' to Rule Them All...")

start_path = os.getcwd()
log_path = os.path.join(start_path, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

def get_logins():
    return new_logins_store

def get_baselogins():
    return base_logins_store

def get_gifts():
    return giftDic_store

@app.get('/')
async def home(request:Request):
    return templates.TemplateResponse('home.html',context={'request':request,'id':id})

@app.post('/secretsanta')
async def secretsanta(request:Request):
    return templates.TemplateResponse('secretsanta.html',context={'request':request,'id':id})

@app.post('/login')
async def secretsanta(request:Request):
    return templates.TemplateResponse('login.html',context={'request':request,'id':id})

@app.post('/register')
async def secretsanta(request:Request):
    return templates.TemplateResponse('register.html',context={'request':request,'id':id})

@app.post('/flyfool')
async def flyfool(request:Request):
    return templates.TemplateResponse('flyfools.html', context={'request':request,'id':id})

@app.get('/pwdused')
async def pwdused(pwd):
    """
    Takes inputed password and verfies if it has been used to make a user-made login alreaady.
    """
    logins = get_logins()
    
    pwd_s = []
    for login_pwd in logins.values():
        pwd_s.append(login_pwd)
    
    if pwd in pwd_s:
        return False
    else:
        return True
    
@ app.get('/makelogin')
async def makelogin(request: Request,username, password):
    """
    Makes and stores user-made login.

    System logs registration.
    """
    username = str(username)
    password = str(password)
    new_logins_store[username] = password

    client_ip = request.client.host
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    log = os.open(os.path.join(log_path, f"{timestamp}. [REGISTRATION]. {username}"), os.O_WRONLY | os.O_CREAT)
    log_text = f"CLIENT IP: {client_ip}\nUSERNAME: {username}\nPASSWORD: {password}\nDATE MADE: {datetime.datetime.now()}"
    os.write(log, log_text.encode())

    print()

    return True

@app.get('/logins')
async def logins(request: Request, ring = 0):
    """
    Allows for the Admin to see user-made logins.

    If someone fails to provide the correct Admin password, system will log attempt.
    """
    client_ip = request.client.host

    if ring == onering:
        logins = get_logins()
        return logins
    else:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log = os.open(os.path.join(log_path, f"{timestamp}. [UNAUTHORIZED ATTEMPT]. LOGINS"), os.O_WRONLY | os.O_CREAT)
        log_text = f"CLIENT IP: {client_ip}\nDATE: {timestamp}"
        os.write(log, log_text.encode())

        return await flyfool(request=request)

@app.get('/gifts')
async def gifts(request: Request, ring = 0):
    """
    Allows for the Admin to see Secret Santa givers and recipients.

    If someone fails to provide the correct Admin password, system will log attempt.
    """
    client_ip = request.client.host

    if ring == onering:
        gifts = get_gifts()
        return gifts
    else:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log = os.open(os.path.join(log_path, f"{timestamp}. [UNAUTHORIZED ATTEMPT]. GIFTS"), os.O_WRONLY | os.O_CREAT)
        log_text = f"CLIENT IP: {client_ip}\nDATE: {datetime.datetime.now()}"
        os.write(log, log_text.encode())

        return await flyfool(request=request)

@app.get('/login_check')
async def login_check(username, password):
    """
    Takes a user's inputed username and password and checks agaisnt user-made logins to verify login.
    """
    print(f"username: {username}")
    print(f"password: {password}")

    logins = get_logins()
    
    users = []
    for user in logins.keys():
        users.append(user)

    pwds = []
    for pwd in logins.values():
        pwds.append(pwd)
    
    if username in users:
        if password in pwds:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
            log = os.open(os.path.join(log_path, f"{timestamp}. [LOGIN]. {username}"), os.O_WRONLY | os.O_CREAT)
            log_text = f"USERNAME: {username}\nPASSWORD: {password}\nDATE MADE: {datetime.datetime.now()}"
            os.write(log, log_text.encode())

            return True
        else:
            return False
    else:
        return False
    
@app.get('/gift_check')
async def gift_check(password):
    """
    Takes a user's inputed password and checks agaisnt base logins to get the coresponding receiver for the user.
    """
    password = str(password)
    gifts = get_gifts()
    logins = get_baselogins()

    pwds = []
    for pwd in logins[0].keys():
        pwds.append(pwd)

    if password in pwds:
        print(f"Your person is: {gifts[0].get(logins[0].get(password))}")
        return gifts[0].get(logins[0].get(password))
    else:
        print("Invalid Password")
        return False


@app.get('/make_secretsanta')
async def make_secretsanta(request: Request, numAttend, givers, ring):
    """
    Takes the people attending a secret santa event, and assigns recipients to givers for the event.

    Returns a dictionary of givers -> recipients and a dictionary of passwords for retrieving recipient
    """
    if ring == onering:
        numAttend = int(numAttend)

        givers = givers.split(',')

        while True:
            recipients = random.sample(givers, len(givers))
            if all(givers[person] != recipients[person] for person in range(len(givers))):
                break

        giftDic = {givers[person]: recipients[person] for person in range(numAttend)}

        passList = {str(random.randrange(1000, 9999)): givers[person] for person in range(numAttend)}
        
        base_logins_store.clear()
        giftDic_store.clear()

        base_logins_store.append(passList)
        giftDic_store.append(giftDic)

        client_ip = request.client.host
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log = os.open(os.path.join(log_path, f"{timestamp}. [OFFICIAL]. MAKE-SECRET-SANTA"), os.O_WRONLY | os.O_CREAT)
        log_text = f"GIFT DIC: {giftDic}\nPASSWORDS: {passList}"
        os.write(log, log_text.encode())

        return giftDic, passList
    else:
        client_ip = request.client.host
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log = os.open(os.path.join(log_path, f"{timestamp}. [UNAUTHORIZED ATTEMPT]. MAKE-SECRET-SANTA"), os.O_WRONLY | os.O_CREAT)
        log_text = f"CLIENT IP: {client_ip}\nDATE: {timestamp}"
        os.write(log, log_text.encode())

        return await flyfool(request=request)

@app.get('/restore_secretsanta')
async def restore_secretsanta(request: Request, giftDic, passList, ring):
    """
    Takes in string of giftDic and passList, which an admin can find in past log files, and restores them to the fastAPI.

    BE SURE TO 
    """
    if ring == onering:
        giftDic = giftDic.replace(" ","")
        passList = passList.replace(" ","")
        giftDic = giftDic.replace("'","")
        passList = passList.replace("'","")
        giftDic = giftDic.split(",")
        passList = passList.split(",")

        givers = []
        recipients = []
        for item in giftDic:
            giver, recipient = item.split(':')
            givers.append(giver)
            recipients.append(recipient)

        pwds = []
        pwd_givers = []
        for item in passList:
            pwd, pwd_giver = item.split(':')
            pwds.append(pwd)
            pwd_givers.append(pwd_giver)

        numAttend = len(givers)

        giftDic = {givers[person]: recipients[person] for person in range(numAttend)}

        passList = {pwds[person]: pwd_givers[person] for person in range(numAttend)}

        base_logins_store.clear()
        giftDic_store.clear()

        base_logins_store.append(passList)
        giftDic_store.append(giftDic)

        client_ip = request.client.host
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log = os.open(os.path.join(log_path, f"{timestamp}. [OFFICIAL]. RESTORE-SECRET-SANTA"), os.O_WRONLY | os.O_CREAT)
        log_text = f"GIFT DIC: {giftDic}\nPASSWORDS: {passList}"
        os.write(log, log_text.encode())

        return giftDic, passList
    else:
        client_ip = request.client.host
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        log = os.open(os.path.join(log_path, f"{timestamp}. [UNAUTHORIZED ATTEMPT]. RESTORE-SECRET-SANTA"), os.O_WRONLY | os.O_CREAT)
        log_text = f"CLIENT IP: {client_ip}\nDATE: {timestamp}"
        os.write(log, log_text.encode())

        return await flyfool(request=request)