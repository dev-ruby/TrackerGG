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
from typing import Dict, Any, List

from .platform import PlatformInfo
from .segment import Segment
from .user import UserInfo


class CSGOProfile:
    def __init__(self, data: Dict[str, Any]):
        segments = []
        for seg in data["segments"]:
            segments.append(Segment(seg))

        self.platform_info: PlatformInfo = PlatformInfo(data["platformInfo"])
        self.user_info: UserInfo = UserInfo(data["userInfo"])
        self.segments: List[Segment] = segments
        self.expiry_date: str = data["expiryDate"]
