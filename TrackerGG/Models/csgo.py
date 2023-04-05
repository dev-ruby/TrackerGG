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
from enum import Enum
from typing import Dict, Any, List, Union

from .platform import PlatformInfo
from .segment import Stat
from .user import UserInfo


class CSGOStats:
    def __init__(self, data: Dict[str, dict]):
        self.time_played: Stat = Stat(data["timePlayed"])
        self.score: Stat = Stat(data["score"])
        self.kills: Stat = Stat(data["kills"])
        self.deaths: Stat = Stat(data["deaths"])
        self.kd: Stat = Stat(data["kd"])
        self.damage: Stat = Stat(data["damage"])
        self.headshots: Stat = Stat(data["headshots"])
        self.dominations: Stat = Stat(data["dominations"])
        self.shots_fired: Stat = Stat(data["shotsFired"])
        self.shots_hit: Stat = Stat(data["shotsHit"])
        self.shots_accuracy: Stat = Stat(data["shotsAccuracy"])
        self.snipers_killed: Stat = Stat(data["snipersKilled"])
        self.domination_overkills: Stat = Stat(data["dominationOverkills"])
        self.domination_revenges: Stat = Stat(data["dominationRevenges"])
        self.bombs_planted: Stat = Stat(data["bombsPlanted"])
        self.bombs_defused: Stat = Stat(data["bombsDefused"])
        self.money_earned: Stat = Stat(data["moneyEarned"])
        self.hostages_rescued: Stat = Stat(data["hostagesRescued"])
        self.mvp: Stat = Stat(data["mvp"])
        self.wins: Stat = Stat(data["wins"])
        self.ties: Stat = Stat(data["ties"])
        self.matches_played: Stat = Stat(data["matchesPlayed"])
        self.losses: Stat = Stat(data["losses"])
        self.rounds_played: Stat = Stat(data["roundsPlayed"])
        self.rounds_won: Stat = Stat(data["roundsWon"])
        self.wl_percentage: Stat = Stat(data["wlPercentage"])
        self.headshot_pct: Stat = Stat(data["headshotPct"])


class CSGOMapStats:
    def __init__(self, data: Dict[str, dict]):
        self.rounds: Stat = Stat(data["rounds"])
        self.wins: Stat = Stat(data["wins"])


class CSGOMapSegment:
    def __init__(self, data: Dict[str, Union[str, dict]]):
        self.type: str = data["type"]
        self.attributes: dict = data["attributes"]
        self.metadata: dict = data["metadata"]
        self.expiry_date: str = data["expiryDate"]
        self.stats: CSGOMapStats = CSGOMapStats(data["stats"])


class CSGOSegment:
    def __init__(self, data: Dict[str, Union[str, dict]]):
        self.type: str = data["type"]
        self.attributes: dict = data["attributes"]
        self.metadata: dict = data["metadata"]
        self.expiry_date: str = data["expiryDate"]
        self.stats: CSGOStats = CSGOStats(data["stats"])


class CSGOProfile:
    def __init__(self, data: Dict[str, Any]):
        segments = []
        for seg in data["segments"]:
            segments.append(CSGOSegment(seg))

        self.platform_info: PlatformInfo = PlatformInfo(data["platformInfo"])
        self.user_info: UserInfo = UserInfo(data["userInfo"])
        self.segments: List[CSGOSegment] = segments
        self.expiry_date: str = data["expiryDate"]


class CSGOMap:
    def __init__(self, data: Dict[str, Union[str, dict]]):
        self.attributes: dict = data["attributes"]
        self.metadata: dict = data["metadata"]
        self.expiry_date: str = data["expiryDate"]
        self.stats: CSGOMapStats = CSGOMapStats(data["stats"])
