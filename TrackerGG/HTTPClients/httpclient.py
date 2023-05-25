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
from enum import Enum, auto
from typing import ClassVar, Optional, Dict, Any


class Missing:
    pass


MISSING: Any = Missing()


class HTTPClientLibrary(Enum):
    AIOHTTP = auto()
    HTTPX = auto()


def get_http_client(
    loop: asyncio.AbstractEventLoop, api_key: str, lib: Optional[HTTPClientLibrary] = None
):
    if lib is None:
        try:
            import aiohttp
            from .aiohttp_client import AiohttpHTTPClient

            return AiohttpHTTPClient(loop, api_key)
        except ImportError:
            pass

        try:
            import httpx
            from .httpx_client import HttpxHTTPClient

            return HttpxHTTPClient(loop, api_key)
        except ImportError:
            pass

        raise ImportError("At least one of aiohttp or httpx libraries is required")

    if lib == HTTPClientLibrary.HTTPX:
        from .httpx_client import HttpxHTTPClient

        return HttpxHTTPClient(loop, api_key)

    elif lib == HTTPClientLibrary.AIOHTTP:
        from .aiohttp_client import AiohttpHTTPClient

        return AiohttpHTTPClient(loop, api_key)


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
            url += "%s%s=%s" % ("?" if first else "&", key, str(val))
            first = False
        return url

    def __init__(self, method: RequestMethod, url: str, params: Optional[Dict[str, Any]] = None) -> None:
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
