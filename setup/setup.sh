echo "Starting setup . . ."

echo "Please enter your discord token."
read token
echo "TOKEN=\"$token\"">>../src/.env

echo
echo "Installing dependencies . . ."
pip install --user discord==1.7.3
pip install --user python-dotenv==0.19.0
pip install --user toml==0.10.2