from enum import Enum


class EventStatus(str, Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    NOT_PLAYED = "NOT_PLAYED"
