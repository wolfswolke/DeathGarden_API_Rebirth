## Steam Login

Steam Login can be send to XXX
It works by sending a Steam Session Ticket to the server, which then sends it to Steam to verify it. If it is valid, the server will 

You then Get this back:

`{"preferredLanguage":"en","friendsFirstSync":{"steam":true},"fixedMyFriendsUserPlatformId":{"steam":true},"id":"xx000x00-x000-00x0-x0xx-x0000000000x","provider":{"providerId":"00000000000000000","providerName":"steam","userId":"xx000x00-x000-00x0-x0xx-x0000000000x"},"providers":[{"providerName":"steam","providerId":"00000000000000000"}],"friends":[],"triggerResults":{"success":[],"error":[]},"tokenId":"0x0000x0-00x0-0xxx-00x0-x00x0x000x0x","generated":1686004631,"expire":1686091031,"userId":"xx000x00-x000-00x0-x0xx-x0000000000x","token":"0x0000x0-00x0-0xxx-00x0-x00x0x000x0x"}`


# Explanation:

preferredLanguage = Steam Language

providerId = Steam ID (See SteamDB)

id = Unknown

userId = Unknown

tokenId = Unknown

# Workaround

Thanks to Layles DBD Api Doc and script you can manually get the connection json.

If you past that as the return Value in AUTH the Game loads you into the hub.

Source: https://layle.me/posts/authenticating-via-sessiontickets-dbd/ (Thanks to Layle)