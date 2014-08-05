import praw
import json
from os import path

# Read configuration file
dir = path.dirname(__file__)
config_data = open(path.join(dir, "config.json"), "r")
config = json.load(config_data)
config_data.close()

# Reddit login
r = praw.Reddit(config['reddit']['user_agent'])
r.login(config['reddit']['username'], config['reddit']['password'])

# Update the stylesheet
dir = path.dirname(__file__)
stylesheet = open(path.join(dir, "style.min.css"), "r")
r.get_subreddit("formula1").set_stylesheet(stylesheet)

stylesheet.close()
