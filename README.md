# Packages
Linux Debian is the repository of package files for the new YAPI cross-platform rewrite by [IanDuncanT](https://github.com/IanDuncanT).

****

## Badges

| LICENSE | Rewrite |
|---------|---------|
| [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)| [![Rewrite: Project](https://img.shields.io/badge/Rewrite-Project-green.svg)](https://github.com/YetAnotherPackageInstaller/rewrite) |

****

## Packages
The packages supported include:
<!--readme_update start -->
- Dropbox - Dropbox cloud storage - https://www.dropbox.com/
- Googlechrome - Google Chrome browser - https://www.google.it/chrome/
- Ideacom - IntelliJ IDEA Community edition - https://www.jetbrains.com/idea/
- Skype - Skype for linux instant chat and VoIP - https://www.skype.com/
- Javajdk11 - Java jdk 11 with path setup - https://www.oracle.com/technetwork/java/javase/downloads/index.html
- Spotify - Spotify client music for all - https://www.spotify.com
- Rambox - Rambox workspace browser - https://rambox.pro
- Virtualbox - VirtualBox is a general-purpose full virtualizer for x86 hardware - https://www.virtualbox.org
- Oh-my-zsh - zsh + oh-my-zsh - https://ohmyz.sh/
- Eclipseinstaller - Eclipse IDE installer - https://www.eclipse.org/
- Steam - Steam ultimate entertainment platform - https://store.steampowered.com/about
- Atom - Atom Text Editor - https://atom.io/
- Playerctl - Playerctl command-line controller and library - https://github.com/acrisci/playerctl
- Light - Light GNU/Linux application to control backlights - http://haikarainen.github.io/light
- Gitkraken - GitKraken Git Client and Glo Boards to build epic software - https://www.gitkraken.com/
- Mailspring - The best mail client - https://getmailspring.com/
- Discord - Discord chat vocale e testuale - https://discordapp.com/
- Nodejs - NodeJs JavaScript runtime - https://github.com/nodesource/distributions#installation-instructions
- Pycharmcom - Pycharm Community edition - https://www.jetbrains.com/pycharm/
- Nvidiadriver - NVIDIA driver support of Geforce 4xx and higher GPUs - https://wiki.debian.org/NvidiaGraphicsDrivers
<!--readme_update end -->

## How to add new script

There is a format for the install scripts:

    # <description of package> - <reference site of package>
    <bash commands>

An example of this format is [test.sh](scripts/test.sh):

    # Description of package - https://github.com/YetAnotherPackageInstaller/packages
    echo "Hello world!"

If you want to add one script you **need** to maintain this standard. This is because the packages list is generated with this information, taken directly from the scripts.

****

## How To Contribute

Contributions are always welcome, either reporting issues/bugs or forking the repository and then issuing pull requests when you have completed some additional coding that you feel will be beneficial to the main project. If you are interested in contributing in a more dedicated capacity, then please contact us.

****

## License

YAPI source code is released under the MIT License. Please see [LICENSE](LICENSE) for complete licensing information.

****

## Contributors:

[Wabri](https://github.com/Wabri), [IanDuncanT](https://github.com/IanDuncanT)
