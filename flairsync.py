import csv
import praw
import json
from os import path

def templates_from_csv(path):
    f = csv.reader(file(path))
    # skip header row
    f.next()
    return [(r[0], r[1], csv_bool(r[2])) for r in f]

def csv_bool(value):
    # interpret a string as a boolean in the same way that the server does for
    # CGI parameters
    value = value.lower()
    if not value or value[0] in 'fn' or value == 'off':
        return False
    return True

# Read configuration file
dir = path.dirname(__file__)
config_data = open(path.join(dir, "config.json"), "r")
config = json.load(config_data)
config_data.close()

r = praw.Reddit(config['reddit']['user_agent'])
r.login(config['reddit']['username'], config['reddit']['password'])
subreddit = config['reddit']['subreddit']

print 'Parsing csv file ...'
csv_templates = templates_from_csv('flair.csv')

print 'Clearing flair templates ...'
r.get_subreddit(subreddit).clear_flair_templates()

for text, css_class, text_editable in csv_templates:
    print 'Adding flair templates: %r, %r, %r' % (
        text, css_class, text_editable)
    count = 0
    while count < 3:
        try:
            r.get_subreddit(subreddit).add_flair_template(text=text, css_class=css_class)

        except:
            count += 1
        else:
            break

print 'Done!'
