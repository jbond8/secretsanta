# GooglyBooglyz Secret Santa 2025  

backend: python (fastapi)  
frontend: html/css  

the backend uses fastapi, treating each program function as an api call.  

on initial launch, fastapi generates a random admin password. this password is not stored or saved—it's up to the admin to keep it safe.  

the setup allows a designated administrator to call the api to generate:  
1. a list of random givers and recipients  
2. a list of passwords  

the api ensures no one is matched to themselves, then outputs `.txt` files with the assignments.  

admins can also restore giver/recipient and password lists if fastapi goes down.  

~the end~  

p.s. don’t ask me to explain everything lol  