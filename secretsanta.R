Check <- readline(prompt = "Are the following names for GooglyBooglyz Secret Santa 2022 Correct?:
                   Jacob,Jared,Josh,Kai,Logan,Lucas,Hajin,David,Howin [Y/N]")

if(Check == "Y") {
  print("Check Complete...Next Step...")
} else {
  print("Modify Code and Try Again :(")
}

Givers <- c("Jacob,Jared,Josh,Kai,Logan,Lucas,Hajin,David,Howin")
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
    Recipients <- sample(Recipients)
  }else{
    print("All Good! No One Matches Each Other!")
    Complete <- 1
  }
  
if(Complete == 1) {
  
    break
  }
}

Complete2 <- 0

repeat{
  
  if(Recipients[1] == "Howin"
         && Recipients[2] == "Hajin"
         && Recipients[3] == "Jared"
         && Recipients[4] == "Jacob"
         && Recipients[5] == "Lucas"
         && Recipients[7] == "Kai"
         && Recipients[9] == "Logan") {
    print("Error Encountered!")
    print("Fixing Real Quick")
    Recipients <- sample(Recipients)
  }else{
    print("All Good! No One Got Each Other From Last Year!")
    Complete2 <- 1
  }
  
  if(Complete2 == 1) {
    
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

print("You are Good To Go!")
