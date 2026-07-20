class Computer:
    class CPU:
        def __init__(self, cores):
            self.cores = cores 
        
        def info(self):
            print(f' "CPU has {self.cores} counts" ')

    def __init__(self, cores):
        self.cpu = Computer.CPU(cores)

computer = Computer(8)
computer.cpu.info()
