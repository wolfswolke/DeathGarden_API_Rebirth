
# DeathGarden Bloodharvest API Rebirth Project

This project is MORE than just a WIP!

The goal of this project is to revive the Deathgarden backend and servers.

If you have any old HTTP captures of the traffic between the game and server, please submit them here!

I am currently reverse-engineering the files to find all the API endpoints and requests.
Current knowledge

## Current knowledge

The game uses Unreal Engine 4.21.0.

The anticheat is Battleye.

The backend and server can be changed with start parameters.

The in-game console can be re-enabled.

The in-game SET command is available.

The "Status" API is Stashboard. Stashboard has been discontinued in 2019 but is only an HTTP POST, so I will recreate it.

The game server is the Amazon Gamelift SDK.

The steamAPI.dll cannot be spoofed because Battle Eye checks the signature.

If you have any information, suggestions, etc., please create an issue.

### Currently, known Endpoints and URLs

https://stashboard.live.tex.bhvronline.com  (Stashboard Open Source Status API)

https://latest.live.tex.bhvronline.com/api/v1/services/tex  ()

https://latest.live.tex.bhvronline.com/api/v1/gameDataAnalytics (Game Data Analytics)

https://latest.live.tex.bhvronline.com/api/v1/auth  (Steam Auth)

https://latest.live.tex.bhvronline.com/api/v1/healthcheck   (Keep Alive)

https://latest.live.tex.bhvronline.com/metrics  (Tells Server HTTP Codes and time for requests)

https://latest.live.tex.bhvronline.com/tex  ()
