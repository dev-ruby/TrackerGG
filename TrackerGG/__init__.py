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

from .Models import Platform
from .Models import CSGOProfile
from .Models import CSGOMapSegment
from .Models import CSGOWeaponSegment
from .Models import CSGOWeapon
from .Models import ApexProfile

from .client import CSGOClient
from .client import ApexClient

from . import utils


count = 0

try:
    import aiohttp
    count += 1
except ImportError:
    pass

try:
    import httpx
    count += 1
except ImportError:
    pass

if count == 0:
    raise ImportError("\nAt least one of aiohttp or httpx libraries is required\nTry `pip install aiohttp` or `pip install httpx`")