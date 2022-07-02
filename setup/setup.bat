@ECHO Starting setup . . .

set /p DiscordToken="Please enter your discord bot's token. "

echo "TOKEN=\"%DiscordToken%"">>../src/.env

