from scheduler import Owner, Task, Scheduler


def test_priority_order():
    owner = Owner(
        "Jordan",
        60,
        "Priority First"
    )

    tasks = [
        Task("Play Time", 10, "low"),
        Task("Medication", 10, "high"),
        Task("Brush Fur", 10, "medium")
    ]

    scheduler = Scheduler()

    plan, skipped = scheduler.generate_plan(
        tasks,
        owner
    )

    assert plan[0].priority == "high"
    assert plan[1].priority == "medium"
    assert plan[2].priority == "low"


def test_time_limit():
    owner = Owner(
        "Jordan",
        30,
        "Priority First"
    )

    tasks = [
        Task("Morning Walk", 20, "high"),
        Task("Feed Pet", 15, "medium")
    ]

    scheduler = Scheduler()

    plan, skipped = scheduler.generate_plan(
        tasks,
        owner
    )

    total_time = sum(
        task.duration for task in plan
    )

    assert total_time <= owner.available_time
    assert len(skipped) == 1


def test_preference_priority():
    owner = Owner(
        "Jordan",
        60,
        "Shortest Tasks First"
    )

    tasks = [
        Task("Long Walk", 30, "high"),
        Task("Feed Pet", 5, "medium"),
        Task("Play", 15, "low")
    ]

    scheduler = Scheduler()

    plan, skipped = scheduler.generate_plan(
        tasks,
        owner
    )

    assert plan[0].duration == 5
    assert plan[1].duration == 15
    assert plan[2].duration == 30