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

from typing import Dict, Union, Any, Optional


class Stat:
    def __init__(self, data: Dict[str, Union[int, float, str, dict, None]]):
        if data is None:
            return
        self.rank: Optional[int] = data["rank"]
        self.percentile: Optional[float] = data["percentile"]
        self.description: Optional[str] = data["description"]
        self.metadata: Optional[dict[str, Any]] = data["metadata"]
        self.category: Optional[str] = data["category"]
        self.display_name: str = data["displayName"]
        self.value: int = data["value"]
        self.display_value: str = data["displayValue"]
        self.display_category: str = data["displayCategory"]
        self.display_type: str = data["displayType"]

    def __str__(self):
        return f"Name : {self.display_name}\nValue : {self.display_value}\nPercentile : {self.percentile}"
