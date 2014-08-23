import utils
import math

if __name__ == '__main__':
    a = {'x': 0, 'y': 0}
    b = {'x': 1, 'y': 1}

    r = utils.find_angle_of_point(a, b)
    if math.degrees( r ) != 45:
        print('Failed: ')
        print(str(math.degrees(r)))
        assert False

    r = utils.find_angle_of_point(b, a)
    if math.degrees(r) != 225:
        print('Failed: ')
        print(str(math.degrees(r)))
        assert False

    a = {'x': 0, 'y': 0}
    b = {'x': 1, 'y': -1}

    r = utils.find_angle_of_point(a, b)
    if math.degrees(r) != 135:
        print('Failed: ')
        print(str(math.degrees(r)))
        assert False

    r = utils.find_angle_of_point(b, a)
    if math.degrees(r) != 315:
        print('Failed: ')
        print(str(math.degrees(r)))
        assert False

    # Check we can do triangles with points in triangles
    tri = [{'x': 0, 'y': 1}, {'x': 1, 'y': -1}, {'x': -1, 'y': -1}]
    pt1 = {'x': 0, 'y': 0}
    pt2 = {'x': 1, 'y': 1}

    if not utils.is_point_inside_triangle(tri, pt1):
        print('Failed pt should be in triangle')
        assert False

    if utils.is_point_inside_triangle(tri, pt2):
        print('Failed pt should not be in triangle')
        assert False

    print('Tests Passed')