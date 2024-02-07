@echo off
setlocal enabledelayedexpansion

TITLE The Exit Rebirth Updater

set version_url=https://api.zkwolf.com/updater/version/pak
set download_url=https://api.zkwolf.com/updater/files/
set "path_value=%~dp0\"
set "pak_folder=%path_value%TheExit\Content\Paks\"
set "updater_versions_folder=%path_value%updater_versions\"
set "updater_version=1"
set "pak_Version=0"
set "sig_version=0"
set "power=%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command"

if not exist "%~dp0\TheExit\" (
    echo The Script is not in the DEATHGARDEN Folder. Please move it there and start it again.
    exit
)

if not exist "%updater_versions_folder%" (
    mkdir "%updater_versions_folder%"
)

if not exist "%updater_versions_folder%pak_version.txt" (
    echo %pak_Version% > "%updater_versions_folder%pak_version.txt"
    set /p pak_Version=<"%updater_versions_folder%pak_version.txt"
)
set /p pak_Version=<"%updater_versions_folder%pak_version.txt"

if not exist "%updater_versions_folder%sig_version.txt" (
    echo %sig_Version% > "%updater_versions_folder%sig_version.txt"
    set /p sig_Version=<"%updater_versions_folder%sig_version.txt"
)
set /p sig_Version=<"%updater_versions_folder%sig_version.txt"

rem Check Script Version
%power% "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webRequest = Invoke-WebRequest https://api.zkwolf.com/updater/versions -UseBasicParsing; $Data = ConvertFrom-Json $webRequest.Content; if ( $Data.script_version -gt '%updater_version%' ) { 'A new Version of this Script is available. Please download it here: ' + 'V-' + $Data.script_version + '.'; echo 'https://api.zkwolf.com/updater/files/script/'; '' } }"

REM Check Pak Version and Download if newer
%power% "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webRequest = Invoke-WebRequest https://api.zkwolf.com/updater/versions -UseBasicParsing; $Data = ConvertFrom-Json $webRequest.Content; $pak_version = '%pak_version%' -replace '\D', ''; if ( $Data.pak_version -gt $pak_version ) { 'A new Version of the PAK File is available. Downloading it now: ' + 'V-' + $Data.pak_version + '.'; Invoke-WebRequest '%download_url%pak/' -OutFile '%pak_folder%TheExitRebirthBackendAPI-WindowsNoEditor_P.pak'; } echo $Data.pak_version > '%updater_versions_folder%pak_version.txt'; ' '}"

REM Check SIG Version and Download if newer
%power% "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webRequest = Invoke-WebRequest https://api.zkwolf.com/updater/versions -UseBasicParsing; $Data = ConvertFrom-Json $webRequest.Content; $sig_version = '%sig_version%' -replace '\D', ''; if ( $Data.sig_version -gt $sig_version ) { 'A new Version of the SIG File is available. Downloading it now: ' + 'V-' + $Data.sig_version + '.'; Invoke-WebRequest '%download_url%sig/' -OutFile '%pak_folder%TheExitRebirthBackendAPI-WindowsNoEditor_P.sig'; } echo $Data.sig_version > '%updater_versions_folder%sig_version.txt'; ' '}"

echo Finished Update. You can now exit this Updater.
pause
