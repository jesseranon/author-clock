import random 
from datetime import datetime #for testing
from school_calendar import default_title, default_author
# generate random time quote for times that don't exist in time-quotes csv
# generate special messages according to class days

numbers = {
    0: ['0', 'o\'clock'],
    1: ['1', 'one'],
    2: ['2', 'two'],
    3: ['3', 'three'],
    4: ['4', 'four'],
    5: ['5', 'five'],
    6: ['6', 'six'],
    7: ['7', 'seven'],
    8: ['8', 'eight'],
    9: ['9', 'nine'],
    10: ['10', 'ten'],
    11: ['11', 'eleven'],
    12: ['12', 'twelve'],
    13: ['13', 'thirteen'],
    14: ['14', 'fourteen'],
    15: ['15', 'fifteen', 'a quarter'],
    16: ['16', 'sixteen'],
    17: ['17', 'seventeen'],
    18: ['18', 'eighteen'],
    19: ['19', 'nineteen'],
    20: ['20', 'twenty'],
    30: ['30', 'thirty'],
    40: ['40', 'forty'],
    50: ['50', 'fifty']
}


def generate_time_quote(s):
    # print(f"{default_title} {default_author}")
    quote = {'text-time': '', 'text': '', 'title': default_title, 'author': default_author}

    formatting = {
        'until': ['it', 'until', 'hours'], 
        'after': ['it', 'after', 'hours'], 
        'numbers': ['it', 'hours']
    }
    words = {
        'it': {
            'The time': {'is': ['is now', 'is', 'now reads', 'has come upon']},
            'It': {'is': ['is', 'is now']},
            'The clock': {'is': ['reads', 'now reads', 'has struck', 'strikes', 'chimes']}
        },
        'until': ['to', 'until'],
        'after': ['past', 'after'],
        'am': ['am', ['in the morning', 'this morning', 'this fine morning']],
        'pm': ['pm', ['in the afternoon', 'this afternoon', 'this fine afternoon']]
    }
    #choose formatting
    f = random.choice(list(formatting.keys()))

    h = int(s[:s.find(':')])
    m = int(s[s.find(':')+1:])

    t = '' #text
    tt = '' #text-time

    if m > 0 and f == 'until':
        h += 1
        if m > 0:
            m = 60 - m

    if h >= 12:
        formatting[f].append('pm')
        if h > 12:
            h -= 12
    else:
        formatting[f].append('am')

    if f == 'numbers':
        if len(str(m)) < 2:
            m = '0' + str(m)
        words.update({
            'hours': [f"{h}:{m}"]
        })
    else:
        # randomly choose whether hours is a number or word
        h = random.choice(numbers[h])
        # if m == 0, randomly choose whether to append o'clock to hours
        if m == 0:
            if random.choice(numbers[m]) == 'o\'clock':
                h = str(h) + ' ' + 'o\'clock'
        else:
        # randomly choose whether minutes is a number or word
            mins = ''
            try:
                mins += f"{random.choice(numbers[m])}"
            except KeyError:
            # # if word, generate proper wording for two-digit minutes
                if random.choice([0,1]) > 0:
                    # generate word format
                    tens = m - (m % 10)
                    m -= tens
                    mins = f"{numbers[tens][1]}-{numbers[m][1]}"
                else:
                    mins = m
        # choose whether to concatenate ' minutes'
        if random.choice([0,1]) > 0:
            if int(m) > 1:
                mins = str(mins) + " minutes"
            else:
                mins = str(mins) + " minute"
        words.update({
            'minutes': [mins]
        })
        words.update({
            'hours': [h]
        })

        formatting[f].insert(1, 'minutes')
    
    ttl = formatting[f][slice(1,len(formatting[f]))]

    for w in formatting[f]:
        try:
            if w == 'it':
                c = random.choice(list(words[w].keys()))
                t += c + ' ' + random.choice(words[w][c]['is'])
            elif type(words[w]) == list:
                c = random.choice(words[w])
                while type(c) == list:
                    c = random.choice(c)
                t += ' ' + str(c)
            if w in ttl:
                tt += str(c) + ' '
        except KeyError:
            continue
    t += '.'
    tt = tt[0:len(tt)-1]
    quote.update({
        'text-time': tt,
        'text': t
    })

    # print(quote)
    return quote

# # TESTING BELOW THIS LINE
# now = datetime.now()
# hour = now.hour
# minute = now.minute
# def time_string(h,m):
#     if len(str(m)) < 2:
#         m = '0' + str(m)
#     return f"{h}:{m}"

# times = time_string(hour,minute)

# generate_time_quote(times)