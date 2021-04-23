# -*- coding: utf-8 -*-
class ApiError(Exception):
    def __init__(self):
        super().__init__("Incorrect API key")
class UserError(Exception):
    def __init__(self):
        super().__init__("Can't find the user")
