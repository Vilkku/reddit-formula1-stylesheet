# Stylesheet for [/r/Formula1](http://www.reddit.com/r/formula1)

This collection of scripts receives a notice from GitHub whenever this repository is updated, pulls and minifies the CSS file contained within and finally pushes the minified version to reddit. Reddit has a size limit on CSS files that is checked before their own minifying, so by pre-minifying the subreddit stylesheet additional space is gained.

This is what I wrote in a comment on reddit explaining this project:

> Copy the file config.json.sample to config.json. Replace the values in the file with reddit account details and a user agent string (just something like "Bot for subreddit X by /u/whatever").

> The file webhook.php is the file that receives the push from GitHub. This file has to be somewhere accessible from the web, which means that your probably have to move the file somewhere else. In that file there are two variables, $home and $secret.

> $home should be set to your "home" directory (actually it should be set to the directory where the directory for the script is, so calling it home isn't really correct), in my case it's set to /home/users/vilkku.

> $secret is for authenticating with GitHub. What you need to do is to go to your project settings, then under Webhooks & Services add a webhook with the Payload URL set to wherever the wehbook.php file is (publicly accessible URL), content set to application/json and secret set to whatever you want, but the same as $secret variable in webhook.php and finally to check the box active to set it as active.

> The next piece of the puzzle is the webhook.sh file. This is just a shell script that gets executed by the webhook.php file that changes into the correct directory, does a git pull, executes [rCSSmin](http://opensource.perlig.de/rcssmin/) and finally executes webhook.py. Many things here are awfully hardcoded, it makes the assumption that the project folder resides in your home directory and uses a specific Python installation that I have set up.

> The final piece in this pretty tangled mess is webhook.py, but you shouldn't have to do anything with this file - it uses the values from config.json. One thing to mention though is that it uses [PRAW](https://praw.readthedocs.org/), so you need to install that as well.
