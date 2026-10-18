# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

- Owner stores information about the pet owner and manages multiple pets.
- Pet stores pet information such as name, species, age, and assigned tasks.
- Task represents a pet care activity with information such as description, due time, duration, frequency, and completion status.
- Scheduler acts as the main scheduling engine responsible for sorting, filtering, conflict detection, and recurring task generation.

This design followed object-oriented programming principles by assigning a specific responsibility to each class and keeping scheduling logic separate from data storage.

### b. Design changes

My design changed during implementation. Initially, the scheduler only created a simple daily plan based on available time and priority. Later, I expanded the Scheduler class to include sorting by time, filtering tasks by completion status and pet name, recurring task generation, and conflict detection.

I also added task completion tracking and recurrence support because these features made the application more realistic and aligned better with the project requirements.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler considers several constraints:

- Available owner time
- Task duration
- Task due time
- Task completion status
- Task frequency
- Scheduling conflicts

The most important constraints were due time and available time because they directly affect whether a task can fit into a daily schedule. I also considered completion status so users could separate completed and incomplete tasks.

### b. Tradeoffs

One tradeoff my scheduler makes is that conflict detection only checks for exact time matches rather than overlapping durations.

For example, if one task starts at 8:00 AM and another also starts at 8:00 AM, the scheduler flags a conflict. However, if one task runs from 8:00 AM to 8:30 AM and another runs from 8:15 AM to 8:45 AM, the conflict is not detected.

This tradeoff is reasonable because it keeps the implementation simple, easy to understand, and efficient while still providing useful scheduling warnings.

---

## 3. AI Collaboration

### a. How you used AI

I used AI throughout the project for:

- UML brainstorming and system design
- Creating class skeletons
- Debugging Python errors
- Improving Streamlit integration
- Designing scheduling algorithms
- Creating automated tests
- Generating documentation and README content

The most helpful prompts were questions about object-oriented design, scheduling algorithms, Streamlit session state management, and testing strategies. AI was especially useful when troubleshooting errors and connecting the backend logic to the user interface.

### b. Judgment and verification

One situation where I did not accept an AI suggestion directly was during the scheduling implementation. Some suggestions added more complexity than the project required. Instead of using a more advanced scheduling algorithm, I simplified the logic to focus on the project requirements.

I verified AI-generated code by running the application, testing the functionality manually, and using pytest to confirm the expected behavior.

---

## 4. Testing and Verification

### a. What you tested

I tested several important behaviors:

- Task creation
- Task completion
- Adding tasks to pets
- Sorting tasks by time
- Filtering completed and incomplete tasks
- Conflict detection for duplicate times
- Recurring task generation

These tests were important because they verify the core scheduling functionality and ensure that the application's main features work correctly.

### b. Confidence

I am highly confident that the scheduler works correctly for the project's required functionality.

The test suite verifies the most important behaviors, and I also validated the results manually through both the command-line demo and the Streamlit interface.

If I had more time, I would test additional edge cases such as:

- Invalid time formats
- Very large task lists
- Multiple pets with overlapping schedules
- Empty task lists
- Tasks with zero duration
- More advanced overlapping-duration conflict detection

---
