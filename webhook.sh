#!/bin/bash

(cd ~/reddit-formula1-stylesheet && git pull)
~/python27/bin/python -mrcssmin <~/reddit-formula1-stylesheet/style.css >~/reddit-formula1-stylesheet/style.min.css
#~/python27/bin/python ~/reddit-formula1-stylesheet/webhook.py
