from scheduler import Owner, Task, Scheduler


def test_task_creation():
    task = Task(
        "Walk",
        20,
        "high"
    )

    assert task.title == "Walk"
    assert task.duration == 20
    assert task.priority == "high"


def test_generate_plan():
    owner = Owner(
        "Joanne",
        30,
        "Priority First"
    )

    tasks = [
        Task("Walk", 20, "high"),
        Task("Vet Visit", 20, "medium")
    ]

    scheduler = Scheduler()

    plan, skipped = scheduler.generate_plan(
        tasks,
        owner
    )

    assert len(plan) == 1
    assert len(skipped) == 1