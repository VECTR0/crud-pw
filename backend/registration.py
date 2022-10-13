#!/usr/bin/python
import datetime

# TODO: jak ma wygladac tabela


class Registration:
    def __init__(self, date_1: datetime, date_2: datetime, who: str, what: str):
        self.date_1 = date_1
        self.date_2 = date_2
        self.who = who
        self.what = what

    def __init__(self, id: int, date_1: datetime, date_2: datetime, who: str, what: str):
        self.id = id
        self.date_1 = date_1
        self.date_2 = date_2
        self.who = who
        self.what = what
