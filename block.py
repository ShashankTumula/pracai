class Block:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
    
    def move(self, nx, ny, nz):
        self.x = nx
        self.y = ny
        self.z = nz
    
    def display(self):
        print(f"{self.name} is at ({self.x}, {self.y}, {self.z})")


class World:
    def __init__(self):
        self.blocks = [
            Block("A", 0, 0, 0),
            Block("B", 0, 1, 0),
            Block("C", 0, 2, 0)
        ]
    
    def move_block(self, name, nx, ny, nz):
        for block in self.blocks:
            if block.name == name:
                block.move(nx, ny, nz)
                break
    
    def display(self):
        for block in self.blocks:
            block.display()


def main():
    world = World()
    world.display()
    world.move_block("A", 1, 0, 0)
    world.display()


if __name__ == "__main__":
    main()
