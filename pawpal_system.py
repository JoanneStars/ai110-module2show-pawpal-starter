from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    id: int
    description: str
    due_time: str
    duration_mins: int
    frequency: str
    is_completed: bool = False

    def mark_complete(self):
        self.is_completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)


class Scheduler:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))

        return all_tasks

    def get_upcoming_tasks(self):
        return self.get_all_tasks()

    def check_conflicts(self, new_task):
        return False

    def generate_recurring_tasks(self):
        return []