# -*- coding: utf-8 -*-

"""
TrackerGG API Wrapper
~~~~~~~~~~~~~~~~~~~

An API Wrapper for TrackerGG API

Copyright (c) 2023 DevRuby

"""

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

import TrackerGG.Models
from . import utils
from .client import ApexClient
from .client import CSGOClient

__all__ = ["Models", "CSGOClient", "ApexClient", "utils"]

__count = 0

try:
    import aiohttp

    __count += 1
except ImportError:
    pass

try:
    import httpx

    __count += 1
except ImportError:
    pass

if __count == 0:
    raise ImportError(
        "\nAt least one of aiohttp or httpx libraries is required\nTry `pip install aiohttp` or `pip install httpx`"
    )
