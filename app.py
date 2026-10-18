import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

# ===================================
# Page Configuration
# ===================================

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.caption("Smart Pet Care Management System")

# ===================================
# Session State
# ===================================

if "owner" not in st.session_state:
    st.session_state.owner = None

if "pets" not in st.session_state:
    st.session_state.pets = []

if "selected_pet" not in st.session_state:
    st.session_state.selected_pet = None

# ===================================
# Owner Information
# ===================================

st.header("Owner Information")

owner_name = st.text_input(
    "Owner Name",
    value="Joanne")

# ===================================
# Pet Information
# ===================================

st.header("Add Pet")

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

age = st.number_input(
    "Age",
    min_value=0,
    max_value=30,
    value=1
)

if st.button("Add Pet"):

    if pet_name.strip():

        new_pet = Pet(
            pet_name.strip(),
            species,
            age
        )

        st.session_state.pets.append(new_pet)

        st.success(
            f"{pet_name} added successfully!"
        )

    else:

        st.warning(
            "Please enter a pet name."
        )

# ===================================
# View Pets
# ===================================

st.subheader("Saved Pets")

if st.session_state.pets:

    pet_names = [
        pet.name
        for pet in st.session_state.pets
    ]

    selected_name = st.selectbox(
        "Choose a Pet",
        pet_names
    )

    for pet in st.session_state.pets:

        if pet.name == selected_name:
            st.session_state.selected_pet = pet

        st.write(
            f"🐾 {pet.name} "
            f"({pet.species}, Age {pet.age})"
        )

else:

    st.info(
        "No pets added yet."
    )

# ===================================
# Task Entry
# ===================================

st.header("Add Task")

task_description = st.text_input(
    "Task Description",
    value="Morning Walk"
)

task_time = st.text_input(
    "Time (HH:MM)",
    value="08:00"
)

duration = st.number_input(
    "Duration (minutes)",
    min_value=1,
    max_value=240,
    value=20
)

frequency = st.selectbox(
    "Frequency",
    [
        "Once",
        "Daily",
        "Weekly"
    ]
)

if st.button("Add Task to Selected Pet"):

    if st.session_state.selected_pet is None:

        st.warning(
            "Please add and select a pet first."
        )

    else:

        task = Task(
            id=len(
                st.session_state.selected_pet.tasks
            ) + 1,
            description=task_description,
            due_time=task_time,
            duration_mins=duration,
            frequency=frequency
        )

        st.session_state.selected_pet.add_task(task)

        st.success(
            "Task added successfully."
        )

# ===================================
# Display Tasks
# ===================================

st.header("Current Tasks")

if st.session_state.selected_pet:

    if st.session_state.selected_pet.tasks:

        table_data = []

        for task in st.session_state.selected_pet.tasks:

            table_data.append(
                {
                    "Task": task.description,
                    "Time": task.due_time,
                    "Duration": task.duration_mins,
                    "Frequency": task.frequency,
                    "Completed": task.is_completed
                }
            )

        st.table(table_data)

    else:

        st.info(
            "No tasks assigned yet."
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
    
    if not owner_name.strip():
        st.warning(
            "Please enter an owner name."
        )

    elif not st.session_state.pets:
        st.warning("Please add at least one")