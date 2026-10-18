# AI Interactions Log

> **Stretch features only.** Document AI-assisted work completed beyond the core project requirements.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent to make multi-step changes autonomously.

### What task did you give the agent?

I asked the AI assistant to help extend my PawPal+ scheduling system by implementing smarter scheduling features. The goal was to add task sorting, filtering, recurring task support, conflict detection, improved Streamlit integration, automated testing, and README documentation updates.

### What did the agent do?

The AI assistant helped perform several multi-step tasks:

- Reviewed my existing class structure
- Suggested improvements to the UML design
- Updated the `Task` class to support task completion and recurrence
- Added sorting algorithms for scheduling tasks by time
- Added filtering methods for completed and incomplete tasks
- Added conflict detection logic to identify duplicate task times
- Suggested updates to `main.py` for algorithm verification
- Generated automated pytest test cases
- Assisted with Streamlit session state integration
- Generated README and reflection content

### What did you have to verify or fix manually?

I reviewed all generated code before using it.

Several AI-generated suggestions required modification because they introduced more complexity than the project required. I simplified portions of the scheduling system to better fit the assignment requirements and verified functionality by:

- Running the CLI demo (`main.py`)
- Running automated tests with pytest
- Testing the Streamlit UI manually
- Reviewing output formatting and scheduling behavior

Human verification was necessary to ensure the final design remained readable, maintainable, and aligned with project goals.

---

## Prompt Comparison (SF11)

> Compare two different prompts on the same task.

|  | Option A | Option B |
|----|----|----|
| **Model / tool used** | Microsoft Copilot | Microsoft Copilot |
| **Prompt** | "Create a scheduling algorithm that prioritizes tasks by priority level." | "Create a scheduling algorithm that sorts tasks by time and detects conflicts." |
| **Response summary** | Generated a priority-based scheduling algorithm that schedules high-priority tasks first. | Generated time-based sorting logic and a conflict detection system using matching task times. |
| **What was useful** | Helped organize tasks based on importance and available time. | Added smarter scheduling features that improved usability and task management. |
| **Problems noticed** | Did not consider task timing or scheduling conflicts. | Did not initially consider task duration overlaps and required refinement. |
| **Decision** | Kept portions of the priority-ranking algorithm. | Adopted the sorting and conflict detection approach because it better matched project requirements. |

### Which approach did you use in your final implementation and why?

I used a combination of both approaches. The final version of PawPal+ uses priority-based scheduling for planning tasks while also incorporating time-based sorting, task filtering, recurring task generation, and conflict detection. This combined approach provided the most useful scheduling behavior while keeping the implementation relatively simple and easy to understand.