echo 'Initializing...'
sudo apt -y install python3 python3.10-venv figlet > /dev/null 2>&1

figlet 'Welcome to ConvergeCast Installation'
read x

python3 -m pip install --upgrade pip
python3 -m venv venv 
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt