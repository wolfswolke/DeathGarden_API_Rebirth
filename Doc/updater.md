# Updater WIP DOC!

The Updater is a self writen Script that updates the Game modifications to the latest build.

In the future there will also be a in-game part that will show you when you need a update.

# 1. Script explained

## 1.1 Script Part X


# 2. Endpoints

These Endpoints are used by the updater to download its files, check for newer versions,...

ROOT: /updater/

## 2.1 /updater/version/*
Type: GET

Response Type: JSON

Example: {"version": 1}

Description: Used to check for newer Versions.

### 2.1.1 Sub-Endpoints
/script

/pak

/sig

## 2.2 /updater/files/*
Type: GET

Response: FILE

Description: Used for downloading Files.

### 2.2.1 Sub-Endpoints
/script

/pak

/sig

# 3. In-Game Part

What it does

How its done