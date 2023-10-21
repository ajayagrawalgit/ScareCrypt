#!/bin/bash
clear;
echo -e "

░██████╗░█████╗░░█████╗░██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
░╚═══██╗██║░░██╗██╔══██║██╔══██╗██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██████╔╝╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
A CROSS-PLATFORM SYMMETRIC ENCRYPTION AND DECRYPTION TOOL FOR ALL KINDS OF FILES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Read the Complete Document on: https://github.com/ajayagrawalgit/ScareCrypt
Support Me On: https://www.buymeacoffee.com/ajayagrawal

Cheers 🥂

"


PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>&1)
if [ -n "$PYTHON_VERSION" ] && [ "$(echo "$PYTHON_VERSION" | awk -F. '{ printf("%03d%03d%03d\n", $1,$2,$3); }')" -lt "$(echo '3.11.2' | awk -F. '{ printf("%03d%03d%03d\n", $1,$2,$3); }')" ]; then
  echo "Upgrading to Python 3.11.2"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install python@3.11
  elif [[ -f /etc/redhat-release ]]; then
    # RHEL/CentOS
    sudo yum update -y
    sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    sudo yum install -y python3.11
  else
    # Debian/Ubuntu
    sudo apt-get update
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install -y python3.11
  fi
else
  echo "Python version is already up to date"
fi


# Install required packages
echo "Installing required packages"
pip3 install -r requirements.txt
if [[ $? -ne 0 ]]; then
  echo "Failed to install required packages"
  exit 1
fi

sleep 2


echo -e "$(date): Performing some cleanup before starting ..."
if [ -d "/usr/local/lib/ScareCrypt" ]; then
    echo "Older verion of ScareCrypt found. Removing it..."
    rm -r "/usr/local/lib/ScareCrypt"
fi

if [ -L "/usr/local/bin/scarecrypt" ]; then
    echo "Removing the softlinks as well..."
    rm -f "/usr/local/bin/scarecrypt"
fi

echo -e "Cleanup Completed !"

sleep 2

echo -e "$(date): \n\nCopying Libraries Now..."
mkdir /usr/local/lib/ScareCrypt
cp -r * /usr/local/lib/ScareCrypt/.
echo -e "$(date): \n\nLibraries Copied..."

sleep 2

echo -e "\n\n$(date): \n\nMaking the library accessible accross terminal now..."
ln -s /usr/local/lib/ScareCrypt/src/scarecrypt.sh /usr/local/bin/scarecrypt
chmod -R 755 /usr/local/lib/ScareCrypt*

sleep 4

echo -e "\n$(date): ScareCrypt Installed Successfullly\nTry running this command -> scarecrypt\nAnd then you'll be able to understand the rest where to take it forward from there 😉\n\nAll the best 🔥\n"