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

from .csgo_stats import CSGOStats

__all__ = ["CSGOSegment"]


class CSGOSegment:
    def __init__(self, data: Dict[str, Union[str, dict]]):
        self.type: str = data["type"]
        self.attributes: dict = data["attributes"]
        self.metadata: dict = data["metadata"]
        self.expiry_date: str = data["expiryDate"]
        self.stats: CSGOStats = CSGOStats(data["stats"])
