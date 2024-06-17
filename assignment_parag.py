def calculate_sphere_volume(radius):
    volume = (4 / 3) * (3.14) * (radius ** 3)
    return volume


def calculate_cube_volume(side):
    return side ** 3


def calculate_cylinder_volume(height, radius):
    return 3.14 * radius ** 2 * height


def main():
    while True:
        print(
            "Welcome to Volume Calculator\nWhich shape's volume would you like to calculate?\n1. Sphere\n2. Cube\n3. Cylinder\n4. Exit")
        try:
            selection = int(input("Enter the number from the list: "))

            if selection == 1:
                while True:
                    try:
                        radius = float(input("Enter the radius of the sphere: "))
                        print("Volume of the sphere is:", calculate_sphere_volume(radius))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

            elif selection == 2:
                while True:
                    try:
                        side = float(input("Enter the side length of the cube: "))
                        print("Volume of the cube is:", calculate_cube_volume(side))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

            elif selection == 3:
                while True:
                    try:
                        height = float(input("Enter the height of the cylinder: "))
                        radius = float(input("Enter the radius of the cylinder: "))
                        print("Volume of the cylinder is:", calculate_cylinder_volume(height, radius))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

            elif selection == 4:
                print("Thank you! Run again.")
                break

            else:
                print("Please enter a valid number from the list.")

        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
