import streamlit as st

from scheduler import Owner, Pet, Task, Scheduler


# ===================================
# Page Configuration
# ===================================

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.caption("Pet Care Planning Assistant")


# ===================================
# Session State
# ===================================

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# ===================================
# Owner Information
# ===================================

st.header("Owner Information")

owner_name = st.text_input(
    "Owner Name",
    value="Jordan"
)

available_time = st.number_input(
    "Available Time (minutes)",
    min_value=10,
    max_value=1440,
    value=60,
    step=5
)

owner_preference = st.selectbox(
    "Scheduling Preference",
    [
        "Priority First",
        "Shortest Tasks First"
    ]
)


# ===================================
# Pet Information
# ===================================

st.header("Pet Information")

pet_name = st.text_input(
    "Pet Name",
    value="Mochi"
)

species = st.selectbox(
    "Species",
    [
        "Dog",
        "Cat",
        "Other"
    ]
)


# ===================================
# Pet Care Task Entry
# ===================================

st.header("Pet Care Tasks")

task_title = st.text_input(
    "Task Title",
    value="Morning Walk"
)

duration = st.number_input(
    "Duration (minutes)",
    min_value=1,
    max_value=240,
    value=20,
    step=1
)

priority = st.selectbox(
    "Priority",
    [
        "high",
        "medium",
        "low"
    ]
)


# ===================================
# Add / Clear Task Buttons
# ===================================

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "Add Task",
        use_container_width=True
    ):
        cleaned_title = task_title.strip()

        new_task = {
            "title": cleaned_title,
            "duration": int(duration),
            "priority": priority
        }

        duplicate = any(
            task["title"].lower() == cleaned_title.lower()
            and task["duration"] == int(duration)
            and task["priority"] == priority
            for task in st.session_state.tasks
        )

        if not cleaned_title:
            st.warning(
                "Please enter a task title."
            )

        elif duplicate:
            st.warning(
                "This task has already been added."
            )

        else:
            st.session_state.tasks.append(new_task)

            st.success(
                "Task added."
            )


with col2:
    if st.button(
        "Clear Tasks",
        use_container_width=True
    ):
        st.session_state.tasks = []
        st.rerun()


# ===================================
# Current Tasks
# ===================================

st.subheader("Current Tasks")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):

        task_col, delete_col = st.columns([5, 1])

        with task_col:
            st.write(
                f"• {task['title']} "
                f"({task['duration']} min) "
                f"[{task['priority']}]"
            )

        with delete_col:
            if st.button(
                "Delete",
                key=f"delete_{i}"
            ):
                st.session_state.tasks.pop(i)
                st.rerun()

else:
    st.info(
        "No tasks added yet."
    )


# ===================================
# Generate Schedule
# ===================================

st.divider()

if st.button(
    "Generate Schedule",
    type="primary",
    use_container_width=True
):

    # -------------------------------
    # Validation
    # -------------------------------

    if not owner_name.strip():
        st.warning(
            "Please enter the owner's name."
        )

    elif not pet_name.strip():
        st.warning(
            "Please enter the pet's name."
        )

    elif not st.session_state.tasks:
        st.warning(
            "Please add at least one pet care task "
            "before generating a schedule."
        )

    else:

        # -------------------------------
        # Create Owner
        # -------------------------------

        owner = Owner(
            owner_name.strip(),
            int(available_time),
            owner_preference
        )

        # -------------------------------
        # Create Pet
        # -------------------------------

        pet = Pet(
            pet_name.strip(),
            species
        )

        # -------------------------------
        # Convert Tasks
        # -------------------------------

        task_objects = [
            Task(
                task["title"],
                task["duration"],
                task["priority"]
            )
            for task in st.session_state.tasks
        ]

        # -------------------------------
        # Generate Schedule
        # -------------------------------

        scheduler = Scheduler()

        plan, skipped = scheduler.generate_plan(
            task_objects,
            owner
        )


        # ===================================
        # Daily Plan
        # ===================================

        st.header(
            f"Daily Plan for {pet.name}"
        )

        total_time = 0

        if plan:
            for task in plan:
                total_time += task.duration

                st.write(
                    f"✅ {task.title} "
                    f"({task.duration} min) "
                    f"[{task.priority}]"
                )

        else:
            st.info(
                "No tasks could be scheduled "
                "within the available time."
            )


        # ===================================
        # Schedule Summary
        # ===================================

        remaining_time = (
            int(owner.available_time)
            - total_time
        )

        st.write(
            f"**Total Scheduled Time:** "
            f"{total_time} minutes"
        )

        st.write(
            f"**Available Time:** "
            f"{owner.available_time} minutes"
        )

        st.write(
            f"**Remaining Time:** "
            f"{remaining_time} minutes"
        )


        # ===================================
        # Scheduling Explanation
        # ===================================

        st.subheader(
            "Scheduling Explanation"
        )

        st.write(
            f"Scheduling preference: "
            f"**{owner.preference}**"
        )

        if owner.preference == "Priority First":
            st.write(
                "Tasks were ranked by priority. "
                "High-priority tasks were considered first, "
                "followed by medium-priority and "
                "low-priority tasks."
            )

        elif owner.preference == "Shortest Tasks First":
            st.write(
                "Tasks were ranked by duration. "
                "Shorter tasks were considered before "
                "longer tasks."
            )

        st.write(
            "Tasks were added to the daily plan "
            "as long as they fit within the owner's "
            "available time."
        )


        # ===================================
        # Skipped Tasks
        # ===================================

        if skipped:
            st.subheader(
                "Skipped Tasks"
            )

            for task in skipped:
                st.write(
                    f"❌ {task.title} "
                    f"({task.duration} min) "
                    f"[{task.priority}] "
                    f"— insufficient remaining time"
                )

        else:
            st.success(
                "All pet care tasks fit "
                "within the available time."
            )