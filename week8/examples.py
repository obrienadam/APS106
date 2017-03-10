inventory = ['pickles', 'medpack', 'cards', 'unknown']
last_item = inventory[-1]

items = [('eggs', 10), ('oranges', 34), ('apples', 12)]

nums = {-4, -3, 1, 2, 3, 4, -2, -8}
negative_nums = {-3, -1, -4, -9}
nums_subset = nums.intersection(negative_nums)

my_first_dictionary = {'Name': 'George',
                       'Favourite Programming Language': 'Python',
                       'Age': 27,
                       32: 'I don\'t know what this key would mean, but it\'s allowed'}

print('What is George\'s favourite programming language?:', my_first_dictionary['Favourite Programming Language'])

# Empty dictionary
agents = {}

# Create an agent
agent = {
    'name': 'James Bond',
    'clearance': 34,
    'license': 'to kill',
    'agency': 'MI-6'
}

# Add the agent to the agents dictionary
agents['007'] = agent

# Create another agent
agent = {
    'name': 'Jason Bourne',
    'clearance': 23,
    'agency': 'CIA'
}

# Add the agent to the agents dictionary
agents['Delta One'] = agent

print(agents['Delta One']['name'], 'has clearance', agents['Delta One']['clearance'])
print(agents['007']['name'], 'has clearance', agents['007']['clearance'])

