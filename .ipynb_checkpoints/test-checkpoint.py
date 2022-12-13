import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from config import *
from models import *
from pprint import pprint

regions = Venue.query.distinct(Venue.city, Venue.state).all()

print(regions[0])

#for region in regions:
#    venues = Venue.query.filter_by(city=region.city, #state=region.state).order_by('id').all()
#    print(len(venues[0].shows))