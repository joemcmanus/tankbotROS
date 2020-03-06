#!/usr/bin/env python
# File    : server.py  - a web interface to display coding vulnerabilities
# Author  : Joe McManus joe.mcmanus@canonical.com
# Version : 0.1  03/02/2020 Joe McManus
# Copyright (C) 2020 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, Markup, request, make_response, escape, render_template
import rospy 
from std_msgs.msg import String
import threading 

app = Flask(__name__)

threading.Thread(target=lambda:  rospy.init_node('talker', disable_signals=True, anonymous=True)).start()
pub = rospy.Publisher('/command', String, queue_size=10)
        

@app.route("/")
def index():
    titleText = "Python Robot Examples"
    bodyText = Markup(
        """
    <a href=/drive/1> Forward </a><br>
    <a href=/drive/2> Back </a><br>
    <a href=/drive/3> Left </a><br>
    <a href=/drive/4> Right </a><br>
    """
    )
    return render_template("templatecss.html", bodyText=bodyText, titleText=titleText)


@app.route("/drive/<urlDir>/")
def drive(urlDir):
    titleText = "Drive the bot"
    if urlDir == "1":
        direction = "Forward"
        link = "/drive/1"
    if urlDir == "2":
        direction = "Back"
        link = "/drive/2"
    if urlDir == "3":
        direction = "Left"
        link = "/drive/3"
    if urlDir == "4":
        direction = "Right"
        link = "/drive/4"
    pub.publish(direction)

    bodyText = Markup(
        "Moving " + direction + "<br> <a href=" + link + ">" + direction + "</a><br>"
    )
    return render_template("templatecss.html", bodyText=bodyText, titleText=titleText)

@app.route('/about')
def about():
    titleText="About"
    bodyText=Markup('''A simple flask app to show using Flask and ROS <br>
    <br> Source code can be found at : <a href=https://github.com/joemcmanus/tankbotROS> github </a> <br>
    <br><br>
    Thanks - Joe 
    ''')
    return render_template('templatecss.html', bodyText=bodyText, titleText=titleText)


if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True, host="0.0.0.0", port=8080)
