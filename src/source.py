import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from time import sleep
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

def find_midpoint(P1: Point, P2: Point) -> Point:
    midpoint = Point((P1.x + P2.x) / 2, (P1.y + P2.y) / 2)
    return midpoint

def divideBezier(P0, P1, P2, iterations):
    # print(f"1: {P0},2 : {P1}, 3: {P2}\n")
    if iterations == 0:
        return [P0,P2]
    else:
        q0 = find_midpoint(P0, P1)
        q1 = find_midpoint(P1, P2)
        r0 = find_midpoint(q0, q1)

        curve_left = divideBezier(P0, q0, r0, iterations - 1)
        curve_right = divideBezier(r0, q1, P2, iterations - 1)

        return curve_left + curve_right[1:]
    
def bfBezier(P0:Point, P1:Point, P2:Point, iterations):
    curve = [P0]
    for t in range(1, iterations + 1):
        t /= (iterations + 1)
        x = (1 - t) ** 2 * P0.x + 2 * (1 - t) * t * P1.x + t ** 2 * P2.x
        y = (1 - t) ** 2 * P0.y + 2 * (1 - t) * t * P1.y + t ** 2 * P2.y
        curve.append(Point(x, y))
    curve.append(P2)
    return curve

def update(frame,P0,P1,P2,iterations,option,pauses):
    plt.clf()
    plot_curve(frame,P0,P1,P2,option)
    plt.scatter(*zip((P0.x, P0.y), (P1.x, P1.y), (P2.x, P2.y)), c='red', label='Titik Kontrol', marker='o')

    plt.legend()
    plt.title(f"Quadratic Bézier Curve - Iterasi {frame}/{iterations}")
    if pauses:
        plt.pause(1.5)

def plot_curve(iteration,P0,P1,P2,method : str):
    if method == 'D' or method == 'd':
        curve_points = divideBezier(P0, P1, P2, iteration)
        x = [point.x for point in curve_points]
        y = [point.y for point in curve_points]
        plt.plot(x, y,marker='D', label='Iterasi Sekarang')
    elif method == 'b' or method == 'B':
        curve_points = bfBezier(P0, P1, P2, iteration)
        x = [point.x for point in curve_points]
        y = [point.y for point in curve_points]
        plt.plot(x, y,marker='D', label='Iterasi Sekarang')
    else :
        print("Input tidak dikenali.\n")

def callInput():
    P0x = float(input(f"Koordinat-X P0: "))
    P0y = float(input(f"Koordinat-Y P0: "))
    P1x = float(input(f"Koordinat-X P1: "))
    P1y = float(input(f"Koordinat-Y P1: "))
    P2x = float(input(f"Koordinat-X P2: "))
    P2y = float(input(f"Koordinat-Y P2: "))
    P0 = Point(P0x, P0y)
    P1 = Point(P1x, P1y)
    P2 = Point(P2x, P2y)
    iterations = int(input("Jumlah Iterasi: "))
    print("\nPilih B untuk metode BruteForce dan D untuk divide and conquer\n")
    option = str(input("Metode Pembentukan Kurva Bezier: "))
    pause = str(input("Apakah animasi ingin dijeda perdetik(y/n): "))
    if pause == 'y' or pause == 'Y' :
        pauses = True
    else :
        pauses = False
    return P0,P1,P2,iterations,option,pauses

def printWellcome():
    print(r'''
 _______                       __                             ______                                                            ______                                                     __                         
|       \                     |  \                           /      \                                                          /      \                                                   |  \\                        
| $$$$$$$\  ______   ________  \$$  ______    ______        |  $$$$$$\ __    __   ______  __     __   ______    _______       |  $$$$$$\  ______   _______    ______    ______   ______  _| $$_     ______    ______  
| $$__/ $$ /      \ |        \|  \ /      \  /      \       | $$   \$$|  \  |  \ /      \|  \   /  \ /      \  /       \      | $$ __\$$ /      \ |       \  /      \  /      \ |      \|   $$ \   /      \  /      \ 
| $$    $$|  $$$$$$\ \$$$$$$$$| $$|  $$$$$$\|  $$$$$$\      | $$      | $$  | $$|  $$$$$$\\$$\ /  $$|  $$$$$$\|  $$$$$$$      | $$|    \|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$\\
| $$$$$$$\| $$    $$  /    $$ | $$| $$    $$| $$   \$$      | $$   __ | $$  | $$| $$   \$$ \$$\  $$ | $$    $$ \$$    \       | $$ \$$$$| $$    $$| $$  | $$| $$    $$| $$   \$$/      $$ | $$ __ | $$  | $$| $$   \$$ \\
| $$__/ $$| $$$$$$$$ /  $$$$_ | $$| $$$$$$$$| $$            | $$__/  \| $$__/ $$| $$        \$$ $$  | $$$$$$$$ _\$$$$$$\      | $$__| $$| $$$$$$$$| $$  | $$| $$$$$$$$| $$     |  $$$$$$$ | $$|  \| $$__/ $$| $$      
| $$    $$ \$$     \|  $$    \| $$ \$$     \| $$             \$$    $$ \$$    $$| $$         \$$$    \$$     \|       $$       \$$    $$ \$$     \| $$  | $$ \$$     \| $$      \$$    $$  \$$  $$ \$$    $$| $$      
 \$$$$$$$   \$$$$$$$ \$$$$$$$$ \$$  \$$$$$$$ \$$              \$$$$$$   \$$$$$$  \$$          \$      \$$$$$$$ \$$$$$$$         \$$$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$ \$$       \$$$$$$$   \$$$$   \$$$$$$  \$$                                                                                                                                                                                                                    
    ''')
    sleep(1)
    print(r''' 
    ______                                  __               
    |      \                                |  \              
    \$$$$$$ _______    ______   __    __  _| $$_          __ 
    | $$  |       \  /      \ |  \  |  \|   $$ \        |  \
    | $$  | $$$$$$$\|  $$$$$$\| $$  | $$ \$$$$$$         \$$
    | $$  | $$  | $$| $$  | $$| $$  | $$  | $$ __        __ 
    _| $$_ | $$  | $$| $$__/ $$| $$__/ $$  | $$|  \      |  \
    |   $$ \| $$  | $$| $$    $$ \$$    $$   \$$  $$       \$$
    \$$$$$$ \$$   \$$| $$$$$$$   \$$$$$$     \$$$$           
                    | $$                                    
                    | $$                                    
                    \$$                                    
    ''')

