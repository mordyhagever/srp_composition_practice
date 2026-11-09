from classes.disk import Disk
from classes.ram import Ram
from classes.cpu import Cpu
from classes.cumputer import Computer

pc = Computer(Cpu(8, 3.2), Ram(8), Disk(512))
print(pc)
print("Can run the game", pc.can_run(6, 16))