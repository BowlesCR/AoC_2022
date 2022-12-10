import fileinput


class CPU:
    def __init__(self, text: list[str]):
        self.text = [line.strip() for line in text]
        self.pc = 0
        self.x = 1

        self.cycles = 0

    def tick(self) -> int:  # returns value DURING the cycle
        # start cycle
        inst = self.text[self.pc].split()
        if self.cycles == 0:
            if inst[0] == "noop":
                self.cycles = 1
            elif inst[0] == "addx":
                self.cycles = 2

        # during cycle
        x = self.x

        # end cycle
        self.cycles -= 1
        if self.cycles == 0:
            if inst[0] == "addx":
                self.x += int(inst[1])

            self.pc += 1
        return x

    def end_of_program(self) -> bool:
        return self.pc >= len(self.text)


def main():
    acc = 0

    cpu = CPU(list(fileinput.input()))
    for i in range(1, 220 + 1):
        assert not cpu.end_of_program()
        x = cpu.tick()
        if (i - 20) % 40 == 0:
            acc += i * x
    print(acc)


if __name__ == "__main__":
    main()
