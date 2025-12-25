#!/bin/bash

# Made with Love
GREEN='\033[0;32m'
NC='\033[0m' 

echo -e "${GREEN}Starting installation of Ubuntu Error Identifier...${NC}"


echo "Checking requirements..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt update -y && sudo apt install -y python3
else
    echo "Python3 is already installed."
fi


echo "Installing main script..."
if [ -f "error_explainer.py" ]; then
  
    sudo cp error_explainer.py /usr/local/bin/er-iden
    sudo chmod +x /usr/local/bin/er-iden
    echo -e "${GREEN}Main command 'er-iden' installed.${NC}"
else
    echo "CRITICAL ERROR: error_explainer.py not found in current directory."
    exit 1
fi

echo "Creating short alias 'ei'..."
echo '#!/bin/bash' | sudo tee /usr/local/bin/ei > /dev/null
echo 'python3 /usr/local/bin/er-iden "$@"' | sudo tee -a /usr/local/bin/ei > /dev/null
sudo chmod +x /usr/local/bin/ei
echo -e "${GREEN}Shortcut 'ei' created.${NC}"

echo "------------------------------------------------"
echo -e "${GREEN}Installation Complete!${NC}"
echo "Usage:"
echo "  1. Long command:  er-iden <error>"
echo "  2. Short command: ei <error>"
echo "------------------------------------------------"
