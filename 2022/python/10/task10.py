INPUT_FILE = "input.txt"


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    lines = iter(lines)

    cycles = []
    cycle_count = 1
    register = 1
    hold = False
    crt_grid = [["."]*40 for _ in range(6)]
    crt_col = 0
    crt_row = 0
    sprite = (register-1, register, register+1)
    for cycle in range(1, 300):
        # Pass to crt index to the beggining of a new line
        if (crt_col > 39):
            crt_col = 0
            crt_row += 1
        # Draw CRT pixel
        if crt_col in sprite:
            crt_grid[crt_row][crt_col] = "#"
        crt_col += 1
        if not hold:
            try:
                instr = next(lines)
                inner_cycle = 1
            except StopIteration:
                break
        if "noop" in instr:
            cycles.append([instr, cycle, register, cycle*register])
        elif "addx" in instr:
            addx = instr.split(" ")
            cycles.append([instr, cycle, register, cycle*register])
            # Hold instruction loading
            hold = True
            inner_cycle += 1
            if inner_cycle > 2:
                register += int(addx[1])
                sprite = (register-1, register, register+1)
                # Possible to load next instruction
                hold = False

    cycles.append(["None", cycle_count, register, cycle_count*register])
    print(cycles)
    print(cycles[19][3] + cycles[59][3] + cycles[99][3] + cycles[139][3] + cycles[179][3] + cycles[219][3])

    for row in crt_grid:
        print(row)


if __name__ == "__main__":
    main()
