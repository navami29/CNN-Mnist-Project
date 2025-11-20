echo "A script to create, activate and install requiremnet.txt"
echo "......."

virtualenv venv

echo "Creation of Virtualenv done..."
echo "activation my env"

source venv/bin/activate

echo "......."

echo "install requiremnet.txt"
pip install -r requirement.txt

sleep(2)
echo "install done"
echo "Creation Activation and install of library done"


