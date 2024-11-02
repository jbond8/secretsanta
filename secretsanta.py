import random

def secretsanta():
    """
    Takes the people attending a secret santa event, and assigns reciepients to givers for the event.

    Returns a dictionary of givers -> recipients and a dictionary of passwords for retrieving recipient
    """
    numAttend = int(input("How many people attending this year?: "))

    givers = [input(f"Who is person {person + 1}?: ") for person in range(numAttend)]

    recipients = random.sample(givers, len(givers))

    for person in range(numAttend):
        if givers[person] == recipients[person]:
            print(f"Match Found {givers[person]} and {recipients[person]}")
            recipients = random.sample(givers,len(givers))

    giftDic = {givers[person]: recipients[person] for person in range(numAttend)}

    passList = {int(random.randrange(1000, 9999)): givers[person] for person in range(numAttend)}

    for giver in giftDic:
        print(f"{giver}'s person for secret santa is {giftDic[giver]}")
        
    return giftDic, passList

def passcheck(results):
    """
    Takes an attempted password and provides reciepient aligned with password.
    If password fails, it results in an invalid password.
    """
    attemptpass = int(input("What's your password?: "))
    if attemptpass in results[1]:
        print(f"Your person is: {results[0][results[1][attemptpass]]}")
    else:
        print("Invalid Password")

results = secretsanta()
print(results)
passcheck(results)