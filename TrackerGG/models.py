# -*- coding: utf-8 -*-

"""
Copyright (c) 2021 DevRuby

MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""

import requests
from .exceptions import ApiError, UserError
from enum import Enum
import re
import aiohttp


class Platform(Enum):
    steam = "steam"
    uplay = "uplay"
    ps = "playstation"
    xbox = "xbox"
    battlenet = "battlenet"
    origin = "origin"


def get_platform(platform: str) -> Platform:
    return {
        "steam": Platform.steam,
        "uplay": Platform.uplay,
        "psn": Platform.ps,
        "xbl": Platform.xbox,
        "battlenet": Platform.battlenet,
        "origin": Platform.origin,
    }.get(platform)


class CsgoProfileData:
    """
    Attributes
    -----------
    platform class:`PlatformInfo`
        user's playform data
    stats class:`CsgoStats`
        user's stats
    """
    def __init__(self, data: dict):
        self.platform: PlatformInfo = PlatformInfo(data["platformInfo"])
        self.stats: CsgoStats = CsgoStats(data["segments"][0]["stats"])


class CsgoStatData:
    """
    Attributes
    -----------
    rank class:`str`
        Could be `None`
    percentile class:`str`
        percentage of your data
    displayName class:`str`
        The name of the stat on the TrackerGG website.
    displayCategory class:`str`

    category class:`str`

    metadata class:`str`

    value class:`float` or `int`
        stat's value
    displayValue class:`str`
        The value of the stat on the TrackerGG website
    displayType class:`str`
        The type of the stat on the TrackerGG website
    """
    def __init__(self, data: dict):
        self.rank = data["rank"]
        self.percentile = data["percentile"]
        self.displayName = data["displayName"]
        self.displayCategory = data["displayCategory"]
        self.category = data["category"]
        self.metadata = data["metadata"]
        self.value = data["value"]
        self.displayValue = data["displayValue"]
        self.displayType = data["displayType"]


class CsgoStats:
    def __init__(self, data: dict):
        self.timePlayed: CsgoStatData = CsgoStatData(data["timePlayed"])
        self.score: CsgoStatData = CsgoStatData(data["score"])
        self.kills: CsgoStatData = CsgoStatData(data["kills"])
        self.deaths: CsgoStatData = CsgoStatData(data["deaths"])
        self.kdr: CsgoStatData = CsgoStatData(data["kd"])
        self.damage: CsgoStatData = CsgoStatData(data["damage"])
        self.headshots: CsgoStatData = CsgoStatData(data["headshots"])
        self.dominations: CsgoStatData = CsgoStatData(data["dominations"])
        self.shotsFired: CsgoStatData = CsgoStatData(data["shotsFired"])
        self.shotsHit: CsgoStatData = CsgoStatData(data["shotsHit"])
        self.shotsAccuracy: CsgoStatData = CsgoStatData(data["shotsAccuracy"])
        self.snipersKilled: CsgoStatData = CsgoStatData(data["snipersKilled"])
        self.dominationOverkills: CsgoStatData = CsgoStatData(
            data["dominationOverkills"]
        )
        self.dominationRevenges: CsgoStatData = CsgoStatData(data["dominationRevenges"])
        self.bombsPlanted: CsgoStatData = CsgoStatData(data["bombsPlanted"])
        self.bombsDefused: CsgoStatData = CsgoStatData(data["bombsDefused"])
        self.moneyEarned: CsgoStatData = CsgoStatData(data["moneyEarned"])
        self.hostagesRescued: CsgoStatData = CsgoStatData(data["hostagesRescued"])
        self.mvp: CsgoStatData = CsgoStatData(data["mvp"])
        self.wins: CsgoStatData = CsgoStatData(data["wins"])
        self.ties: CsgoStatData = CsgoStatData(data["ties"])
        self.matchesPlayed: CsgoStatData = CsgoStatData(data["matchesPlayed"])
        self.losses: CsgoStatData = CsgoStatData(data["losses"])
        self.roundsPlayed: CsgoStatData = CsgoStatData(data["roundsPlayed"])
        self.roundsWon: CsgoStatData = CsgoStatData(data["roundsWon"])
        self.winLosePct: CsgoStatData = CsgoStatData(data["wlPercentage"])
        self.headshotPct: CsgoStatData = CsgoStatData(data["headshotPct"])


class PlatformInfo:
    """
    Attributes
    -----------
    platform class:`Platform`
        user's platform
    userID class:`str` or `int`
        user's ID in the platform
    userHandle class:`str`
        user's name
    userIdentifier class:`str` or `int`
        user's identifier
    avatarUrl class:`str`
        user's avatar
    additionalParameters
        Parameters. Could be None
    """
    def __init__(self, data: dict):
        self.platform = get_platform(data["platformSlug"])
        self.userID = data["platformUserId"]
        self.userHandle = data["platformUserHandle"]
        self.userIdentifier = data["platformUserIdentifier"]
        self.avatarUrl = data["avatarUrl"]
        self.additionalParameters = data["additionalParameters"]


class Client:
    def __init__(self, api_key: str) -> None:
        if (
            re.compile(
                "[A-Za-z0-9+]{8}-[A-Za-z0-9+]{4}-[A-Za-z0-9+]{4}-[A-Za-z0-9+]{4}-[A-Za-z0-9+]{12}"
            ).match(api_key)
            == None
            or not len(api_key) == 36
        ):
            raise ApiError

        self.__api_key = api_key

    @property
    def api_key(self) -> str:
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        if (
            re.compile(
                "[A-Za-z0-9+]{8}-[A-Za-z0-9+]{4}-[A-Za-z0-9+]{4}-[A-Za-z0-9+]{4}-[A-Za-z0-9+]{12}"
            ).match(api_key)
            == None
            or not len(api_key) == 36
        ):
            raise ApiError

        self.__api_key = api_key

    def get_csgo_profile(self, identifier: str) -> CsgoProfileData:
        response = requests.get(
            url="https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{0}".format(
                identifier
            ),
            params={
                "TRN-Api-Key": self.__api_key,
                "Accept": "application/json",
                "Accept-Encoding": "gzip",
            },
        )
        if response.json().get("message") == "Invalid authentication credentials":
            raise ApiError
        if (
            "errors" in response.json()
            and response.json().get("errors")[0].get("message")
            == "The stat collector returned the following status code: NotFound"
        ):
            raise UserError

        return CsgoProfileData(response.json()["data"])

    async def async_get_csgo_profile(self, identifier:str) -> CsgoProfileData:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{0}".format(
                    identifier
                ),
                params={
                    "TRN-Api-Key": self.__api_key,
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip",
                },
            ) as response:
                res = await response.json()
                if (
                    res.get("message")
                    == "Invalid authentication credentials"
                ):
                    raise ApiError
                if (
                    "errors" in res
                    and res.get("errors")[0].get("message")
                    == "The stat collector returned the following status code: NotFound"
                ):
                    raise UserError
                return CsgoProfileData(res["data"])
