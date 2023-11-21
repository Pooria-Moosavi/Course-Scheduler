import random
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
def create_closer_schedule(courses, teachers, course_to_teacher, teacher_):
    schedule = []
    teacher_info = {teacher: {'classes': 0, 'workdays': 0, 'credits': 10} for teacher in teachers}
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
    time_slots = [f'{i} - {i + 2}' for i in range(8, 18, 2) if i != 12]  # Exclude the 12-14 time slot

    teacher_info = {teacher: {'classes': 0, 'workdays': 0, 'credits': 10} for teacher in teachers}

    # Loop through each course to schedule their classes
    for course, course_info in courses.items():
        credits = course_info['credits']

        # Check if the course is explicitly defined in course_to_teacher
        if course in course_to_teacher:
            assigned_teachers = course_to_teacher.get(course, [])
            if not isinstance(assigned_teachers, list):
                assigned_teachers = [assigned_teachers]

            # Calculate the total number of timeslots needed for the course
            total_timeslots = 2 if credits == 3 else 1

            for teacher in assigned_teachers:
                if teachers[teacher]['credits'] >= credits and len(teachers[teacher]['workdays']) <= 3:
                    # Check if the teacher has enough credits for the entire course
                    if teachers[teacher]['credits'] >= total_timeslots:
                        teachers[teacher]['credits'] -= total_timeslots
                        teachers[teacher]['classes'] += total_timeslots

                        assigned_days = []
                        for _ in range(total_timeslots):
                            # Choose a day and time slot
                            day = random.choice(days)
                            time_slot = random.choice(time_slots)

                            # Check teacher unavailability
                            while day in teacher_unavailability.get(teacher, {}) and time_slot in \
                                    teacher_unavailability[teacher][day]:
                                day = random.choice(days)
                                time_slot = random.choice(time_slots)

                            assigned_days.append(day)

                            # Assign the course to the teacher
                            schedule.append([day, time_slot, course, random.choice(classes), teacher])

                        # Update teacher_info dictionary
                        teacher_info[teacher]['classes'] += total_timeslots
                        teacher_info[teacher]['workdays'] += len(set(assigned_days))
                        teacher_info[teacher]['credits'] = 10 - teachers[teacher]['credits']

                    else:
                        print(f"Skipping {course} for {teacher}. Insufficient credits.")
                else:
                    print(f"Skipping {course} for {teacher}. Insufficient credits or exceeds workday limit.")
        else:
            # Assign 1 class (1 timeslot) per teacher for 2-credit courses, 2 classes (2 timeslots) for 3-credit courses
            total_timeslots = 2 if credits == 3 else 1
            available_teachers = [t for t, info in teachers.items() if
                                  info['credits'] >= credits and len(info['workdays']) <= 3]

            if not available_teachers:
                print(f"No available teachers for {course}. Resetting teacher credits.")
                for t in teachers:
                    teachers[t]['credits'] = 10
                    teachers[t]['workdays'] = []
                available_teachers = list(teachers.keys())

            for _ in range(total_timeslots):
                # If it's a 3-credit course, assign 1 random teacher for 2 timeslots
                if credits == 3:
                    teacher = random.choice(available_teachers)
                    available_teachers.remove(teacher)
                else:
                    teacher = random.choice(available_teachers)

                teachers[teacher]['credits'] -= credits
                teachers[teacher]['classes'] += 1
                teachers[teacher]['workdays'].append(random.choice(days))

                day = teachers[teacher]['workdays'].pop(0)
                time_slot = random.choice(time_slots)
                schedule.append([day, time_slot, course, random.choice(classes), teacher])

    # Create a Pandas DataFrame for the entire schedule
    closer_df = pd.DataFrame(schedule, columns=['Day', 'TimeSlot', 'Course', 'Classroom', 'Teacher'])

    # Create a DataFrame for teacher information
    teacher_info_df = pd.DataFrame(
        [(teacher, info['classes'], info['workdays'], 10 - info['credits']) for teacher, info in teacher_info.items()],
        columns=['Teacher', 'Total Classes', 'Total Workdays', 'Remaining Credits'])

    # Save the closer schedule and teacher information to an Excel file with two sheets
    with pd.ExcelWriter('final.xlsx') as writer:
        closer_df.to_excel(writer, sheet_name='Closer Schedule', index=False)
        teacher_info_df.to_excel(writer, sheet_name='Teacher Info', index=False)


# Generate the schedule
create_closer_schedule(courses, teachers, course_to_teacher, teacher_unavailability)

