# DeathGarden Bloodharvest API Rebirth Project

*Quick jump [Setup](https://github.com/wolfswolke/DeathGarden_API_Rebirth?tab=readme-ov-file#usage)*

**This project is a work in progress! That means there are bugs!**

**In its current state, you can play, and most features have been implemented. 
For info about missing features, check out the [to-do page](https://github.com/users/wolfswolke/projects/2/views/1).**

**Please note that this project is not affiliated with Behaviour Interactive or any other company.**

**This project is for educational purposes only!**

**This Repository will probably not be updated a lot anymore because 
Project Chronos started to work on their own backend in PHP.**

****

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
- InitOrGetGroup (Challenges disabled atm see TODO)
- A lot of other features and endpoints (most of them keep the game from crashing)


**To-Do List:**
- Create a new catalog parser
- Dynamic leaderboards
- Challenges (code is done already but needs rework)
- Progression (leveling, currency, end of match, etc.)
- Private matches (Requires Dedicated Servers sadly)
- End-of-match endpoints

For more detailed information about our project's tasks, please visit the [to-do page](https://github.com/users/wolfswolke/projects/2/views/1).

The goal of this project is to revive the Deathgarden backend and servers. 

**Contact Information:**
- Matrix: @zkwolf:matrix.org
- Discord: sunywolf

## Usage

0. If you do not already own Deathgarden, you can get it with this command: 
`steam://run/555440`

1. Download the [TheExit-Rebirth-Updater.bat](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/src/files/TheExit-Rebirth-Updater.bat) file and place it in the following directory: "\steamapps\common\DEATHGARDEN\"

2. Run the script and wait for it to finish. (RED TEXT means something went wrong!)

**Self Hosting/Development Requirements:**
- Steam API Key (see [Steam_Login.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Steam_Login.md) for details).
- Python 3.10 (or newer).
- Install the requirements from `requirements.txt`.
- Create an api_config.yaml file (an example is available in the `src/config` folder).
- For request analysis, consider using Fiddler.
