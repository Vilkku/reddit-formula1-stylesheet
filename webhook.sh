#!/bin/bash

cd ~/reddit-formula1-stylesheet && git pull && ~/python27/bin/python -mrcssmin <style.css >style.min.css && ~/python27/bin/python webhook.py
