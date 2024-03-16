import typer
from utils import find_shortest_path_command
from movements import Robi

app = typer.Typer()


@app.command("move_robot")
def move_robot(move_command: str):
    robi = Robi()
    shortest_command = find_shortest_path_command(robi)

    robi.move(shortest_command)

    # Execute the provided move command only if Robi hasn't passed the bonus yet or if preferred
    # we can just use robi.move(move_command) without calculating shortest path
    if not robi.passed_bonus:
        robi.move(move_command)


@app.command("shortest_path")
def shortest_path():
    robi = Robi()
    shortest_command = find_shortest_path_command(robi)
    typer.echo(f"Shortest move command: {shortest_command}")


if __name__ == "__main__":
    app()

