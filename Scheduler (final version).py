import numpy as np
import pandas as pd

# Define the courses, classes, and teachers
courses = {
    'inter-finance': {'credits': 2, 'group': 'G1'},
    'Islamic-finance': {'credits': 2, 'group': 'G1'},
    'economic-evaluation': {'credits': 3, 'group': 'G1'},
    'e1': {'credits': 2, 'group': 'G1'},
    'e2': {'credits': 2, 'group': 'G1'},
    'islam-iran': {'credits': 2, 'group': 'G1'},
    'indust-eco': {'credits': 2, 'group': 'G2'},
    'recources-eco': {'credits': 2, 'group': 'G2'},
    'research methods': {'credits': 2, 'group': 'G2'},
    'public-eco2': {'credits': 2, 'group': 'G2'},
    'eco-system': {'credits': 2, 'group': 'G2'},
    'money-eco': {'credits': 2, 'group': 'G2'},
    'iran-2': {'credits': 2, 'group': 'G2'},
    'micro-financing': {'credits': 2, 'group': 'G2'},
    'econometrics1': {'credits': 3, 'group': 'G3'},
    'macro3': {'credits': 3, 'group': 'G3'},
    'micro3': {'credits': 3, 'group': 'G3'},
    'eco-history': {'credits': 3, 'group': 'G3'},
    'development': {'credits': 3, 'group': 'G3'},
    'fegh-h eghtesadi': {'credits': 2, 'group': 'G3'},
    'micro1': {'credits': 3, 'group': 'G4'},
    'macro1': {'credits': 3, 'group': 'G4'},
    'stats2': {'credits': 3, 'group': 'G4'},
    'math2': {'credits': 3, 'group': 'G4'},
    'islamic-economy': {'credits': 2, 'group': 'G4'},
    'financial management': {'credits': 2, 'group': 'G2'},
}

classes = ['Classroom1', 'Classroom2', 'Classroom3', 'Classroom4', 'Classroom5',
           'Classroom6', 'Classroom7', 'Classroom8', 'Classroom9', 'Classroom10']

# Create a dictionary of teachers and their available credits
teachers = {
    'teacher1': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher2': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher3': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher4': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher5': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher6': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher7': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher8': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher9': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher10': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher11': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher12': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher13': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher14': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher15': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher16': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher17': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher18': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher19': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher20': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher21': {'credits': 10, 'classes': 0, 'workdays': []},
    'teacher22': {'credits': 10, 'classes': 0, 'workdays': []}
}


course_to_teacher = {
    'inter-finance': ['teacher1'],
    'Islamic-finance': ['teacher2'],
    'economic-evaluation': ['teacher3', 'teacher4'],
    'indust-eco': ['teacher5'],
    'recources-eco': ['teacher6', 'teacher7'],
    'research methods': ['teacher8', 'teacher9'],
    'public-eco2': ['teacher10', 'teacher11'],
    'eco-system': ['teacher12'],
    'money-eco': ['teacher13'],
    'iran-2': ['teacher14'],
    'econometrics1': ['teacher15', 'teacher4', 'teacher7'],
    'macro3': ['teacher11', 'teacher3', 'teacher1'],
    'micro3': ['teacher9', 'teacher8'],
    'eco-history': ['teacher10'],
    'fegh-h eghtesadi': ['teacher5'],
    'micro1': ['teacher6', 'teacher4', 'teacher12'],
    'macro1': ['teacher13', 'teacher14', 'teacher15'],
    'stats2': ['teacher5']
}

# Define teacher availability
teacher_unavailability = {
    'teacher1': {'Saturday': ['8 - 10'], 'Sunday': ['8 - 10'], 'Monday': ['8 - 10'], 'Tuesday': ['8 - 10'], 'Wednesday': ['8 - 10']},
    'teacher10': {'Tuesday': ['14 - 16']}
    # Add availability for other teachers as needed
}

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']

