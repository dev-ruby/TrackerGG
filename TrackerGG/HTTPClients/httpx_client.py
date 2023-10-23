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
from typing import *

import httpx

from .abstract_http_client import AbstractHTTPClient
from .httpclient import ResponseData, Route

__all__ = ["HttpxHTTPClient"]


class HttpxHTTPClient(AbstractHTTPClient):
    USER_AGENT: ClassVar[str] = "Mozilla/5.0"

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, loop: asyncio.AbstractEventLoop, api_key: str) -> None:
        self.loop: asyncio.AbstractEventLoop = loop
        self.lock: asyncio.Lock = asyncio.Lock()
        self.api_key: str = api_key

    async def request(self, route: Route, headers: Optional[Dict[str, str]] = None) -> ResponseData:
        if not headers:
            headers = {}

        default_header = {
            "User-Agent": self.USER_AGENT,
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "TRN-Api-Key": self.api_key,
            "Host": "public-api.tracker.gg",
            "Connection": "keep-alive",
            "TE": "trailers",
            "Upgrade-Insecure-Requests": "1",
        }

        headers.update(default_header)

        async with self.lock:
            async with httpx.AsyncClient() as client:
                response: httpx.Response = await client.request(
                    method=route.method.name, url=route.url, headers=headers
                )
                status: int = response.status_code
                text: str = response.text
                return ResponseData(text, status)
