import typer
from utils import find_shortest_path_command
from movements import Robi

app = typer.Typer()


@app.command("move_robot")
def move_robot(move_command: str):
    robi = Robi(initial_x=0, initial_y=0, initial_direction='T', bonus_x=3, bonus_y=41)
    shortest_command = find_shortest_path_command(robi)

    robi.move(shortest_command)


@app.command("shortest_path")
def shortest_path():
    robi = Robi()
    shortest_command = find_shortest_path_command(robi)
    typer.echo(f"Shortest move command: {shortest_command}")


if __name__ == "__main__":
    app()