# Define a function to create a schedule with courses grouped closely
def create_schedule(courses, teachers, course_to_teacher, teacher_unavailability):
    schedule = []
    teacher_info = {teacher: {'classes': 0, 'workdays': set(), 'credits': 10} for teacher in teachers}
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
    time_slots = [f'{i} - {i + 2}' for i in range(8, 18, 2) if i != 12]  # Exclude the 12-14 time slot

    teacher_info = {teacher: {'classes': 0, 'workdays': set(), 'credits': 10} for teacher in teachers}

    # Group courses based on the 'group' attribute
    grouped_courses = {}
    for course, course_info in courses.items():
        group = course_info.get('group', '')
        grouped_courses.setdefault(group, []).append((course, course_info))

    # Loop through each group of courses
    for group, group_courses in grouped_courses.items():
        group_schedule = {}  # Temporary schedule for the group to check overlaps
        for course, course_info in group_courses:
            credits = course_info['credits']
            assigned_teachers = course_to_teacher.get(course, [])

            # Calculate the total number of timeslots needed for the course
            total_timeslots = 2 if credits == 3 else 1

            for teacher in assigned_teachers:
                if teachers[teacher]['credits'] >= credits and len(teachers[teacher]['workdays']) <= 3:
                    # Check if the teacher has enough credits for the entire course
                    if teachers[teacher]['credits'] >= total_timeslots:
                        teachers[teacher]['credits'] -= total_timeslots
                        teachers[teacher]['classes'] += total_timeslots

                        assigned_days = []
                        assigned_time_slots = []
                        for i in range(total_timeslots):
                            # Choose a day and time slot using numpy
                            available_days = set(days)
                            if credits == 3 and i == 1:
                                # For the second class of 3-credit courses, exclude the day of the first class
                                available_days.discard(assigned_days[0])

                            day = np.random.choice(list(available_days))
                            time_slot = np.random.choice(time_slots)

                            # Check teacher unavailability
                            while day in teacher_unavailability.get(teacher, {}) and time_slot in \
                                    teacher_unavailability[teacher][day]:
                                day = np.random.choice(list(available_days))
                                time_slot = np.random.choice(time_slots)

                            # Check for overlaps with other courses in the group or the teacher
                            while (day, time_slot) in group_schedule.get(teacher, []) or any(
                                    (day, time_slot) == (sched[0], sched[1]) for sched in schedule if sched[4] == teacher
                            ):
                                day = np.random.choice(list(available_days))
                                time_slot = np.random.choice(time_slots)

                            assigned_days.append(day)
                            assigned_time_slots.append(time_slot)

                        # Assign the course to the teacher in the final schedule
                        for day, time_slot in zip(assigned_days, assigned_time_slots):
                            schedule.append([day, time_slot, course, np.random.choice(classes), teacher])
                            group_schedule.setdefault(teacher, []).append((day, time_slot))

                            # Update teacher_info dictionary
                            teacher_info[teacher]['classes'] += 1
                            teacher_info[teacher]['workdays'].add(day)
                            teacher_info[teacher]['credits'] = 10 - teachers[teacher]['credits']

                    else:
                        print(f"Skipping {course} for {teacher}. Insufficient credits.")
                else:
                    print(f"Skipping {course} for {teacher}. Insufficient credits or exceeds workday limit.")

    # Reschedule within assigned days if workdays count exceeds 3
    for teacher, info in teacher_info.items():
        if len(info['workdays']) > 3:
            assigned_days = list(info['workdays'])
            np.random.shuffle(assigned_days)  # Shuffle the days

            for i in range(len(info['workdays']) - 3):
                # Find a suitable day and time slot
                day = assigned_days[i]
                time_slot = np.random.choice(time_slots)

                while any(
                        (day, time_slot) == (sched[0], sched[1]) for sched in schedule if sched[4] == teacher
                ):
                    day = assigned_days[i]
                    time_slot = np.random.choice(time_slots)

                # Assign the course to the teacher in the final schedule
                schedule.append([day, time_slot, list(courses.keys())[-1], np.random.choice(classes), teacher])

    # Create a Pandas DataFrame for the entire schedule
    closer_df = pd.DataFrame(schedule, columns=['Day', 'TimeSlot', 'Course', 'Classroom', 'Teacher'])

    # Create a DataFrame for teacher information
    teacher_info_df = pd.DataFrame(
        [(teacher, info['classes'], len(info['workdays']), 10 - info['credits']) for teacher, info in teacher_info.items()],
        columns=['Teacher', 'Total Classes', 'Total Workdays', 'Remaining Credits'])

    # Save the closer schedule and teacher information to an Excel file with two sheets
    with pd.ExcelWriter('Course-Schedule.xlsx') as writer:
        closer_df.to_excel(writer, sheet_name='Schedule', index=False)
        teacher_info_df.to_excel(writer, sheet_name='Teacher Info', index=False)

# Generate the schedule
create_schedule(courses, teachers, course_to_teacher, teacher_unavailability)
