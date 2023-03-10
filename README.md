# TrackerGG



![license](https://img.shields.io/github/license/Dev-Ruby/TrackerGG)
![Downloads](https://img.shields.io/pypi/dm/TrackerGG)
![Issues](https://img.shields.io/github/issues-raw/dev-ruby/TrackerGG)

![Version](https://img.shields.io/pypi/v/TrackerGG)
![Commits](https://img.shields.io/github/commit-activity/m/dev-ruby/TrackerGG)

![Tracker](https://static1-fr.millenium.gg/articles/9/34/23/09/@/1117224-111-article_m-1.jpg)

**TrackerGG is a Tracker API Client**

## Install

```pip install TrackerGG```


## Use

[Sign in tracker.gg and get token](https://tracker.gg/developers)

**Example of getting csgo profile**
```py
import TrackerGG # import this library
import asyncio # asyncio library for calling async function

client = TrackerGG.Client('TOKEN') # replace 'TOKEN' with your token value.

def GetSync(profile):
    return client.get_csgo_profile(profile)

async def GetAsync(profile):
    return await client.async_get_csgo_profile(profile)

print(GetSync("DevRuby").stats.kills.value)
print(asyncio.run(GetAsync("DevRuby")).stats.kills.value)

```

## Exceptions
### ApiError
Incorrect Api Key
### UserError
Can't find the user
