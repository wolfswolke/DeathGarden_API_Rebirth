# Updater

The Updater is a self writen Script that updates the Game modifications to the latest build.

In the future there will also be a in-game part that will show you when you need a update.

# 1. Script explained

## SET COMMANDS

``SET`` is used to set a name to with a value.

This is used, so you can for instance have a url and multiple paths and if you change the URL you only need to change it once

``%~dp0\`` This is a special Windows command that gets the path of the script.

It's used to get the current folder and to not have to search for DEATHGARDEN.

``%SYSTEMROOT%`` This variable is used to get the path of the Windows folder.

We need the powershell application to download the files and check the version.

This is also possible in CMD, but it's a lot more complicated.

## IF NOT EXIST

``IF NOT EXIST`` is used to check if a file or folder exists.

We use it 4 times.

1. Check if we are currently in the DEATHGARDEN folder
2. Check if the ``updater_versions`` folder exists
3. Check if the ``pak_version.txt`` file exists
4. Check if the ``sig_version.txt`` file exists

Between those we also use the ``SET`` command again to get the content of the ``pak_version.txt`` and ``sig_version.txt`` files.

We set those into the variables ``pak_version`` and ``sig_version`` for later use.

## CHOICE

``CHOICE`` As the name says you can CHOOSE something and depending on what you choose GOTO will be used to jump to a specific part of the script.

## GOTO

``GOTO`` is used to jump to a specific part of the script.

Anything that can be jumped to is marked with a ``:`` at the beginning. Like ``:FirstTimeSetup``

## POWER SHELL

The next 3 commands are the "brain" of the script.

1. Check if the script is up-to-date

``%power%`` anything after this will be run in PowerShell.

``[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;`` This is used to set the security protocol to TLS 1.2.

``$webRequest = Invoke-WebRequest https://api.zkwolf.com/updater/versions -UseBasicParsing;`` This is used to get the latest version from the API.

``$Data = ConvertFrom-Json $webRequest.Content;`` This is used to convert the JSON content to a PowerShell object.

``if ( $Data.script_version -gt '%updater_version%' ) {`` This is used to check if the script version is higher than the current version.

``'A new Version of this Script is available. Please download it here: ' + 'V-' + $Data.script_version + '.';`` This is used to show a message if a new version is available.

``echo 'https://api.zkwolf.com/updater/files/script';`` This is used to show the download link.

2. Check if the PAK file is up-to-date and if not download it

``%power% `` anything after this will be run in PowerShell.

``[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;`` This is used to set the security protocol to TLS 1.2.

``$webRequest = Invoke-WebRequest https://api.zkwolf.com/updater/versions -UseBasicParsing;`` This is used to get the latest version from the API.

``$Data = ConvertFrom-Json $webRequest.Content;`` This is used to convert the JSON content to a PowerShell object.

``$pak_version = '%pak_version%' -replace '\D', '';`` This is used to get the current version of the PAK file.

``if ( $Data.pak_version -gt $pak_version ) {`` This is used to check if the PAK file version is higher than the current version.

``'A new Version of the PAK File is available. Downloading it now: ' + 'V-' + $Data.pak_version + '.';`` This is used to show a message if a new version is available.

``Invoke-WebRequest '%download_url%pak/' -OutFile '%pak_folder%TheExitRebirthBackendAPI-WindowsNoEditor_P.pak';`` This is used to download the new PAK file.

3. Check if the SIG file is up-to-date and if not download it

`` %power% `` anything after this will be run in PowerShell.

``[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;`` This is used to set the security protocol to TLS 1.2.

``$webRequest = Invoke-WebRequest https://api.zkwolf.com/updater/versions -UseBasicParsing;`` This is used to get the latest version from the API.

``$Data = ConvertFrom-Json $webRequest.Content;`` This is used to convert the JSON content to a PowerShell object.

``$sig_version = '%sig_version%' -replace '\D', '';`` This is used to get the current version of the SIG file.

``if ( $Data.sig_version -gt $sig_version ) {`` This is used to check if the SIG file version is higher than the current version.

``'A new Version of the SIG File is available. Downloading it now: ' + 'V-' + $Data.sig_version + '.';`` This is used to show a message if a new version is available.

``Invoke-WebRequest '%download_url%sig/' -OutFile '%pak_folder%TheExitRebirthBackendAPI-WindowsNoEditor_P.sig';`` This is used to download the new SIG file.

## CLS

This is used to clear the console. (Clear means removing all text above)

## ECHO

This just shows a message in the console.

## PAUSE

This is used to pause the script, so you can read the messages.

## FirstTimeSetup

This is used to set up the game folder if you have never played the game.

It does these 3 things.

1. DELETE the Battleye folder
2. DELETE the TheExit_BE.exe file (This is the Battleye Launcher)
3. RENAME the TheExit.exe file to TheExit_BE.exe (This is done because steam opens this file when you click START.)

## RMDIR

This is used to delete a folder.

## DEL

This is used to delete a file.

## REN

This is used to rename a file.

# 2. How to use the Script

1. Download the script from GitHub
2. Put it into the DEATHGARDEN folder
3. Run the script