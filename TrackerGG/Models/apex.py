# -*- coding: utf-8 -*-

"""
Copyright (c) 2023 DevRuby

MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
from typing import Dict, Any, Union, Optional, List
from .segment import Stat
from .platform import PlatformInfo
from .user import UserInfo


class ApexQueryData:
    def __init__(self, data: Dict[str, Optional[Union[str, int]]]):
        self.platform_id: int = int(data["platformId"])
        self.platform_slug: str = data["platformSlug"]
        self.platform_user_identifier: str = data["platformUserIdentifier"]
        self.platform_user_id: str = data["platformUserId"]
        self.platform_user_handle: str = data["platformUserHandle"]
        self.avatar_url: Optional[str] = data["avatarUrl"]
        self.status: Optional[str] = data["status"]
        self.additional_parameters: Optional[str] = data["additionalParameters"]


class ApexStats:
    def __init__(self, data: Dict[str, dict]):
        self.level: Optional[Stat] = Stat(data.get("level"))
        self.kills: Optional[Stat] = Stat(data.get("kills"))
        self.kills_per_match: Optional[Stat] = Stat(data.get("killsPerMatch"))
        self.winning_kills: Optional[Stat] = Stat(data.get("winningKills"))
        self.kills_as_kill_leader: Optional[Stat] = Stat(data.get("killsAsKillLeader"))
        self.damage: Optional[Stat] = Stat(data.get("damage"))
        self.matches_played: Optional[Stat] = Stat(data.get("matchesPlayed"))
        self.revives: Optional[Stat] = Stat(data.get("revives"))
        self.sniper_kills: Optional[Stat] = Stat(data.get("sniperKills"))
        self.rank_score: Optional[Stat] = Stat(data.get("rankScore"))
        self.arena_rank_score: Optional[Stat] = Stat(data.get("arenaRankScore"))
        self.beast_of_the_hunt_kills: Optional[Stat] = Stat(
            data.get("beastOfTheHuntKills")
        )
        self.grapple_travel_distance: Optional[Stat] = Stat(
            data.get("grappleTravelDistance")
        )
        self.voices_warnings_heard: Optional[Stat] = Stat(
            data.get("voicesWarningsHeard")
        )
        self.voices_warnings_heard: Optional[Stat] = Stat(
            data.get("voicesWarningsHeard")
        )


class ApexSegment:
    def __init__(self, data: Dict[str, Union[str, dict]]):
        self.type: str = data["type"]
        self.attributes: dict = data["attributes"]
        self.metadata: dict = data["metadata"]
        self.expiry_date: str = data["expiryDate"]
        self.stats: ApexStats = ApexStats(data["stats"])


class ApexProfile:
    def __init__(self, data: Dict[str, Any]):
        segments = []
        for seg in data["segments"]:
            segments.append(ApexSegment(seg))

        self.platform_info: PlatformInfo = PlatformInfo(data["platformInfo"])
        self.user_info: UserInfo = UserInfo(data["userInfo"])
        self.segments: List[ApexSegment] = segments
        self.expiry_date: str = data["expiryDate"]
