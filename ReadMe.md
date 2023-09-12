# DeathGarden Bloodharvest API Rebirth Project

**This project is more than just a Work in Progress (WIP)!**

**Current Progress:**
- Logging (Stashboard, Metrics, gameDataAnalytics) See [Logging.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Logging.md) for details.
- Steam Login
- Load Lobby
- Some items in the Shop
- Messaging System
- Currency System
- Matchmaking implemented
- Leaderboard doesn't crash anymore

**To-Do List:**
- InitOrGetGroup
- Dynamic Leaderboards
- Challenges
- Progression
- Buying items
- Fixing the Catalog crash

For more detailed information about our project's tasks, please visit the [ToDo page](https://github.com/users/wolfswolke/projects/2/views/1).

The goal of this project is to revive the Deathgarden backend and servers. If you have any knowledge about how the backend used to work or want to contribute, please reach out!

**Contact Information:**
- Matrix: @zkwolf:matrix.org
- Discord: sunywolf

## Usage

1. Download the [TheExitRebirthBackendAPI-WindowsNoEditor_P.pak](https://github.com/wolfswolke/DeathGarden_API_Rebirth/tree/master/src/files/TheExitRebirthBackendAPI-WindowsNoEditor_P.pak) file and place it in the following directory: "DEATHGARDEN\TheExit\Content\Paks\"

2. Make a copy of TheExit-WindowsNoEditor.sig and rename it to TheExitRebirthBackendAPI-WindowsNoEditor_P.sig. Your folder should contain the following files:
   - TheExitRebirthBackendAPI-WindowsNoEditor_P.pak
   - TheExitRebirthBackendAPI-WindowsNoEditor_P.sig
   - TheExit-WindowsNoEditor.pak
   - TheExit-WindowsNoEditor.sig

**Self Hosting/Development Requirements:**
- Steam API Key (See [Steam_Login.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Steam_Login.md) for details)
- Python 3.10 (or newer)
- Install the requirements from requirements.txt
- Create an api_config.yaml file (An example is available in the Config folder)
- For request analysis, consider using Fiddler
- A debug version of the game and PDB file is available upon request.

**Current Knowledge:**
- The game uses Unreal Engine 4.21.0.
- The anticheat is Battleye (Note: Windows 11 blocks vulnerable drivers).
- The newest game version is: te-18f25613-36778-ue4-374f864b (Versions may vary by region).
- The backend and server can be changed with start parameters (new method with the PAK file).
- The in-game console can be re-enabled.
- The in-game SET command is available.
- The "Status" API is Stashboard, which has been discontinued in 2019.
- The game server uses the Amazon Gamelift SDK (Potential use of Steam P2P).
- The steamAPI.dll cannot be spoofed because Battleye checks the signature.
- There is an API Key that is currently not used by the game.
- The authentication is done cia the bhvrSession Cookie. See [bhvrSession.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/bhvrSession.md) for details.

**Currently Known Endpoints and URLs:**
- This information will be reworked into a Wiki page for more detailed reference.
