import random
import zipfile
import subprocess

# Input for names confirmation
check = input("Are the following names for GooglyBooglyz Secret Santa 2023 Correct?:\nJacob,Jared,Josh,Kai,Logan,Lucas,Hajin,David,Howin,Naoki [Y/N] ")

if check == "Y":
    print("Check Complete...Next Step...")
else:
    print("Modify Code and Try Again :(")
    exit()

givers = ["Jacob", "Jared", "Josh", "Kai", "Logan", "Lucas", "Hajin", "David", "Howin", "Naoki"]

approval = 'N'

# Loop for re-randomizing if not approved
while approval != 'Y':

    recipients = random.sample(givers, len(givers))
    print("Starting Randomization...")

    while any([giver == recipient for giver, recipient in zip(givers, recipients)]):
        recipients = random.sample(givers, len(givers))
        
    print("All Good! No One Matches Each Other!")
    secret_santa = list(zip(givers, recipients))
    
    # Display the pairs for approval
    for giver, recipient in secret_santa:
        print(f"{giver} -> {recipient}")
    
    approval = input("Do you approve of these matches? [Y/N]: ").upper()

print("Randomization Approved!")
print("Creating Directory...")

# Write the matches to files
for giver, recipient in secret_santa:
    filename = f"{giver}.txt"
    with open(filename, "w") as f:
        f.write(f"Your Person for Secret Santa is: {recipient}")

print("Directory is Complete")
print("You are Good To Go!")

# Generating Passcodes for Files
passcodes = {}

for name in givers:
    passcode = random.randint(1000, 9999)
    passcodes[name] = passcode

    zip_filename = f"{name}.zip"
    txt_filename = f"{name}.txt"
    
    subprocess.run(["7z", "a", "-p" + str(passcode), "-y", zip_filename, txt_filename])
    
    # Display the passcode for each name
    print(passcode, name)
