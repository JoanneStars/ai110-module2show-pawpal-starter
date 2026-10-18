from datetime import datetime, timedelta


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
        self.tasks = []

    def add_task(self, task):
        """Add a task to a pet."""
        self.tasks.append(task)


class Task:
    """Represents a pet care task."""

    def __init__(
        self,
        title,
        duration,
        priority,
        due_time="09:00",
        frequency="Once"
    ):
        self.title = title
        self.duration = int(duration)
        self.priority = priority
        self.due_time = due_time
        self.frequency = frequency
        self.completed = False

    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True


class Scheduler:
    """Generates schedules and manages tasks."""

    def __init__(self):
        self.priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

    def generate_plan(self, tasks, owner):
        """Create a schedule using owner preferences."""

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

    def sort_by_time(self, tasks):
        """Sort tasks by HH:MM due time."""

        return sorted(
            tasks,
            key=lambda task: task.due_time
        )

    def filter_completed(self, tasks):
        """Return completed tasks."""

        return [
            task
            for task in tasks
            if task.completed
        ]

    def filter_incomplete(self, tasks):
        """Return incomplete tasks."""

        return [
            task
            for task in tasks
            if not task.completed
        ]

    def check_conflicts(self, tasks):
        """Detect tasks sharing the same time."""

        conflicts = []

        seen = {}

        for task in tasks:

            if task.due_time in seen:

                conflicts.append(
                    f"Conflict detected: "
                    f"{seen[task.due_time]} and "
                    f"{task.title} "
                    f"are both scheduled at "
                    f"{task.due_time}"
                )

            else:

                seen[task.due_time] = task.title

        return conflicts

    def generate_recurring_tasks(self, tasks):
        """Generate recurring task instances."""

        recurring_tasks = []

        for task in tasks:

            if not task.completed:
                continue

            if task.frequency.lower() == "daily":

                recurring_tasks.append(
                    Task(
                        task.title,
                        task.duration,
                        task.priority,
                        task.due_time,
                        "Daily"
                    )
                )

            elif task.frequency.lower() == "weekly":

                recurring_tasks.append(
                    Task(
                        task.title,
                        task.duration,
                        task.priority,
                        task.due_time,
                        "Weekly"
                    )
                )

        return recurring_tasks