# scheduler.py


class Owner:
    def __init__(self, name, available_time, preference):
        self.name = name
        self.available_time = int(available_time)
        self.preference = preference


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Task:
    def __init__(self, title, duration, priority):
        self.title = title
        self.duration = int(duration)
        self.priority = priority


class Scheduler:
    def __init__(self):
        # Used to rank priorities
        self.priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

    def generate_plan(self, tasks, owner):
        """
        Create a schedule based on the owner's preference
        and available time.

        Returns:
            plan: tasks that fit in the schedule
            skipped: tasks that could not fit
        """

        # Make a copy so the original list is not changed
        ranked_tasks = list(tasks)

        # -----------------------------------
        # Rank Tasks
        # -----------------------------------

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

        # -----------------------------------
        # Build Schedule
        # -----------------------------------

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