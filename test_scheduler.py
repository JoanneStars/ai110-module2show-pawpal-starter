from scheduler import Owner, Task, Scheduler


def test_task_creation():
    """Verify a task is created correctly."""

    task = Task(
        "Walk",
        20,
        "high",
        "08:00",
        "Daily"
    )

    assert task.title == "Walk"
    assert task.duration == 20
    assert task.priority == "high"
    assert task.due_time == "08:00"
    assert task.frequency == "Daily"


def test_generate_plan():
    """Verify scheduler respects available time."""

    owner = Owner(
        "Joanne",
        30,
        "Priority First"
    )

    tasks = [
        Task(
            "Walk",
            20,
            "high",
            "08:00",
            "Daily"
        ),
        Task(
            "Vet Visit",
            20,
            "medium",
            "09:00",
            "Once"
        )
    ]

    scheduler = Scheduler()

    plan, skipped = scheduler.generate_plan(
        tasks,
        owner
    )

    assert len(plan) == 1
    assert len(skipped) == 1


def test_sort_by_time():
    """Verify tasks are sorted chronologically."""

    tasks = [
        Task(
            "Brush Fur",
            15,
            "low",
            "18:00",
            "Weekly"
        ),
        Task(
            "Morning Walk",
            20,
            "high",
            "08:00",
            "Daily"
        ),
        Task(
            "Breakfast",
            10,
            "medium",
            "09:00",
            "Daily"
        )
    ]

    scheduler = Scheduler()

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].title == "Morning Walk"
    assert sorted_tasks[1].title == "Breakfast"
    assert sorted_tasks[2].title == "Brush Fur"


def test_task_completion():
    """Verify mark_complete changes status."""

    task = Task(
        "Dinner",
        15,
        "medium",
        "18:00",
        "Daily"
    )

    task.mark_complete()

    assert task.completed is True


def test_conflict_detection():
    """Verify duplicate times are detected."""

    tasks = [
        Task(
            "Morning Walk",
            20,
            "high",
            "08:00",
            "Daily"
        ),
        Task(
            "Breakfast",
            10,
            "medium",
            "08:00",
            "Daily"
        )
    ]

    scheduler = Scheduler()

    conflicts = scheduler.check_conflicts(tasks)

    assert len(conflicts) == 1


def test_recurring_task_generation():
    """Verify completed recurring tasks generate a new task."""

    task = Task(
        "Brush Fur",
        15,
        "low",
        "18:00",
        "Weekly"
    )

    task.mark_complete()

    scheduler = Scheduler()

    recurring = scheduler.generate_recurring_tasks(
        [task]
    )

    assert len(recurring) == 1
    assert recurring[0].title == "Brush Fur"