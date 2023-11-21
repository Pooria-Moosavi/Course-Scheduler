Course Schedule Generator

This Python script generates a class schedule for a set of courses, classrooms, and teachers. The schedule is created considering teacher availability, credits for each course, and the workday limit for each teacher.

## Requirements

- Python 3.x
- pandas library (`pip install pandas`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Pooria-Moosavi/Course-Scheduler
    ```

2. Run the script:

    ```bash
    python schedule_generator.py
    ```

3. Check the output:

    The generated schedule will be saved in an Excel file named `final.xlsx` with two sheets: 'Closer Schedule' and 'Teacher Info'.

## Configuration

Adjust the following variables in the script to customize the schedule generation:

- `courses`: Define the courses, their credits, and the assigned groups.
- `classes`: List of available classrooms.
- `teachers`: Information about teachers, including their credits, classes, and workdays.
- `course_to_teacher`: Mapping of courses to the teachers responsible.
- `teacher_unavailability`: Specify days and time slots when teachers are unavailable.
- `days`: List of weekdays.

Feel free to modify the script according to your specific requirements. If you encounter any issues or have suggestions, please [create an issue](https://github.com/Pooria-Moosavi/Course-Scheduler/issues)
(Heads up: there are few issues in this code for example in teachers dictionary, days counterdoesnt work properly)

Happy scheduling!
