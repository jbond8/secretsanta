Givers <- readline(prompt = 'Enter the names of the people particpating in secret santa divided by a " , " :')

Givers <- strsplit(Givers,",")
Givers <- unlist(Givers)
Givers <- gsub(' ',"",Givers)

Recipients <- sample(Givers)
Complete <- 0

print("Starting Randomization...")

repeat{
  
  if(any(Givers == Recipients)) {
    print("Error Encountered!")
    print("Fixing Real Quick")
    Givers <- sample(Givers)
  }else{
    print("All Good!")
    Complete <- 1
  }
  
if(Complete == 1) {
  
    break
  }
}

print("Randomization Complete")
print("Creating Directory...")

SecretSanta <- data.frame(Givers, Recipients)
colnames(SecretSanta) <- c("Givers", "Recipients")

x <- 2
y <- 1
x_while <- 0
while(x_while < 9) {
  
R <- paste("Your Person for Secret Santa is:", SecretSanta[y,x])
FileName <- paste(SecretSanta[y,1],".txt")
FileName <- gsub(' ',"",FileName)
write.table(R, file = FileName, col.names = FALSE, row.names = FALSE)

y <- y + 1
x_while <- x_while + 1
  
}

print("Directory is Complete")

print("Starting Passwords...")

PasswordList <- data.frame(Givers, Recipients)
colnames(SecretSanta) <- c("Person", "Password")

x <- 2
y <- 1
x_while <- 0

while(x_while < 9) {
  
  Pass <- sample(sample(1:9), size = 4)
  Pass <- toString(Pass)
  Pass <- gsub(',',"",Pass)
  
  PasswordList[y,x] <- Pass
  
  y <- y + 1
  x_while <- x_while + 1
  
}
print("Passwords Complete!")
print("You are Good To Go!")