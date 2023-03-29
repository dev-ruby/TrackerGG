# TrackerGG



![license](https://img.shields.io/github/license/Dev-Ruby/TrackerGG)
![Downloads](https://static.pepy.tech/badge/trackergg)
![Downloads](https://static.pepy.tech/badge/trackergg/month)

![Version](https://img.shields.io/pypi/v/TrackerGG)
![Commits](https://img.shields.io/github/commit-activity/m/dev-ruby/TrackerGG)

![Tracker](https://static1-fr.millenium.gg/articles/9/34/23/09/@/1117224-111-article_m-1.jpg)

**An API Wrapper for [TrackerGG API](https://tracker.gg)**



## [Wiki](https://github.com/dev-ruby/TrackerGG/wiki)

## Install

```pip install TrackerGG```

Get API Key

[TrackerGG Developers](https://tracker.gg/developers)


## **Quick Example**
```py
import TrackerGG
import asyncio


client = TrackerGG.CSGOClient("YOUR_API_KEY")

profile = asyncio.run(client.get_profile("PLAYER_NAME OR ID"))

print(profile.segments[0].stats.time_played)

```
**Output**
```
Name : Time Played
Value : 1,236h
Percentile : 84.0
```
