import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def find_midpoint(P1: Point, P2: Point) -> Point:
    midpoint = Point((P1.x + P2.x) / 2, (P1.y + P2.y) / 2)
    return midpoint

def bezier_curve(P, iterations):
    curve = [P[0]]
    for t in range(1, iterations + 1):
        t /= (iterations + 1)
        x = (1 - t) ** 2 * P[0].x + 2 * (1 - t) * t * P[1].x + t ** 2 * P[2].x
        y = (1 - t) ** 2 * P[0].y + 2 * (1 - t) * t * P[1].y + t ** 2 * P[2].y
        curve.append(Point(x, y))
    curve.append(P[2])
    return curve

def plot_bezier_curve(points):
    # Plot titik kontrol
    x_coords = [point.x for point in points]
    y_coords = [point.y for point in points]
    plt.plot(x_coords, y_coords, 'bo-', label='Titik Kontrol')

    # Plot kurva Bézier
    bezier_points = bezier_curve(points, iterations=1)  # Ubah iterasi sesuai kebutuhan
    bezier_x = [point.x for point in bezier_points]
    bezier_y = [point.y for point in bezier_points]
    plt.plot(bezier_x, bezier_y, 'r-', label='Kurva Bézier')

    # Menambahkan label dan legenda
    plt.title('Kurva Bézier')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # Menampilkan plot
    plt.grid(True)
    plt.show()

# Contoh penggunaan
P0 = Point(1, 1)
P1 = Point(2, 4)
P2 = Point(3, 1)  # Titik kontrol

plot_bezier_curve([P0, P1, P2])
