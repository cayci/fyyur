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

data = []

for region in regions:
  venues_data = Venue.query.filter_by(city=region.city,   state=region.state).order_by('id').all()
  venues = []
  for venue in venues_data:
    venues.append({"id": venue.id,
                   "name": venue.name,
                   "num_upcoming_shows": len(venue.shows)})
        
    data.append({
      "city": region.city,
      "state": region.state,
      "venues": venues
    })  

pprint(data)

#for region in regions:
#    venues = Venue.query.filter_by(city=region.city, #state=region.state).order_by('id').all()
#    print(len(venues[0].shows))