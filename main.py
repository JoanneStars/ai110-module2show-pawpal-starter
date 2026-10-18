from scheduler import Owner, Pet, Task, Scheduler

owner = Owner(
    "Joanne",
    45,
    "Priority First"
)

dog = Pet("Luna", "Dog")
cat = Pet("Milo", "Cat")

tasks = [
    Task("Morning Walk", 20, "high"),
    Task("Breakfast", 10, "medium"),
    Task("Brush Fur", 30, "low")
]

scheduler = Scheduler()

plan, skipped = scheduler.generate_plan(
    tasks,
    owner
)

print("TODAY'S SCHEDULE")
print("-" * 30)

for task in plan:
    print(
        f"{task.title} "
        f"({task.duration} min) "
        f"[{task.priority}]"
    )

print("\nSKIPPED TASKS")
print("-" * 30)

if skipped:
    for task in skipped:
        print(
            f"{task.title} "
            f"({task.duration} min) "
            f"[{task.priority}]"
        )
else:
    print("None")