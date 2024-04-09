# DeathGarden Bloodharvest API Rebirth Project

**This project is a work in progress! That means there are bugs!**

**In its current state you can play, and most features are implemented. For info about missing features, check out the [to-do page](https://github.com/users/wolfswolke/projects/2/views/1).**

****

**Current Progress:**
- Logging (Stashboard, metrics, gameDataAnalytics) See [Logging.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Logging.md) for details.
- Steam login
- Load lobby
- Shop
- Messaging system
- Currency system
- Matchmaking via Steam P2P
- Leaderboard doesn't crash anymore
- GameNews (disabled atm because they mess InitOrGetGroup up)
- InitOrGetGroup
- A lot of other features and endpoints (most of them keep the game from crashing)


**To-Do List:**
- Create a new catalog parser
- Dynamic leaderboards
- Challenges (code is done already but needs rework)
- Progression (leveling, currency, end of match, etc.)
- Private matches
- End-of-match endpoints

For more detailed information about our project's tasks, please visit the [to-do page](https://github.com/users/wolfswolke/projects/2/views/1).

The goal of this project is to revive the Deathgarden backend and servers. 
If you have any knowledge about how the backend used to work or want to contribute, please reach out!
From what we know the game was based on WH40KEC (Warhammer 40k Eternal Crusade) and some code was also used in DBD.

**Contact Information:**
- Matrix: @zkwolf:matrix.org
- Discord: sunywolf

## Usage

0. If you do not already own Deathgarden, you can get it with this command: 
`steam://run/555440`

1. Download the [TheExit-Rebirth-Updater.bat](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/src/files/TheExit-Rebirth-Updater.bat) file and place it in the following directory: "\steamapps\common\DEATHGARDEN\"

2. Run the script and wait for it to finish.

**Self Hosting/Development Requirements:**
- Steam API Key (see [Steam_Login.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Steam_Login.md) for details).
- Python 3.10 (or newer).
- Install the requirements from `requirements.txt`.
- Create an api_config.yaml file (an example is available in the `src/config` folder).
- For request analysis, consider using Fiddler.

**Current Knowledge:**
- The game uses Unreal Engine 4.21.0.
- The anticheat is BattlEye (note: Windows 11 blocks vulnerable drivers).
- The newest game version is: te-18f25613-36778-ue4-374f864b (versions may vary by region).
- The backend and server can be changed with start parameters (new method with the PAK file).
- The in-game console can be re-enabled.
- The in-game SET command is available.
- The "Status" API is Stashboard, which has been discontinued since 2019.
- Fluentd was used for logging.
- The game server uses the Amazon GameLift SDK (we are now using P2P).
- The steam_api.dll cannot be spoofed because Battleye checks the signature. (we have a Battleye emulator)
- There is an API key that is currently not used by the game.
- The authentication is done via the bhvrSession Cookie. See [bhvrSession.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/bhvrSession.md) for details.

**Currently Known Endpoints and URLs:**
- This information will be reworked into a wiki page for more detailed reference.
