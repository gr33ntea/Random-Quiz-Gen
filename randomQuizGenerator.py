#! python3
# RANDOM STATE CAPITAL QUIZ GENERATOR!

import random, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

filePath = 'C:\\Users\\User\\Documents\\PythonQuizzes'
quizPath = '\\quizzes'
keyPath = '\\keys'
if os.path.exists(filePath) == False:
    print("Required folder missing: 'PythonQuizzes'")
    print("Creating directory now...")
    os.makedirs(filePath)
    if os.path.exists(filePath + quizPath) == False:
        os.makedirs(filePath + quizPath)
    if os.path.exists(filePath + keyPath) == False:
        os.makedirs(filePath + keyPath)

for i in range(0, 35):
    print('Creating quizzes... (' + str(i + 1) + ' out of 35 created)')
    #TODO: Create the quiz and answer key files.
    quizName = 'quiz' + str(i + 1) + '.txt'
    keyName = 'key' + str(i + 1) + '.txt.'
    quizFile = open(filePath + quizPath + quizName, 'w')
    keyFile = open(filePath + keyPath + keyName, 'w')
    
    #TODO: Write out the header for the quiz.
    quizFile.write('Capitals Quiz (Version ' + str(i + 1) + ')\nName:\nDate:\n')
    
    #TODO: Shuffle the order of the states.
    keys = list(capitals.keys())
    random.shuffle(keys)
    shuffledCapitals = dict()
    for key in keys:
        shuffledCapitals.update({key:capitals[key]})

    #TODO: Loop through all 50 states, making a question for each.
    questionNumber = 1
    for state, capital in shuffledCapitals.items():
        quizFile.write('-'.center(10, '-'))
        quizFile.write('\n')
        quizFile.write(str(questionNumber) + '. What is the capital of ' + state + '?\n')
        questionNumber += 1
        choices = [capital]
        answers = ['A. ', 'B. ', 'C. ', 'D. ']
        for i in range(0, 3):
            randChoice = random.choice(list(shuffledCapitals.values()))
            if choices.count(randChoice) > 0 or choices.count(randChoice) < 0:
                randChoice = random.choice(list(shuffledCapitals.values()))
            choices.append(randChoice)
        random.shuffle(choices)
        printChoices = dict(zip(answers, choices))
        
        for k, v in printChoices.items():
            if v == capital:
                keyFile.write(str(questionNumber - 1) + ') ' + k + '\n')
            quizFile.write(k + v + '\n')
        quizFile.write('-'.center(10, '-'))
        quizFile.write('\n')
    quizFile.close()
    keyFile.close()
print('Quiz creation completed!\nGoodbye now.')
        
        
        
    
