"""Name: Kaala Bajo
lab3.py

Problem: This program summarizes vehicle data for a number of roads.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

def traffic():
    road_num = eval(input("How many roads were surveyed? "))
    vehicle_total = 0

    for roads in range(road_num):  #Gets number of days road was observed
        print("How many days was road", roads + 1, "surveyed? ")
        roadx_days = eval(input())

        road_acc = 0
        for days in range(roadx_days): #Gets number of cars traveled on a given day
            print("\t How many cars traveled on day", days + 1, "? ")
            road_acc = road_acc + eval(input("\t"))
        vehicle_total = vehicle_total + road_acc

        print("Road", roads + 1, "averaged", road_acc/roadx_days, "vehicles per day \n")

    print("Total number of vehicles traveled on all roads:", vehicle_total)
    print("Average number of vehicles per road:", round((vehicle_total/road_num), 2))