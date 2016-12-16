# import subprocess
import json
import random

# Parse a page using Scrapy
# https://docs.python.org/3/library/subprocess.html
# def parse(scrapper_file, output_file):
#     subprocess.run(["rm", "-rf", output_file])
#     subprocess.run(["scrapy", "runspider", scrapper_file, "-o", output_file])

# Give a Json file and return a Dictionary
def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

# Give a json and return a list
def clean_strings(sentences):
    cleaned = []
    # Store quotes on a list. Create an empty list and add each sentence one by one.
    for sentence in sentences:
        # Clean quotes from whitespace and so on
        clean_sentence = sentence.strip()
        # don't use extend as it adds each letter one by one!
        cleaned.append(clean_sentence)
    return cleaned

# Return a random item in a list
def random_item_in(object_list):
    rand_numb = random.randint(0, len(object_list))
    return object_list[rand_numb]


#####################
###### QUOTES #######
#####################

# Gather quotes from San Antonio

def random_quote():
    json_quotes = read_values_from_json('s_a.json', 'quote')
    quotes = clean_strings(json_quotes)
    return random_item_in(quotes)

######################
#### CHARACTERS ######
######################

# Gather characters from Wikipedia

def random_character():
    json_characters = read_values_from_json('characters.json', 'character')
    characters = clean_strings(json_characters)
    return random_item_in(characters)


######################
#### INTERACTION ######
######################

# Print a random sentence.

def random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def interaction():
    message = ('Would you like another true quote? Type [enter]. '
               'To exit, type [B]. To launch the scrapper again, type [C]')
    choice = input(message).upper()
    if choice == 'B':
        quit()
    elif choice == 'C':
        # parse('san_antonio_scrapper.py', 's_a.json')
        # parse('characters_scrapper.py', 'characters.json')
        pass
    else:
        random_sentence()
        interaction()

if __name__ == '__main__':
    random_sentence()
    interaction()
