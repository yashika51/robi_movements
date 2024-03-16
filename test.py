import subprocess


def test_move_robot():
    print("Test Case for move_robot:")
    move_command = "RRRF38"
    subprocess.run(["python", "app.py", "move_robot", move_command])


def test_shortest_path():
    print("Test Case for shortest_path:")
    subprocess.run(["python", "app.py", "shortest_path"])


if __name__ == "__main__":
    test_move_robot()
    test_shortest_path()
