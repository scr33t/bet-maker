from fastapi import HTTPException


class InvalidEventStatusException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Invalid event status")


class EventNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Event not found")
