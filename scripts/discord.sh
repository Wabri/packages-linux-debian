# Discord voice and text chat - https://discordapp.com/ - chat
sudo apt install libgconf-2-4 libappindicator1
wget -O discord.deb https://discordapp.com/api/download?platform=linux&format=deb
sudo dpkg -i discord.deb
rm -r discord.deb
