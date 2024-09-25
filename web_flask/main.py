#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)

# laming page
@app.route('/landingpage', strict_slashes=False)
def landingpage():
    return render_template('landingpage.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')