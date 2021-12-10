#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
import time
import speech_recognition as sr

# this method will make the robot move to the goal location
def move_to_goal(xGoal, yGoal,angle):
    # define a client for to send goal requests to the move_base server through a SimpleActionClient
    ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    # wait for the action server to come up
    while (not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()

    # set up the frame parameters
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # moving towards the goal*/

    goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = angle
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal location ...")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(120))

    if (ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("You have reached the destination")
        return True

    else:
        rospy.loginfo("The robot failed to reach the destination")
        return False

standby = True
state = 0
x_goal1 = 2.582
x_goal2 = -0.85
x_goal3 = -4.354
y_goal1 = 1.224
y_goal2 = -1.943
angle1 = 2.43
angle2 = -2.43
x0 = 4.627
y0 = 0.0
angle0 = 3.066
station = ["1","2","3","4","5","6"]
goal = []
def stt():
    try:
        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=4)
            text = r.recognize_google(audio)
    except:
        text = "Cannot hear"
        pass
    return text

def move(station):
    if station == "1":
        move_to_goal(x_goal1, y_goal1,angle1)
        print('one')
        time.sleep(5)
    if station == "2":
        move_to_goal(x_goal2, y_goal1, angle1)
        print('two')
        time.sleep(5)
    if station == "3":
        move_to_goal(x_goal3, y_goal1, angle1)
        print('three')
        time.sleep(5)
    if station == "4":
        move_to_goal(x_goal3, y_goal2, angle2)
        print('four')
        time.sleep(5)
    if station == "5":
        move_to_goal(x_goal2, y_goal2, angle2)
        print('five')
        time.sleep(5)
    if station == "6":
        move_to_goal(x_goal1, y_goal2, angle2)
        print('six')
        time.sleep(5)
    if station == "home":
        move_to_goal(x0, y0, angle0)
        print('home')
        rospy.spin()

if __name__ == '__main__':
    while standby == True :
        rospy.init_node('map_navigation', anonymous=False)
        r = sr.Recognizer()
        if state == 0 :
            print("Standby")
            Text = stt()
            if "turn on" in Text:
                state = 1
        if state >= 1 and state <= 4 :
            print("Where do you want me go?")
            Text = stt()
            if Text == 'Cannot hear' :
                state += 1
            else:
                for i in range(len(station)):
                    if station[i] in Text:
                        goal.append(station[i])
                print(goal)
        if goal:
            for i in range(len(goal)):
                move(goal[i])
            move("home")
            state = 0
        if state > 4:
            "Bye bye"
            state = 0

