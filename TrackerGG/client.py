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

import asyncio
import json
from typing import List, Union

from .Models import CSGOProfile
from .Models import CSGOMapSegment
from .Models import CSGOWeaponSegment
from .Models import CSGOQueryData
from .httpclient import HTTPClient
from .httpclient import RequestMethod
from .httpclient import ResponseData
from .httpclient import Route


class TrackerClient:
    """
    Parent class of CSGOClient, ApexClient, etc.
    This class contains Tracker API Key, Event Loop, HTTP Client for interacting with TrackerAPI

    :param api_key: :class:`str` Tracker API Key.
    """

    api_key: str
    loop: asyncio.AbstractEventLoop
    http_client: HTTPClient

    def __init__(self, api_key: str) -> None:
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            pass

        self.loop = asyncio.get_event_loop()
        self.api_key = api_key
        self.http_client = HTTPClient(self.loop, self.api_key)


class CSGOClient(TrackerClient):
    """
    A class for interact with Tracker CSGO API
    This class contains Tracker API Key, Event Loop, HTTP Client for interacting with TrackerAPI

    :param api_key: :class:`str` Tracker API Key.
    """

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    async def get_profile(self, identifier: str) -> CSGOProfile:
        """
        Returns career stats for an CSGO player.

        :param identifier: :class:`str`
        :return: :class:`CSGOProfile`
        :raise AssertionError: If the response code is not 200
        """
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/csgo/standard/profile/steam/{identifier}")
        )

        assert response.status == 200, (
            "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        )

        json_data: dict = json.loads(response.response_data)

        return CSGOProfile(json_data["data"])

    async def get_map_segment(self, identifier: str) -> List[CSGOMapSegment]:
        """
        Returns stats of the map for a CSGO player.

        :param identifier: :class:`str`
        :return: List[:class:`CSGOMapSegment`]
        :raise AssertionError: If the response code is not 200
        """
        response: ResponseData = await self.http_client.request(
            Route(
                RequestMethod.GET,
                f"/csgo/standard/profile/steam/{identifier}/segments/map",
            )
        )

        assert response.status == 200, (
            "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        )

        json_data: dict = json.loads(response.response_data)

        segments = []

        for segment in json_data["data"]:
            segments.append(CSGOMapSegment(segment))

        return segments

    async def get_weapon_segment(self, identifier: str) -> List[CSGOWeaponSegment]:
        """
        Returns stats of the weapon for a CSGO player.

        :param identifier: :class:`str`
        :return: List[:class:`CSGOWeaponSegment`]
        :raise AssertionError: If the response code is not 200
        """
        response: ResponseData = await self.http_client.request(
            Route(
                RequestMethod.GET,
                f"/csgo/standard/profile/steam/{identifier}/segments/weapon",
            )
        )

        assert response.status == 200, (
            "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        )

        json_data: dict = json.loads(response.response_data)

        segments = []

        for segment in json_data["data"]:
            segments.append(CSGOWeaponSegment(segment))

        return segments

    async def search_profile(self, query: str) -> Union[None, List[CSGOQueryData]]:
        """
        Returns search data for a CSGO player using a unique identifier

        :param query: :class:`str`
        :return: Union[None, List[:class:`CSGOQueryData`]]
        :raise AssertionError: If the response code is not 200
        """
        response: ResponseData = await self.http_client.request(
            Route(
                RequestMethod.GET,
                f"/csgo/standard/search",
                params={"platform": "steam", "query": query},
            )
        )

        assert response.status == 200, (
            "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        )

        json_data: dict = json.loads(response.response_data)

        query_data = None

        if json_data["data"]:
            query_data = []
            for dat in json_data["data"]:
                query_data.append(CSGOQueryData(dat))

        return query_data
