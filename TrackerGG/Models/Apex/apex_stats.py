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

from typing import *

from TrackerGG.Models.General import Stat

__all__ = ["ApexStats"]


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
        self.beast_of_the_hunt_kills: Optional[Stat] = Stat(data.get("beastOfTheHuntKills"))
        self.grapple_travel_distance: Optional[Stat] = Stat(data.get("grappleTravelDistance"))
        self.voices_warnings_heard: Optional[Stat] = Stat(data.get("voicesWarningsHeard"))
        self.voices_warnings_heard: Optional[Stat] = Stat(data.get("voicesWarningsHeard"))
