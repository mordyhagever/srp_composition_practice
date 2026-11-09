from .cpu import Cpu
from .ram import Ram
from.disk import Disk

class Computer:
    def __init__(self, cpu, ram, disk):
        self.cpu = cpu
        self.disk = disk
        self.ram = ram

    def __str__(self):
        return f"{self.cpu.amount}-core {self.cpu.speed}GHz CPU, {self.ram.size}GB RAM, {self.disk.size}GB SSD"

    def can_run(self, min_heart, min_memory):
        if self.ram.size > min_memory and self.cpu.amount > min_heart:
            return True
        return False