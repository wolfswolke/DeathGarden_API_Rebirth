# Logging

Deathgarden has alot of logging data that is sent to the backend. This data is sent to the backend via HTTP POST requests.

Most of the Data is sent to: https://stashboard.live.tex.bhvronline.com

But some data is also sent to: https://latest.live.tex.bhvronline.com

# Endpoints

/metrics/client/event

/metrics/httplog/event

/api/v1/gameDataAnalytics

/api/v1/gameDataAnalytics/batch

/api/v1/extensions/quitters/getQuitterState

/api/v1/extensions/progression/initOrGetGroups

/api/v1/me/richPresence

/moderation/check/username

/metrics/server/event

# Collected Logging data:

This data is all the collected data from starting the game until loading the Lobby and also the errors that were 
patched.

```json
{
  "body": [
    {
      "timestamp": 1686251652,
      "eventType": "gm_session_started",
      "eventTypeVersion": 1,
      "userId": "<user_id>",
      "eventId": "<event_id>",
      "data": {
        "event_id": "<event_id>",
        "event_type": "gm_session_started",
        "event_time": "2023-06-08T19:14:12.184Z",
        "event_order": 1,
        "session_id": "<session_id>"
      }
    },
    {
      "timestamp": 1686251667,
      "eventType": "gm_session_ended",
      "eventTypeVersion": 1,
      "userId": "<user_id>",
      "eventId": "<event_id>",
      "data": {
        "event_id": "<event_id>",
        "event_type": "gm_session_ended",
        "event_time": "2023-06-08T19:14:27.978Z",
        "event_order": 2,
        "session_id": "<session_id>"
      }
    }
  ]
}
```
```json
{
  "playerUniqueId": "<userid>",
  "clientEvent": "Disconnected",
  "eventType": "Server"
}
```
```json
{
  "timestamp": 1686251667,
  "eventType": "ServerMetric",
  "eventTypeVersion": 1,
  "userId": "<userid>",
  "data": {
    "playerUniqueId": "<userid>",
    "clientEvent": "Disconnected",
    "eventType": "Server"
  }
}
```
```json
{
  "apiMethod": "MetricServerEvent",
  "uRL": "https://latest.live.tex.bhvronline.com/metrics/server/event",
  "httpCode": 200,
  "elapsedTime": 0.06482639908790588,
  "eventType": "Server"
}
```
```json
{
  "data": {}
}
```
```json
{
  "playerUniqueId": "<userid>",
  "clientEvent": "Connected",
  "eventType": "Server"
}
```
```json
{
  "timestamp": 1686251664,
  "eventType": "ServerMetric",
  "eventTypeVersion": 1,
  "userId": "<userid>",
  "data": {
    "playerUniqueId": "<userid>",
    "clientEvent": "Connected",
    "eventType": "Server"
  }
}
```
```json
{
  "userId": "<userid>",
  "username": "<username>"
}

```
```json
{
  "apiMethod": "MetricClientEvent",
  "uRL": "https://latest.live.tex.bhvronline.com/metrics/client/event",
  "httpCode": 200,
  "elapsedTime": 0.06155579909682274,
  "eventType": "Client"
}
```
```json
{
  "timestamp": 1686251660,
  "eventType": "ClientMetric",
  "eventTypeVersion": 1,
  "userId": "<userid>",
  "data": {
    "isPlayingFromChina": false,
    "culture": "de-DE",
    "selectedRegion": "AT",
    "playerUniqueId": "<userid>",
    "eventType": "Client"
  }
}
```
```json
{
  "isPlayingFromChina": false,
  "culture": "de-DE",
  "selectedRegion": "AT",
  "playerUniqueId": "<userid>",
  "eventType": "Client"
}
```
```json
{
  "apiMethod": "MetricClientEvent",
  "uRL": "https://latest.live.tex.bhvronline.com/metrics/client/event",
  "httpCode": 200,
  "elapsedTime": 0.152643084526062,
  "eventType": "Client"
}
```
```json
{
  "timestamp": 1686251658,
  "eventType": "ClientMetric",
  "eventTypeVersion": 1,
  "userId": "<userid>",
  "data": {
    "playerId": "<userid>",
    "playerSessionId": "<sessionid>",
    "hasPurchasedGame": true,
    "eventType": "Client"
  }
}
```
```json
{
  "playerId": "<userid>",
  "playerSessionId": "<sessionid>",
  "hasPurchasedGame": true,
  "eventType": "Client"
}
```
```json
{
  "playerUniqueId": "<userid>",
  "clientEvent": "BackendIsOffline",
  "eventType": "Client"
}
```
```json
{
  "timestamp": 1685394406,
  "eventType": "ClientMetric",
  "eventTypeVersion": 1,
  "userId": "<userid>",
  "data": {
    "playerUniqueId": "<userid>",
    "clientEvent": "BackendIsOffline",
    "eventType": "Client"
  }
}
```
```json
{
  "apiMethod": "MetricClientEvent",
  "uRL": "https://latest.live.tex.bhvronline.com/metrics/client/event",
  "httpCode": 200,
  "elapsedTime": 0.08066260814666748,
  "eventType": "Client"
}
```
```json
{
  "body": [
    {
      "timestamp": 1685394394,
      "eventType": "gm_session_started",
      "eventTypeVersion": 1,
      "userId": "",
      "eventId": "<event_id>",
      "data": {
        "event_id": "<event_id>",
        "event_type": "gm_session_started",
        "event_time": "2023-05-29T21:06:34.334Z",
        "event_order": 1,
        "session_id": "<session_id>"
      }
    },
    {
      "timestamp": 1685394414,
      "eventType": "gm_session_ended",
      "eventTypeVersion": 1,
      "userId": "",
      "eventId": "<event_id>",
      "data": {
        "event_id": "<event_id>",
        "event_type": "gm_session_ended",
        "event_time": "2023-05-29T21:06:54.191Z",
        "event_order": 2,
        "session_id": "<session_id>"
      }
    }
  ]
}
```