author = 'Clock Bot'

calendar = {
    # A - A Day
    # B - B Day
    # C - School Closed/Holidays
    # S - Teacher in-Service Day (no school for students)
    # T - Testing Day - Full Day
    # H - Homeroom / First day of school
    # L - Last day of school
    2021: {
        12: {
            10: 'B',
            13: 'A',
            14: 'T',
            15: 'T',
            16: 'T',
            17: 'T',
            20: 'C',
            21: 'C',
            22: 'C',
            23: 'C',
            24: 'C',
            27: 'C',
            28: 'C',
            29: 'C',
            30: 'C'
        }
    },
    2022: {
        1: {
            3: 'C',
            4: 'T',
            5: 'B',
            6: 'A',
            7: 'B',
            10: 'A',
            11: 'B',
            12: 'A',
            13: 'B',
            14: 'A',
            17: 'C',
            18: 'B',
            19: 'A',
            20: 'B',
            21: 'A',
            24: 'B',
            25: 'A',
            26: 'B',
            27: 'A',
            28: 'B'
        },
        2: {
            1: 'B',
            2: 'A',
            3: 'B',
            4: 'A',
            7: 'C',
            8: 'B',
            9: 'A',
            10: 'B',
            11: 'A',
            14: 'B',
            15: 'A',
            16: 'B',
            17: 'A',
            18: 'B',
            21: 'C',
            22: 'A',
            23: 'B',
            24: 'A',
            25: 'B',
            28: 'A'
        },
        3: {
            1: 'T',
            2: 'B',
            3: 'A',
            4: 'B',
            7: 'A',
            8: 'B',
            9: 'A',
            10: 'B',
            11: 'A',
            14: 'C',
            15: 'B',
            16: 'A',
            17: 'B',
            18: 'A',
            21: 'B',
            22: 'A',
            23: 'B',
            24: 'A',
            25: 'B',
            28: 'A',
            29: 'B',
            30: 'A',
            31: 'B'
        },
        4: {
            1: 'A',
            4: 'B',
            5: 'A',
            6: 'B',
            7: 'A',
            8: 'B',
            11: 'C',
            12: 'C',
            13: 'C',
            14: 'C',
            15: 'C',
            18: 'C',
            19: 'A',
            20: 'B',
            21: 'A',
            22: 'B',
            25: 'S',
            26: 'A',
            27: 'B',
            28: 'A',
            29: 'B'
        },
        5: {
            2: 'A',
            3: 'B',
            4: 'A',
            5: 'B',
            6: 'A',
            9: 'B',
            10: 'A',
            11: 'B',
            12: 'A',
            13: 'B',
            16: 'A',
            17: 'B',
            18: 'A',
            19: 'B',
            20: 'T',
            23: 'T',
            24: 'T',
            25: 'T'
        },
        8: {}
    }
}

days = {
    # key times for each type of school day
    # Day
    # Date
    # Period
    # Time
    'A': {
        '7:00': {'text-time': 'Period 1', 'author': author, 'title': 'Welcome'},
        '8:25': {'text-time': 'Period 1', 'author': author, 'title': 'Have a nice day'},
        '8:30': {'text-time': 'Period 3', 'author': author, 'title': 'Welcome'},
        '9:55': {'text-time': 'Period 3', 'author': author, 'title': 'Have a nice day'},
        '10:00': {'text-time': 'Period 5', 'author': author, 'title': 'Welcome'},
        '11:30': {'text-time': 'Period 5', 'author': author, 'title': 'Have a nice day'},
        '11:31': {'text-time': 'Lunch 3', 'author': author, 'title': 'Why are you here'},
        '11:55': {'text-time': 'Lunch 3', 'author': author, 'title': 'Go to class'},
        '12:00': {'text-time': 'Period 7', 'author': author, 'title': 'Welcome'},
        '13:25': {'text-time': 'Period 7', 'author': author, 'title': 'Have a nice day'}
    },
    'B': {
        '7:00': {'text-time': 'Period 2', 'author': author, 'title': 'Welcome'},
        '8:25': {'text-time': 'Period 2', 'author': author, 'title': 'Have a nice day'},
        '8:30': {'text-time': 'Period 4', 'author': author, 'title': 'Welcome'},
        '9:55': {'text-time': 'Period 4', 'author': author, 'title': 'Have a nice day'},
        '10:00': {'text-time': 'Period 6', 'author': author, 'title': 'Welcome'},
        '11:30': {'text-time': 'Period 6', 'author': author, 'title': 'Have a nice day'},
        '11:31': {'text-time': 'Lunch 3', 'author': author, 'title': 'Why are you here'},
        '11:55': {'text-time': 'Lunch 3', 'author': author, 'title': 'Go to class'},
        '12:00': {'text-time': 'Period 8', 'author': author, 'title': 'Welcome'},
        '13:25': {'text-time': 'Period 8', 'author': author, 'title': 'Have a nice day'}
    },
    'C': {
        '7:00': {'text-time': 'Why are you here?', 'author': author, 'title': 'School\'s closed'}
    },
    'H': {
        '7:00': {'text-time': 'Welcome to school!','author': author, 'title': 'Ms. Haley'}
    },
    'L': {
        '7:00': {'text-time': 'Last day of school!', 'author': author, 'title': 'Congrats!'}
    },
    'S': {
        '7:00': {'text-time': 'Time for busy work!', 'author': author, 'title': 'You can do it!'}
    },
    'T': {
        '7:00': {'text-time': 'Take your tests!', 'author': author, 'title': 'Good luck!'}
    }
}