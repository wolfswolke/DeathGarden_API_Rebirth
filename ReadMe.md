
# DeathGarden Bloodharvest API Rebirth Project

This project is MORE than just a WIP!

Current Progress: Logging (Stashboard, Metrics, gameDataAnalytics), Steam Login, Load 
Lobby, Some items in the Shop, Messaging System, Currency System, MatchMaking implemented and some smaller things,
 Leaderboard doesn't crash anymore.

ToDo: InitOrGetGroup, dynamic Leaderboards, Challenges, Progression, buying things, Fixing the Catalog crash. 

For more Info go to the [ToDo page.](https://github.com/users/wolfswolke/projects/2/views/1)

The goal of this project is to revive the Deathgarden backend and servers.

If you have any knowledge on how the backend used to work or want to help
please reach out!

Matrix: @zkwolf:matrix.org
Discord: sunywolf

## Usage

Download the [TheExitRebirthBackendAPI-WindowsNoEditor_P.pak](https://github.com/wolfswolke/DeathGarden_API_Rebirth/tree/master/src/files/TheExitRebirthBackendAPI-WindowsNoEditor_P.pak)
File and place it here: "DEATHGARDEN\TheExit\Content\Paks\"

Then make a copy of TheExit-WindowsNoEditor.sig and rename it to TheExitRebirthBackendAPI-WindowsNoEditor_P.sig
You should then have the following files in the folder:
```
TheExitRebirthBackendAPI-WindowsNoEditor_P.pak
TheExitRebirthBackendAPI-WindowsNoEditor_P.sig
TheExit-WindowsNoEditor.pak
TheExit-WindowsNoEditor.sig
```

# Self hosting/Developing

You will need a steam API Key. [See Steam_Login.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Steam_Login.md)

Python 3.10 (or newer)

Install the requirements.txt

Create a api_config.yaml (Example is in the Config folder)

You can use Fiddler for request analysis.

A Debug Version of the Game and PDB File is available on request.

## Current knowledge

The game uses Unreal Engine 4.21.0.

The anticheat is Battleye. (Windows 11 blocks vulnerable drivers. So at the time of writing you cant play on W11)

The newest game Version is: te-18f25613-36778-ue4-374f864b (For some Reason this is not 100% true because different Regions have different Versions???)

The backend and server can be changed with start parameters. (New way with the PAK File)

The in-game console can be re-enabled.

The in-game SET command is available.

The "Status" API is Stashboard. Stashboard has been discontinued in 2019.

The game server is the Amazon Gamelift SDK. (Can Potentially be done with Steam P2P)

The steamAPI.dll cannot be spoofed because Battle Eye checks the signature.

There is a API Key which is NOT used by the game.

### Currently, known Endpoints and URLs

This Info will be reworked into a Wiki page.