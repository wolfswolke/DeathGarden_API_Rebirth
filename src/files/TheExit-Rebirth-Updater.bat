@echo off
setlocal enabledelayedexpansion

TITLE The Exit Rebirth Updater

set version_url=http://localhost:8080/updater/version/pak
set download_url=http://localhost:8080/updater/files/pak
set path_value=C:\tmp\

if not exist "updater_versions" (
    mkdir "updater_versions"
)

if not exist "updater_versions\pak_version.txt" (
    echo 0 > "updater_versions\pak_version.txt"
)

for /f %%i in ('type "updater_versions\pak_version.txt"') do set current_version=%%i

for /f %%i in ('powershell -command "(Invoke-WebRequest '%version_url%' -UseBasicParsing).Content | ConvertFrom-Json"') do (
    set json_version=%%i
)

if %json_version% gtr %current_version% (
    echo Updating...

    powershell -command "Invoke-WebRequest '%download_url%' -OutFile '%path_value%\pak'"

    echo %json_version% > "updater_versions\pak_version.txt"
    echo Update complete.
) else (
    echo No update required.
)

pause
