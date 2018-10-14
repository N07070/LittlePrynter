#!/usr/bin/python

import os, random, sys, json
from datetime import datetime
from subprocess import call
from Adafruit_Thermal import *
from flask import Flask, render_template, jsonify, make_response, request, redirect, url_for, abort, session, flash
from flask_limiter import Limiter
from pprint import pprint
from flask_limiter.util import get_remote_address



app = Flask(__name__)
app.secret_key = b'\x98>3nW[D\xa4\xd4\xd0K\xab?oM.`\x98'
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# session['logged_in'] = False

def error_handler_limiter():
    flash("Trop de requêtes !!! CANNOT PRINT !!! HAAAAAAAAAA",'dark')
    return redirect(url_for('display_index_page'))

@app.errorhandler(418)
def i_m_a_tea_pot(error):
    return make_response('☕\n', 418)

@app.route('/tea')
def tea():
    abort(418)

@app.route('/')
@limiter.exempt
def display_index_page():
    if session.get('logged_in'):
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
@limiter.limit("100 per minute", error_message=error_handler_limiter)
def login():
    if request.method == 'POST':
        if not session.get('logged_in'):
            if request.form['username'] and request.form['password']:
                # Get the json
                with open('users.json') as f:
                    users_file = json.load(f)
                for user in users_file["users"]:
                    if users_file["users"][user] == request.form['password']:
                        session['logged_in'] = True
                        session['user'] = request.form['username']

                if not session.get('logged_in'):
                    flash('Mot de passe ou pseudo invalide.','danger')
                    return redirect(url_for('login'))
                else:
                    return redirect(url_for('display_index_page'))
            else:
                flash('Incorrect logins')
                return render_template('password.html')
        else:
            return render_template('password.html')
    else:
        return render_template('password.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    flash('Tu est déconnecté', 'info')
    return redirect(url_for('login'))

@app.route('/print/image')
@limiter.limit("5 per minute", error_message=error_handler_limiter)
def print_image():
    if session.get('logged_in'):
        img = random.choice(os.listdir("static/images/")) #change dir name to whatever
        call(["lp", "-o fit-to-page", "static/images/" + img])
        # printer = Adafruit_Thermal('/dev/serial0', 19200, timeout=5)
        # printer.begin()
        # printer.feed(1)
        # # printer.printImage(dickbutt, True)
        # # printer.feed(2)
        return redirect(url_for('display_index_page'))
    else:
        return redirect(url_for('login'))

@app.route('/print/text', methods=['POST'])
@limiter.limit("3: per minute", error_message=error_handler_limiter)
def print_text():
    if session.get('logged_in'):
        if len(request.form['message']) < 200:
            printer = Adafruit_Thermal('/dev/serial0', 19200, timeout=5)
            printer.begin()
            printer.justify('L')
            printer.println(request.form['message'])
            printer.setSize('S')
            printer.println(">> " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + session.get('user'))
            printer.justify('C')
            printer.println("------------------------------")
            printer.feed(2)
            printer.sleep()      # Tell printer to sleep
            printer.wake()       # Call wake() before printing again, even if reset
            printer.setDefault() # Restore printer to defaults
            return redirect(url_for('display_index_page'))
        else:
            flash('Le text est trop long, 200 caractères au maximum stp !')
            return redirect(url_for('display_index_page'))
    else:
        return redirect(url_for('login'))
