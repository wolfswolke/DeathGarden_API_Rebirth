# DeathGarden Bloodharvest API Rebirth Project

**This project is Work in Progress! We already got far but there is still much to do so don't rush us please.**

**Current Progress:**
- Logging (Stashboard, Metrics, gameDataAnalytics) See [Logging.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Logging.md) for details.
- Steam Login
- Load Lobby
- Some items in the Shop
- Messaging System
- Currency System
- Matchmaking via Steam P2P
- Leaderboard doesn't crash anymore
- GameNews
- and alot of other things and Endpoints. (Most of them keep the game from crashing)

**To-Do List:**
- Fixing the Catalog crash (This is the most important thing!)
- InitOrGetGroup
- Dynamic Leaderboards
- Challenges
- Progression
- Buying items
- End of Match Endpoints

For more detailed information about our project's tasks, please visit the [ToDo page](https://github.com/users/wolfswolke/projects/2/views/1).

The goal of this project is to revive the Deathgarden backend and servers. 
If you have any knowledge about how the backend used to work or want to contribute, please reach out!
From what we know the Game was based on WH40KEC (Warhammer 40k Eternal Crusade) and some code was also used in DBD.

**Contact Information:**
- Matrix: @zkwolf:matrix.org
- Discord: sunywolf

## Usage

1. Download the [TheExit-Rebirth-Updater.bat](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/src/files/TheExit-Rebirth-Updater.bat) file and place it in the following directory: "\steamapps\common\DEATHGARDEN\"

2. Run the Script and wait for it to finish.

**Self Hosting/Development Requirements:**
- Steam API Key (See [Steam_Login.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Steam_Login.md) for details)
- Python 3.10 (or newer)
- Install the requirements from requirements.txt
- Create an api_config.yaml file (An example is available in the Config folder)
- For request analysis, consider using Fiddler

**Current Knowledge:**
- The game uses Unreal Engine 4.21.0.
- The anticheat is Battleye (Note: Windows 11 blocks vulnerable drivers).
- The newest game version is: te-18f25613-36778-ue4-374f864b (Versions may vary by region).
- The backend and server can be changed with start parameters (new method with the PAK file).
- The in-game console can be re-enabled.
- The in-game SET command is available.
- The "Status" API is Stashboard, which has been discontinued in 2019.
- Fluentd was used for logging.
- The game server uses the Amazon Gamelift SDK (We are now using P2P).
- The steamAPI.dll cannot be spoofed because Battleye checks the signature. (We have a Battleye emulator)
- There is an API Key that is currently not used by the game.
- The authentication is done cia the bhvrSession Cookie. See [bhvrSession.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/bhvrSession.md) for details.

**Currently, Known Endpoints and URLs:**
- This information will be reworked into a Wiki page for more detailed reference.
