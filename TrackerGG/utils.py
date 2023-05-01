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

from .Models import CSGOMapSegment
from .Models import CSGOWeaponSegment
from .Models import CSGOWeapon
from typing import List, Union


def query_map_by_key(
    maps: List[CSGOMapSegment], key: str
) -> Union[CSGOMapSegment, int]:
    """
    Returns a CSGOMapSegment that matches key.
    Returns -1 if there is no matching CSGOMapSegment Object.

    :param maps: List[:class:`CSGOMapSegment`]
    :param key: :class:`str`
    :return: Union[:class:`CSGOMapSegment`, :class:`int`]
    """
    for _map in maps:
        if _map.attributes["key"] == key:
            return _map
    return -1


def query_weapon(
    weapons: List[CSGOWeaponSegment], key: CSGOWeapon
) -> Union[CSGOWeaponSegment, int]:
    """
    Returns a CSGO weapon segment that matches key.
    Returns -1 if there is no matching CSGOWeaponSegment Object.

    :param weapons: List[:class:`CSGOWeaponSegment`]
    :param key: :class:`CSGOWeapon`
    :return: Union[:class:`CSGOWeaponSegment`, :class:`int`]
    """
    for _weapon in weapons:
        if _weapon.attributes["key"] == key.value:
            return _weapon
    return -1
