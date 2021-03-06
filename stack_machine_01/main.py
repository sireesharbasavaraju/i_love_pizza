from stackprocessor import CPU


def read_asm(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    cpu = CPU()
    program = read_asm("hello.asm")
    cpu.run(program)
