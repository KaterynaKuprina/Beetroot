import random


class Boss:

    def __init__(self, name: str, company: str):
        self.id = random.randint(1, 999)
        self.name = name
        self.company = company
        self.workers = []

    @property
    def add_workers(self):
        return self.workers

    @add_workers.setter
    def add_workers(self, worker):
        self.workers.append(worker)


class Worker:

    def __init__(self, name: str, boss: Boss):
        self.id_ = random.randint(1, 9999)
        self.name = name
        self.boss = boss
        boss.add_workers = {"id_": self.id_, "name": name}


boss_1 = Boss("Jhonny", "Willariba")
boss_2 = Boss("Linda", "Willabadga")
worker_1 = Worker("Henry", boss_1)
worker_2 = Worker("Lesly", boss_1)
worker_3 = Worker("Anna", boss_2)
worker_4 = Worker("Alice", boss_2)

print(boss_1.workers)
print(boss_2.workers)
