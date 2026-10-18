# scheduler.py

class Owner:
    """Stores owner information and scheduling preferences."""

    def __init__(self, name, available_time, preference):
        self.name = name
        self.available_time = int(available_time)
        self.preference = preference


class Pet:
    """Represents a pet profile."""

    def __init__(self, name, species):
        self.name = name
        self.species = species


class Task:
    """Represents a pet care task."""

    def __init__(self, title, duration, priority):
        self.title = title
        self.duration = int(duration)
        self.priority = priority


class Scheduler:
    """Generates a task schedule based on owner preferences."""

    def __init__(self):
        """Initialize priority rankings."""
        self.priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

    def generate_plan(self, tasks, owner):
        """Create a schedule using the owner's preference."""

        ranked_tasks = list(tasks)

        if owner.preference == "Priority First":
            ranked_tasks.sort(
                key=lambda task: (
                    self.priority_order.get(
                        task.priority.lower(),
                        99
                    ),
                    task.duration
                )
            )

        elif owner.preference == "Shortest Tasks First":
            ranked_tasks.sort(
                key=lambda task: task.duration
            )

        plan = []
        skipped = []

        remaining_time = owner.available_time

        for task in ranked_tasks:

            if task.duration <= remaining_time:
                plan.append(task)
                remaining_time -= task.duration

            else:
                skipped.append(task)

        return plan, skipped