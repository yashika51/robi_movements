"""This could be an additional functionaloty to also have these movement features available
as API rather than just commands in CLI"""


import typer
from fastapi import FastAPI
from utils import find_shortest_path_command
from movements import Robi
from models import MoveCommand

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Robi Movement API"}


@app.post("/move_robot/")
async def move_robot(move_command: MoveCommand):
    robi = Robi(initial_x=0, initial_y=0, initial_direction='T', bonus_x=3, bonus_y=41)
    shortest_command = find_shortest_path_command(robi)

    # Execute the shortest path command first
    shortest_path = robi.move(shortest_command)

    # Execute the provided move command only if Robi hasn't passed the bonus yet
    if not robi.passed_bonus:
        robi_move = robi.move(move_command.move_command)

    return {"shortest_path_result": shortest_path, "provided_move_result": robi_move}


@app.get("/shortest_path/")
async def shortest_path():
    robi = Robi()
    shortest_command = find_shortest_path_command(robi)
    return {"shortest_move_command": shortest_command}


if __name__ == "__main__":
    typer.run(app)
