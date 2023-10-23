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

from TrackerGG.Models.General import Platform

__all__ = ["PlatformInfo"]


class PlatformInfo:
    def __init__(self, data: Dict[str, Union[str, int, None]]):
        self.platform_slug: Platform = Platform.from_name(data["platformSlug"])
        self.platform_user_id: Union[str, int] = data["platformUserId"]
        self.platform_user_handle: str = data["platformUserHandle"]
        self.platform_user_identifier: Union[str, int] = data["platformUserIdentifier"]
        self.avatar_url: str = data["avatarUrl"]
        self.additional_parameters: Any = data["additionalParameters"]
