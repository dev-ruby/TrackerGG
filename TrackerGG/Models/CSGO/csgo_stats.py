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

__all__ = ["CSGOStats"]


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
