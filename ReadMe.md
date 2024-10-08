# DeathGarden Bloodharvest API Rebirth Project

# END OF LIFE NOTICE

This Project has stoped development and is no longer maintained.

This Project was taken over by Project Chronos with their own PHP backend.

This means that nothing will be updated anymore and the API is NOT hosted anymore on the known URL.

Thank you all for the time we had and the fun we had together.

If you want to see future work by me you can check on Project Rebirth here: https://projectrebirth.net

****
****
****

#  OLD README BELOW

*Quick jump [Setup](https://github.com/wolfswolke/DeathGarden_API_Rebirth?tab=readme-ov-file#usage)*

**Please note that this project is not affiliated with Behaviour Interactive or any other company.**

**This project is for educational purposes only!**


****

**Current Progress:**
- Logging (Stashboard, metrics, gameDataAnalytics) See [Logging.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Logging.md) for details.
- Steam login
- Load lobby
- Shop
- Messaging system
- Currency system
- Leveling at the end of the match
- Getting Currency at the end of the match
- Matchmaking via Steam P2P
- Leaderboard doesn't crash anymore
- GameNews (disabled atm because they mess InitOrGetGroup up)
- InitOrGetGroup (Challenges disabled atm see TODO)
- A lot of other features and endpoints (most of them keep the game from crashing)


**To-Do List:**

***Priority HIGH***
- Challenges (code is done already but needs testing)
- Private matches (Requires Dedicated Servers sadly)

***Priority MEDIUM***
- End-of-match endpoints (Show what you got at the end of the match)

***Priority LOW***
- Create a new catalog parser
- Dynamic leaderboards

For more detailed information about our project's tasks, please visit the [to-do page](https://github.com/users/wolfswolke/projects/2/views/1).

The goal of this project is to revive the Deathgarden backend and servers. 

**Contact Information:**
- ~

## Usage
 To find your Game folder right-click on Deathgarden in your Steam Library, hover over Manage and click on Browse Local Files.

0. If you do not already own Deathgarden, you can get it with this command: 
`steam://run/555440`

1. Download the [TheExit-Rebirth-Updater.bat](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/src/files/TheExit-Rebirth-Updater.bat) file and place it in the following directory: "\steamapps\common\DEATHGARDEN\"

2. Run the script and wait for it to finish. (RED TEXT means something went wrong!)

3. Follow the on-screen instructions.

4. IF your game does NOT start and you have a Intel CPU use this Launch Argument in steam: `cmd /c "set OPENSSL_ia32cap=:~0x20000000 && %command%" , -battleye`

**Self Hosting/Development Requirements:**
- Steam API Key (see [Steam_Login.md](https://github.com/wolfswolke/DeathGarden_API_Rebirth/blob/master/Doc/Steam_Login.md) for details).
- Python 3.10 (or newer).
- Install the requirements from `requirements.txt`.
- Create an api_config.yaml file (an example is available in the `src/config` folder).
- For request analysis, consider using Fiddler.
- You need mongo DB installed and running on your machine or your network. (Add the IP and Port in the Config file)
- You can use this Parameter to start the game. (You might need to change the IP):
* -ServiceApi=http://127.0.0.1:8080 -BackendUrl=http://127.0.0.1:8080 -CdnClientData=http://127.0.0.1:8080
