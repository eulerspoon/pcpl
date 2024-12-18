from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests

def main():
    N = 14

    rectangle = Rectangle(N, N, "blue")
    circle = Circle(N, "green")
    square = Square(N, "red")

    print(rectangle)
    print(circle)
    print(square)

    response = requests.get('https://api.github.com')
    print(response.status_code)

if __name__ == "__main__":
    main()
