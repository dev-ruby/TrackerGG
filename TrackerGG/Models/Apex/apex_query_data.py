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

__all__ = ["ApexQueryData"]


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
