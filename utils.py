def find_shortest_path_command(robi):
    x_diff, y_diff = robi.bonus_x - robi.x, robi.bonus_y - robi.y
    x_command = 'F' * abs(x_diff) + ('L' if x_diff < 0 else 'R')
    y_command = 'F' * abs(y_diff) + ('L' if y_diff < 0 else 'R')
    return x_command + y_command
