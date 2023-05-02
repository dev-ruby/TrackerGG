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

from typing import Dict, Union, Optional, Any, List


class SocialAccount:
    def __init__(self, data: Dict[str, Union[str, int, None]]):
        self.platform_slug: str = data["platformSlug"]
        self.platform_user_id: Union[str, int] = data["platformUserId"]
        self.platform_user_handle: str = data["platformUserHandle"]
        self.platform_user_identifier: Union[str, int] = data["platformUserIdentifier"]
        self.avatar_url: Optional[str] = data.get("avatarUrl")
        self.additional_parameters: Any = data["additionalParameters"]


class UserInfo:
    def __init__(self, data: Dict[str, Union[str, int, bool, list, None]]):
        social_accounts = []
        if data["socialAccounts"]:
            for social_account in data["socialAccounts"]:
                social_accounts.append(SocialAccount(social_account))

        self.user_id: Optional[int] = data["userId"]
        self.is_premium: bool = data["isPremium"]
        self.is_verified: bool = data["isVerified"]
        self.is_influencer: bool = data["isInfluencer"]
        self.is_partner: bool = data["isPartner"]
        self.country_code: Union[str, None] = data["countryCode"]
        self.custom_avatar_url: Optional[str] = data["customAvatarUrl"]
        self.custom_hero_url: Optional[str] = data["customHeroUrl"]
        self.social_accounts: List[SocialAccount] = social_accounts
        self.page_views: int = data["pageviews"]
        self.custom_avatar_url: Any = data["isSuspicious"]
