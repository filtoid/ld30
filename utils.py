__author__ = 'fil'

import math

def find_angle_of_point(e, s):
    '''

    :param s: start point (dict ['x'], ['y'])
    :param e: end point (dict ['x'], ['y'])
    :return: return angle
    '''
    diffx = s['x'] - e['x']
    diffy = s['y'] - e['y']

    if diffx == 0:
        if diffy > 0:
            return 0
        if diffy < 0:
            return math.pi

    if diffy == 0:
        if diffx > 0:
            return math.pi/2
        if diffx < 0:
            return 3 * math.pi / 2

    if diffx > 0:
        #print(math.degrees(math.atan(diffy/diffx)))
        return (math.pi/2) - math.atan(diffy/diffx)
    elif diffx < 0:
        return (3 * math.pi/2) - math.atan(diffy/diffx)

    return -1

def is_point_inside_triangle(tri, pt):
    tp1 = tri[0]
    tp2 = tri[1]
    tp3 = tri[2]

    thtri1 = [min(find_angle_of_point(tp1, tp2), find_angle_of_point(tp1, tp3)),
             max(find_angle_of_point(tp1, tp2), find_angle_of_point(tp1, tp3))]
    thtri2 = [min(find_angle_of_point(tp2, tp1), find_angle_of_point(tp2, tp3)),
             max(find_angle_of_point(tp2, tp1), find_angle_of_point(tp2, tp3))]
    thtri3 = [min(find_angle_of_point(tp3, tp1), find_angle_of_point(tp3, tp2)),
             max(find_angle_of_point(tp3, tp1), find_angle_of_point(tp3, tp2))]

    thpt1 = find_angle_of_point(tp1, pt)
    thpt2 = find_angle_of_point(tp2, pt)
    thpt3 = find_angle_of_point(tp3, pt)

    if thpt1 < thtri1[0] or thpt1 > thtri1[1]:
        return False

    if thpt2 < thtri2[0] or thpt2 > thtri2[1]:
        return False

    if thpt3 < thtri3[0] or thpt3 > thtri3[1]:
        return False

    return True


def test_is_point_inside_triangle():
    tri = [{'x': 0, 'y': 1}, {'x': 1, 'y': -1}, {'x': -1, 'y': -1}]
    pt1 = {'x': 0, 'y': 0}
    pt2 = {'x': 1, 'y': 1}

    if not is_point_inside_triangle(tri, pt1):
        print('Failed pt should be in triangle')

    if is_point_inside_triangle(tri, pt2):
        print('Failed pt should not be in triangle')

def test_point_calc_code():
    pt1 = {'x': 1, 'y': 1}
    pt2 = {'x': 2, 'y': 2}

    th1 = find_angle_of_point(pt1, pt2)

    print('pt1 to pt 2 - ' + str(math.degrees(th1)))

    pt1 = {'x': 1, 'y': 1}
    pt2 = {'x': 0, 'y': 0}

    th1 = find_angle_of_point(pt1, pt2)
    print('pt1 to pt 2 - ' + str(math.degrees(th1)))

    pt1 = {'x': 1, 'y': 1}
    pt2 = {'x': 2, 'y': 0}

    th1 = find_angle_of_point(pt1, pt2)
    print('pt1 to pt 2 - ' + str(math.degrees(th1)))

    pt1 = {'x': 2, 'y': 0}
    pt2 = {'x': 1, 'y': 1}

    th1 = find_angle_of_point(pt1, pt2)
    print('pt1 to pt 2 - ' + str(math.degrees(th1)))