from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta


@dataclass
class Task:
    """Represents a pet care task."""

    id: int
    description: str
    due_time: str          # HH:MM format
    duration_mins: int
    frequency: str         # Once, Daily, Weekly
    is_completed: bool = False

    def mark_complete(self):
        """Mark task as completed."""
        self.is_completed = True


@dataclass
class Pet:
    """Represents a pet."""

    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents a pet owner."""

    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))

        return all_tasks


class Scheduler:
    """Handles scheduling logic."""

    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the scheduler."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all pet tasks."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))

        return all_tasks

    def get_upcoming_tasks(self):
        """Return tasks sorted by due time."""
        tasks = self.get_all_tasks()

        return sorted(
            tasks,
            key=lambda item: item[1].due_time
        )

    def sort_by_time(self):
        """Sort all tasks by HH:MM time."""

        return sorted(
            self.get_all_tasks(),
            key=lambda item: item[1].due_time
        )

    def filter_completed(self):
        """Return completed tasks."""

        return [
            (pet_name, task)
            for pet_name, task in self.get_all_tasks()
            if task.is_completed
        ]

    def filter_incomplete(self):
        """Return incomplete tasks."""

        return [
            (pet_name, task)
            for pet_name, task in self.get_all_tasks()
            if not task.is_completed
        ]

    def filter_by_pet(self, pet_name):
        """Return tasks for one pet."""

        return [
            (name, task)
            for name, task in self.get_all_tasks()
            if name.lower() == pet_name.lower()
        ]

    def check_conflicts(self):
        """Detect tasks scheduled at the same time."""

        conflicts = []

        seen_times = {}

        for pet_name, task in self.get_all_tasks():

            if task.due_time in seen_times:

                conflicts.append(
                    f"Conflict detected: "
                    f"{seen_times[task.due_time]} "
                    f"and {task.description} "
                    f"are both scheduled at "
                    f"{task.due_time}"
                )

            else:

                seen_times[task.due_time] = task.description

        return conflicts

    def generate_recurring_tasks(self):
        """Generate next instance of recurring tasks."""

        new_tasks = []

        for pet in self.pets:

            for task in pet.tasks:

                if not task.is_completed:
                    continue

                if task.frequency.lower() == "daily":

                    new_tasks.append(
                        Task(
                            id=task.id + 1000,
                            description=task.description,
                            due_time=task.due_time,
                            duration_mins=task.duration_mins,
                            frequency="Daily"
                        )
                    )

                elif task.frequency.lower() == "weekly":

                    new_tasks.append(
                        Task(
                            id=task.id + 1000,
                            description=task.description,
                            due_time=task.due_time,
                            duration_mins=task.duration_mins,
                            frequency="Weekly"
                        )
                    )

        return new_tasks