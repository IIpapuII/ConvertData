from flask import Blueprint, render_template, request, redirect, url_for

home_site = Blueprint('home_site', __name__, url_prefix='/')

@home_site.route('/')
def home():
    return render_template('home.html')