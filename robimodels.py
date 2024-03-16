from pydantic import BaseModel


class MoveCommand(BaseModel):
    move_command: str


class RobiResult(BaseModel):
    x: int
    y: int
    direction: str
    passed_bonus: bool
