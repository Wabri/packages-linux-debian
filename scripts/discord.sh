# Discord chat vocale e testuale - https://discordapp.com/
sudo apt install libgconf-2-4 libappindicator1
wget -O discord.deb https://discordapp.com/api/download?platform=linux&format=deb
sudo dpkg -i discord.deb
rm -r discord.deb
