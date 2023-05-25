import unittest
import asyncio

import TrackerGG

csgo_client = TrackerGG.CSGOClient("d83a0067-83b9-40d1-9ae8-e1594f8a8019")
apex_client = TrackerGG.ApexClient("d83a0067-83b9-40d1-9ae8-e1594f8a8019")

loop = asyncio.get_event_loop()

csgo_profile_list = ["hiveruby"]


class CSGOTest(unittest.TestCase):
    def test_get_profile(self):
        for p in csgo_profile_list:
            print(loop.run_until_complete(csgo_client.get_profile(p)))

    def test_get_map_segment(self):
        for p in csgo_profile_list:
            print(loop.run_until_complete(csgo_client.get_map_segment(p)))

    def test_get_weapon_segment(self):
        for p in csgo_profile_list:
            print(loop.run_until_complete(csgo_client.get_weapon_segment(p)))

    def test_search_profile(self):
        for p in csgo_profile_list:
            print(loop.run_until_complete(csgo_client.search_profile(p)))
