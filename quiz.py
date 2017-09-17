# coding: utf-8
# author: Kevin Wing <kevinrwing@gmail.com>
# date created: 7/12/17
# date modified: 9/17/17

quiz_table = {
    # dictionary containing the possible quizes based on difficulty.
    'easy': '''
    Sonny, true love is the __1__ thing, in the world -
    except for a nice MLT - __2__, lettuce and tomato sandwich,
    where the __2__ is nice and lean and the tomato is __3__.
    They're so __4__, I love that.
    ''',
    'medium': '''
    You fell victim to one of the classic __1__-the most famous of which is,
    "Never get involved in a land war in __2__"-but only slightly less well-known is this:"
    Never go against a __3__, when __4__ is on the line"!
    Ha ha ha ha ha ha ha! Ha ha ha ha ha ha ha! Ha ha ha...[thunk].
    ''',
    'hard': '''
    Westley: To the __1__ means the first thing you will lose will be your feet below the ankles.
    Then your hands at the wrists. Next your __2__.

    Prince Humperdinck: And then my __3__ I suppose, I killed you too quickly the last time.
    A mistake I don't mean to duplicate tonight.

    Westley: I wasn't finished. The next thing you will lose will be your left eye followed by your right.

    Prince Humperdinck: And then my __4__, I understand let's get on with it.

    Westley: Wrong! Your __4__ you keep and I'll tell you why.
    So that every shriek of every child at seeing your hideousness will be yours to cherish.
    Every babe that weeps at your approach, every woman who cries out, "Dear God! What is that thing?",
    will echo in your perfect __4__. That is what to the __1__ means. It means I leave you in anguish,
    wallowing in __5__ misery forever.
    '''
}

answer_table = {
    # dictionary containing dictionaries of the answers based on difficulty.
    'easy': {
        '1': 'greatest',
        '2': 'mutton',
        '3': 'ripe',
        '4': 'perky'
    },
    'medium': {
        '1': 'blunders',
        '2': 'Asia',
        '3': 'Sicilian',
        '4': 'death'
    },
    'hard': {
        '1': 'pain',
        '2': 'nose',
        '3': 'tongue',
        '4': 'ears',
        '5': 'freakish'
    }
}


def set_difficulty(message):
    '''
    Takes a string as input to display to the user when prompting them to choose a difficulty.
    Checks if user input exists in the dict of quizes.
    Returns the user input if it finds in quiz_table else it will call itself prompting for a correct choice.
    '''
    user_input = raw_input(message).lower()
    if user_input in quiz_table:
        return user_input
    else:
        return set_difficulty('Please choose from easy, medium or hard: ')


def set_num_tries(message):
    '''
    Takes a string as input as message to user for how many guesses they want for each question.
    Attempts conversion of input to integer value. If successful returns user input converted to integer else will
    call itself until a valid integer is entered.
    '''
    try:
        user_input = int(raw_input(message))
    except Exception:
        user_input = set_num_tries('Please enter a valid number: ')
    return user_input


def get_user_answer(question_num):
    '''
    Takes current integer value(question_num) as input and prompts the user for the answer to that question.
    Returns answer formatted to lowercase.
    '''
    message = '\nWhat should replace __{0}__? '.format(question_num)
    user_answer = raw_input(message).lower()
    return user_answer


def display_output(question_num, quiz, message, tries_left=1):
    '''
    Takes 4 inputs: the current question number, the selected quiz, a message depending on
    current status of quiz and number of tries left with a default of 1.
    Set default to allow for less ambiguity in setting tries_left.
    tries_left should be set everytime you call display_output().
    '''
    return '''
    You are on question: {0}

    {1}

    {2}

    You have {3} tries left on this question!
    '''.format(question_num, quiz, message, tries_left)


def proc_string(input_string, question_number, answer):
    '''
    Takes the old quiz string (input_string) and replaces the string version
    of the current question_number and stores it in placeholder and replaces that
    with the answer.
    Returns the new quiz string with the answer replacing the placeholder.
    '''
    placeholder = '__' + str(question_number) + '__'
    return input_string.replace(placeholder, answer)


def check_answer(question_num, answer_key):
    '''
    Takes the current question number (question_num) and the dict of the answers (answer_key).
    Calls get_user_answer passing in the current question number. Loops through answer_key and tests
    each key against the question number. returns the value of the key if they match or returns False if no
    match is found.
    '''
    answer = get_user_answer(question_num)
    for key, val in answer_key.items():
        if str(question_num) == key:
            # print val.lower(), answer
            if val.lower() == answer:
                return val
            else:
                return False
        else:
            continue
    return False


def run_quiz(difficulty, allowed_tries, quiz, answer_key):
    '''
    Core function that handles most of the quiz.
    Takes difficlty(string), allowed_tries(int), quiz(string), answer_key(dict).
    Prints a final display_output and returns a string depending on if you got
    all answers correct or failed too many attempts.
    '''
    tries, question_num, message = 0, 1, ''
    while question_num <= len(answer_key):
        if tries < allowed_tries:
            print display_output(question_num, quiz, message, tries_left=allowed_tries - tries)
            answer = check_answer(question_num, answer_key)
            if answer:
                quiz = proc_string(quiz, question_num, answer)
                question_num += 1
                tries, message = 0, 'Correct!'
            else:
                message = 'Incorrect! Please try again!'
                tries += 1
            result = '\nYou Won! :-)\n'
        else:
            result = '\nYou Lost! :-(\n'
            break
    print display_output(question_num, quiz, message, tries_left=allowed_tries)
    return result


def play_game():
    '''
    Main function of quiz. Called to begin program.
    Prompts for difficulty(string), allowed_tries(int).
    Sets selected quiz and answer_key and runs quiz and stores final result stating whether you have won or lost.
    prints result at end.
pyp    '''
    print '\nWelcome!\nToday we are going to test your knowledge of the greatest movie ever made:\nThe Princess Bride'
    difficulty = set_difficulty('\nPlease choose difficulty.\neasy/medium/hard: ')
    allowed_tries = set_num_tries('\nHow many tries do you want: ')
    quiz = quiz_table[difficulty]
    answer_key = answer_table[difficulty]
    result = run_quiz(difficulty, allowed_tries, quiz, answer_key)
    print result


play_game()
