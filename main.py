from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("Joanne")

# Create pets
dog = Pet("Luna", "Dog", 4)
cat = Pet("Milo", "Cat", 2)

# Create tasks OUT OF ORDER for sorting test
task1 = Task(
    1,
    "Brush Fur",
    "18:00",
    15,
    "Weekly"
)

task2 = Task(
    2,
    "Morning Walk",
    "08:00",
    20,
    "Daily"
)

task3 = Task(
    3,
    "Breakfast",
    "08:00",
    10,
    "Daily"
)

# Add tasks to pets
dog.add_task(task2)
dog.add_task(task3)

cat.add_task(task1)

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler()

scheduler.add_pet(dog)
scheduler.add_pet(cat)

# ---------------------------------
# Sort Tasks
# ---------------------------------

print("SORTED TASKS")
print("-" * 30)

for pet_name, task in scheduler.sort_by_time():

    print(
        f"{task.due_time} | "
        f"{pet_name} | "
        f"{task.description}"
    )

# ---------------------------------
# Completed Task Test
# ---------------------------------

task1.mark_complete()

print("\nCOMPLETED TASKS")
print("-" * 30)

for pet_name, task in scheduler.filter_completed():

    print(
        f"{pet_name} | "
        f"{task.description}"
    )

# ---------------------------------
# Filter By Pet
# ---------------------------------

print("\nTASKS FOR LUNA")
print("-" * 30)

for pet_name, task in scheduler.filter_by_pet("Luna"):

    print(
        f"{task.description} "
        f"at {task.due_time}"
    )

# ---------------------------------
# Conflict Detection
# ---------------------------------

print("\nCONFLICT WARNINGS")
print("-" * 30)

conflicts = scheduler.check_conflicts()

if conflicts:

    for conflict in conflicts:
        print(conflict)

else:
    print("No conflicts detected.")

# ---------------------------------
# Recurring Tasks
# ---------------------------------

print("\nRECURRING TASKS")
print("-" * 30)

new_tasks = scheduler.generate_recurring_tasks()

if new_tasks:

    for task in new_tasks:

        print(
            f"Created new recurring task: "
            f"{task.description}"
        )

else:
    print("No recurring tasks generated.")