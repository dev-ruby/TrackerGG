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

from typing import List, Dict, Union, Any


class Stat:
    def __init__(self, data: Dict[str, Union[int, float, str, None, dict]]):
        self.rank: int = data["rank"]
        self.percentile: float = data["percentile"]
        self.display_name: str = data["displayName"]
        self.display_category: str = data["displayCategory"]
        self.category: Union[None, str] = data["category"]
        self.description: str = data["description"]
        self.metadata: Union[None, dict[str, Any]] = data["metadata"]
        self.value: int = data["value"]
        self.display_value: str = data["displayValue"]
        self.display_type: str = data["displayType"]

    def __str__(self):
        return f"Name : {self.display_name}\nValue : {self.display_value}\nPercentile : {self.percentile}"


class Segment:
    def __init__(self, data: Dict[str, Union[str, int, dict]]):
        stats = []
        for stat in data["stats"].keys():
            stats.append(Stat(data["stats"][stat]))

        self.type: str = data["type"]
        self.attributes: dict = data["attributes"]
        self.metadata: dict = data["metadata"]
        self.expiry_date: str = data["expiryDate"]
        self.stats: List[Stat] = stats
