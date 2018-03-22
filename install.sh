#!/bin/bash

read -p "Waiting for installation scripts   [ Encypt Decrypt Decrypt2 ] " -t 4
chmod +x Decrypt2.py Decrypt.py Encrypt.py geturl.py wordlist.py
mv Decrypt2.py /usr/bin/
mv Decrypt.py /usr/bin/
mv Encrypt.py /usr/bin/
mv geturl.py /usr/bin/
mv wordlist.py /usr/bin/

alias Decrypt2='python3 /usr/bin/Decrypt2.py'
alias Decrypt='python /usr/bin/Decrypt.py'
alias Encrypt='python /usr/bin/Encrypt.py'
alias geturl='python /usr/bin/geturl.py'
alias wlist='python3 /usr/bin/wordlist.py'


echo "alias Decrypt2='python3 /usr/bin/Decrypt2.py'" >> /etc/bash.bashrc
echo "alias Decrypt='python /usr/bin/Decrypt.py'" >> /etc/bash.bashrc
echo "alias Encrypt='python /usr/bin/Encrypt.py'"  >> /etc/bash.bashrc
echo "alias geturl='python /usr/bin/geturl.py'"  >> /etc/bash.bachrc
echo "alias wlist='python3 /usr/bin/wordlist.py'"  >> /etc/bash.bachrc



clear
exit
