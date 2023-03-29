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

from .Models import CSGOProfile
from .httpclient import HTTPClient
from .httpclient import RequestMethod
from .httpclient import ResponseData
from .httpclient import Route


class CSGOClient:
    api_key: str
    loop: asyncio.AbstractEventLoop
    http_client: HTTPClient

    def __init__(self, api_key: str) -> None:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        self.loop = asyncio.get_event_loop()
        self.api_key = api_key
        self.http_client = HTTPClient(self.loop, self.api_key)

    async def get_profile(self, identifier: str):
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/csgo/standard/profile/steam/{identifier}")
        )

        assert response.status == 200, "HTTP Response Status Code is not 200"

        json_data: dict = json.loads(response.response_data)

        return CSGOProfile(json_data["data"])
