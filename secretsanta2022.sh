#!/bin/bash

# Navigating to Directory on System
# and Running R Script

cd ~/R/secretsanta/

Rscript secretsanta.R

# Generating Passcodes for Files

Jacob=$[ $RANDOM % 9999 + 1000 ]
Jared=$[ $RANDOM % 9999 + 1000 ]
Josh=$[ $RANDOM % 9999 + 1000 ]
Kai=$[ $RANDOM % 9999 + 1000 ]
Logan=$[ $RANDOM % 9999 + 1000 ]
Lucas=$[ $RANDOM % 9999 + 1000 ]
Hajin=$[ $RANDOM % 9999 + 1000 ]
David=$[ $RANDOM % 9999 + 1000 ]
Howin=$[ $RANDOM % 9999 + 1000 ]

# Zipping and Encrypting Files

zip -P $Jacob Jacob.zip Jacob.txt
zip -P $Jared Jared.zip Jared.txt
zip -P $Josh Josh.zip Josh.txt
zip -P $Kai Kai.zip Kai.txt
zip -P $Logan Logan.zip Logan.txt
zip -P $Lucas Lucas.zip Lucas.txt
zip -P $Hajin Hajin.zip Hajin.txt
zip -P $David David.zip David.txt
zip -P $Howin Howin.zip Howin.txt

echo $Jacob Jacob
echo $Jared Jared
echo $Josh Josh
echo $Kai Kai
echo $Logan Logan
echo $Lucas Lucas
echo $Hajin Hajin
echo $David David
echo $Howin Howin
