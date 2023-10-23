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

__all__ = ["CSGOWeaponStats"]


class CSGOWeaponStats:
    def __init__(self, data: Dict[str, dict]):
        self.kills: Stat = Stat(data["kills"])
        self.shots_fired: Stat = Stat(data["shotsFired"])
        self.shots_hit: Stat = Stat(data["shotsHit"])
        self.shots_accuracy: Stat = Stat(data["shotsAccuracy"])
