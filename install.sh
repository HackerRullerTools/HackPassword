#!/usr/bin/bash
pathFile="HackPassword" 
pkg install python
cd ~/../usr/bin 
# команда
touch HackPassword
echo "cd ~/$pathFile/ && python HackPassword.py" >  HackPassword
chmod +x HackPassword
cd ~/
#конец
