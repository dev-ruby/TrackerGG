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
from typing import Dict, Union, Any


class Platform(Enum):
    steam = "steam"
    origin = "origin"
    xbl = "xbl"
    psn = "psn"
    uplay = "uplay"


class PlatformInfo:
    def __init__(self, data: Dict[str, Union[str, int, None]]):
        platforms = {
            "steam": Platform.steam,
            "origin": Platform.origin,
            "xbl": Platform.xbl,
            "psn": Platform.psn,
            "uplay": Platform.uplay,
        }

        self.platform_slug: Platform = platforms[data["platformSlug"]]
        self.platform_user_id: Union[str, int] = data["platformUserId"]
        self.platform_user_handle: str = data["platformUserHandle"]
        self.platform_user_identifier: Union[str, int] = data["platformUserIdentifier"]
        self.avatar_url: str = data["avatarUrl"]
        self.additional_parameters: Any = data["additionalParameters"]
