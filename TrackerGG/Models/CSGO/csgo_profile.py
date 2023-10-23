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

from TrackerGG.Models.General import PlatformInfo, UserInfo
from .csgo_segment import CSGOSegment

__all__ = ["CSGOProfile"]


class CSGOProfile:
    def __init__(self, data: Dict[str, Any]):
        segments = []
        for seg in data["segments"]:
            segments.append(CSGOSegment(seg))

        self.platform_info: PlatformInfo = PlatformInfo(data["platformInfo"])
        self.user_info: UserInfo = UserInfo(data["userInfo"])
        self.segments: List[CSGOSegment] = segments
        self.expiry_date: str = data["expiryDate"]
