from typing import List, Tuple
import re

INPUT_FILE = "input.txt"


def get_coord(diff: int, dist: int) -> int:
    return dist - abs(diff)


def manhattan_dist(x1: int, x2: int, y1: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor:
    min_x = 0
    max_x = 0

    def __init__(self, coord: Tuple[int]) -> None:
        self.s_pos = (coord[0], coord[1])
        self.b_pos = (coord[2], coord[3])
        self.dist = manhattan_dist(
            self.s_pos[0],
            self.b_pos[0],
            self.s_pos[1],
            self.b_pos[1]
        )
        self._find_max_min_x()

    def _find_max_min_x(self) -> None:
        if self.s_pos[0] < Sensor.min_x:
            Sensor.min_x = self.s_pos[0]
        if self.b_pos[0] < Sensor.min_x:
            Sensor.min_x = self.b_pos[0]
        if self.s_pos[0] > Sensor.max_x:
            Sensor.max_x = self.s_pos[0]
        if self.b_pos[0] > Sensor.max_x:
            Sensor.max_x = self.b_pos[0]

    def __repr__(self) -> str:
        return f"(Sensor:s_pos={self.s_pos}, " \
               f"b_pos={self.b_pos}, dist={self.dist})"


def mark_visible_area(y: int,
                      row: List[str],
                      sensors: List[Sensor],
                      shift_total: int
                      ) -> None:
    """Mark visible area of all sensors in the row."""
    for sensor in sensors:
        diff_y = abs(y-sensor.s_pos[1])

        if diff_y > sensor.dist:
            continue
        elif diff_y <= sensor.dist:
            dx = get_coord(diff_y, sensor.dist)
            x_sensor = sensor.s_pos[0] + shift_total
            row[(x_sensor-dx):(x_sensor+dx+1)] = ["#"]*(2*dx+1)


def mark_sensors_beacons(y: int,
                         row: List[str],
                         sensors: List[Sensor],
                         shift_total: int
                         ) -> None:
    """Mark S and B in the row."""
    for sensor in sensors:
        if sensor.s_pos[1] == y:
            row[shift_total+sensor.s_pos[0]] = "S"
        if sensor.b_pos[1] == y:
            row[shift_total+sensor.b_pos[0]] = "B"


def get_marked_row(y: int, sensors: List[Sensor]) -> Tuple[List[str], int]:
    """Get row with marked visible area ans S/B symbols.

    The function also counts positions where there cant be a beacon.
    """
    shift_custom = 10  # Custom value
    margin_custom = 10  # Custom value
    shift = abs(sensors[0].min_x)
    shift_total = shift + shift_custom
    row = ["."]*(abs(sensors[0].max_x-sensors[0].min_x)
                 + shift_custom + margin_custom)

    mark_visible_area(y, row, sensors, shift_total)
    mark_sensors_beacons(y, row, sensors, shift_total)

    # Count no beacon positions
    count = len([item for item in row if item == "#"])
    return row, count


def main() -> None:
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    sensors = []
    for line in lines:
        line_parsed = re.findall(r"-*\d+", line)
        line_parsed = tuple([int(item) for item in line_parsed])
        sensors.append(Sensor(line_parsed))
    row, count = get_marked_row(2000000, sensors)
    print(row)
    print(count)


if __name__ == "__main__":
    main()
