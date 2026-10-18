# PawPal+ (Module 2 Project)

PawPal+ is a Streamlit-based pet care management application that helps owners organize, prioritize, and schedule pet care activities. The system uses object-oriented programming and scheduling algorithms to manage tasks such as feeding, walking, grooming, medications, and appointments.

---

## Scenario

A busy pet owner needs help staying consistent with pet care. PawPal+ acts as a scheduling assistant that can:

- Track pet care tasks
- Organize daily responsibilities
- Detect scheduling conflicts
- Support recurring tasks
- Create a prioritized daily plan
- Display scheduling decisions clearly

---

## Features

### Owner Management
- Create an owner profile
- Store multiple pets for one owner

### Pet Management
- Add multiple pets
- Store species and age information
- Associate tasks with individual pets

### Task Management
- Create pet care tasks
- Assign due times
- Track task completion
- Support recurring tasks

### Smart Scheduling
- Sort tasks by time
- Filter tasks by pet
- Filter completed and incomplete tasks
- Detect scheduling conflicts
- Generate recurring tasks automatically

### Streamlit Interface
- Add pets through the browser
- Add pet care tasks
- View current tasks
- Generate schedules
- View scheduling warnings

---

## System Architecture

The application uses four primary classes:

### Owner
Stores owner information and manages pets.

### Pet
Stores pet information and assigned tasks.

### Task
Represents an individual pet care activity.

### Scheduler
Acts as the scheduling engine responsible for:

- Sorting tasks
- Filtering tasks
- Conflict detection
- Recurring task generation

---

## Getting Started

### Setup

```bash
python -m venv .venv

source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

### Run the CLI Demo

```bash
python main.py
```

---

## Sample CLI Output

```text
SORTED TASKS
------------------------------
08:00 | Luna | Morning Walk
08:00 | Luna | Breakfast
18:00 | Milo | Brush Fur

COMPLETED TASKS
------------------------------
Milo | Brush Fur

TASKS FOR LUNA
------------------------------
Morning Walk at 08:00
Breakfast at 08:00

CONFLICT WARNINGS
------------------------------
Conflict detected: Morning Walk and Breakfast are both scheduled at 08:00

RECURRING TASKS
------------------------------
Created new recurring task: Brush Fur
```

---

## Smarter Scheduling

### Task Sorting

Method:

```python
Scheduler.sort_by_time()
```

Tasks are sorted using Python's `sorted()` function and a lambda expression that uses the task time (`HH:MM`) as the sorting key.

### Task Filtering

Methods:

```python
Scheduler.filter_completed()
Scheduler.filter_incomplete()
Scheduler.filter_by_pet()
```

Allows users to:

- View completed tasks
- View incomplete tasks
- View tasks assigned to a specific pet

### Conflict Detection

Method:

```python
Scheduler.check_conflicts()
```

Identifies tasks scheduled at the same time and generates a warning instead of causing a runtime error.

Example:

```text
Conflict detected:
Morning Walk and Breakfast
are both scheduled at 08:00
```

### Recurring Tasks

Method:

```python
Scheduler.generate_recurring_tasks()
```

Completed tasks with Daily or Weekly frequencies automatically generate a new occurrence for future scheduling.

---

## Testing PawPal+

### Run the Test Suite

```bash
python -m pytest
```

### Test Coverage

The automated tests verify:

- Task creation
- Task completion
- Scheduler task sorting
- Conflict detection
- Recurring task generation
- Pet task assignment

### Sample Test Output

```text
===============================
3 passed in 0.05s
===============================
```

### Confidence Level

⭐⭐⭐⭐⭐ (5/5)

The system has been tested for its core scheduling functionality, including sorting, filtering, recurrence generation, and conflict detection.

---

## Demo Walkthrough

### Step 1

Launch the application:

```bash
streamlit run app.py
```

### Step 2

Enter owner information including:

- Owner name
- Scheduling preferences

### Step 3

Add one or more pets using the Add Pet form.

Example:

```text
Mochi
Species: Cat
Age: 2
```

### Step 4

Add tasks for your pets.

Example:

```text
Morning Walk
08:00
20 minutes
Daily
```

### Step 5

Generate a schedule.

PawPal+ will:

- Sort tasks chronologically
- Detect conflicts
- Display completed and incomplete tasks
- Generate recurring tasks when needed

### Step 6

Review warnings and scheduling recommendations displayed in the application.

---

## UML Diagram

### Initial UML

Located in:

```text
diagrams/uml_draft.mmd
```

### Final UML

Located in:

```text
diagrams/uml_final.mmd
```

Example relationships:

```text
Owner
 └── Pet
      └── Task

Scheduler
 ├── sort_by_time()
 ├── filter_completed()
 ├── filter_incomplete()
 ├── filter_by_pet()
 ├── check_conflicts()
 └── generate_recurring_tasks()
```

---

## Reflection Highlights

### Design Decision

I chose an object-oriented design using Owner, Pet, Task, and Scheduler classes because each class has a clear responsibility and can be expanded independently.

### Scheduling Tradeoff

The conflict detection algorithm checks for exact time matches only. This keeps the implementation simple and easy to understand but does not detect overlapping durations.

### AI Collaboration

AI was used to:

- Generate UML ideas
- Scaffold class structures
- Suggest scheduling algorithms
- Draft automated tests
- Review and refine implementation choices

Human oversight was used to verify correctness, simplify code, and keep the design aligned with project requirements.

---

## Author

Joanne Jongeling

CodePath AI110 Foundations of AI Engineering

Module 2 Project: PawPal+