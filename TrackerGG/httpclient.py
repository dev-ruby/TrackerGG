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
import atexit
from enum import Enum
from typing import ClassVar, Optional, Dict, Any

import aiohttp


class Missing:
    pass


MISSING: Any = Missing()


class RequestMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    HEAD = 3
    DELETE = 4
    PATCH = 5
    OPTIONS = 6


class Route:
    BASE_URL: ClassVar[str] = "https://public-api.tracker.gg/v2"

    @staticmethod
    def __make_url(url: str, params: dict) -> str:
        first: bool = True
        for key, val in params.items():
            url += "%s%s=%s" % ("?" if first else "&", key, val)
            first = False
        return url

    def __init__(
        self, method: RequestMethod, url: str, params: Optional[Dict[str, str]] = None
    ) -> None:
        if params:
            url = self.__make_url(url, params)
        self.url: str = self.BASE_URL + url
        self.method: RequestMethod = method


class ResponseData:
    def __init__(self, text: str, status: int) -> None:
        self.response_data: str = text
        self.status: int = status

    def __str__(self) -> str:
        return f"status_code : {self.status}\nresponse_data : {self.response_data}"


class HTTPClient:
    USER_AGENT: ClassVar[str] = "Mozilla/5.0"

    def __init__(self, loop: asyncio.AbstractEventLoop, api_key: str) -> None:
        self.loop: asyncio.AbstractEventLoop = loop
        self.session: aiohttp.ClientSession = MISSING
        self.api_key: str = api_key

        atexit.register(self.close)

    async def request(
        self, route: Route, headers: Optional[Dict[str, str]] = None
    ) -> ResponseData:
        if headers:
            headers["User-Agent"] = self.USER_AGENT
            headers["Accept"] = "application/json"
            headers["Accept-Encoding"] = "gzip"
            headers["TRN-Api-Key"] = self.api_key
            headers["Host"] = "public-api.tracker.gg"
            headers["Connection"] = "keep-alive"
            headers["TE"] = "trailers"
            headers["Upgrade-Insecure-Requests"] = "1"
        else:
            headers = {
                "User-Agent": self.USER_AGENT,
                "Accept": "application/json",
                "Accept-Encoding": "gzip",
                "TRN-Api-Key": self.api_key,
                "Host": "public-api.tracker.gg",
                "Connection": "keep-alive",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            }

        if self.session == MISSING:
            self.session = aiohttp.ClientSession()

        async with self.session.request(
            method=route.method.name, url=route.url, headers=headers
        ) as response:
            status: int = response.status
            text: str = await response.text(encoding="utf-8")
            return ResponseData(text, status)

    def close(self) -> None:
        try:
            if not self.session.closed:
                asyncio.run(self.session.close())
        except TypeError:
            pass
