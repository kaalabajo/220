from graphics import Circle, Line, Polygon, Point


class Face:
    """creates a class Face and init. it"""
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        """draws a mouth"""
        self.mouth.undraw()
        """undraws the default mouth"""
        point_1 = self.mouth.getP1()
        point_2 = self.mouth.getP2()
        """gets the 2 points used to draw default mouth"""
        center = self.head.getCenter()
        """gets center of head"""
        face_rad = self.head.getRadius()
        """gets radius of head"""
        point_3x = (point_1.getX() + point_2.getX()) / 2
        point_3y = center.getY() + face_rad * .8
        """these two points will be used to make the final point in the polygon
        centered and slightly below the original mouth height"""
        Polygon(point_1,point_2,Point(point_3x,point_3y)).draw(self.window)
        """draw the new mouth"""

    def shock(self):
        """draws a shock face"""
        self.mouth.undraw()
        """undraw the mouth from default"""
        point_1 = self.mouth.getP1()
        """the first point used to make default mouth"""
        center = self.head.getCenter()
        """gets center of head"""
        eye_rad = self.left_eye.getRadius()
        """radius of the left eye"""
        o_mouth = Circle(Point(center.getX(),point_1.getY()),eye_rad)
        """new open mouth will be a circle centered"""
        o_mouth.draw(self.window)

    def wink(self):
        left_center = self.left_eye.getCenter()
        """gets the left eye center point"""
        left_rad = self.left_eye.getRadius()
        """gets the radius of the eyes"""
        eye_p1_x = left_center.getX() - left_rad
        eye_p2_x = left_center.getX() + left_rad
        """those get the x values for point 1 and 2 of the new line we'll make"""
        eye_p_y = left_center.getY()
        """use this for the eye line y value"""
        closed_eye = Line(Point(eye_p1_x,eye_p_y),Point(eye_p2_x,eye_p_y))
        """new eye at original y value and length equal to the original circle diameter"""
        self.left_eye.undraw()
        """undraw original eye"""
        self.smile()
        """to get the face with the mouth we want"""
        closed_eye.draw(self.window)
        "draw the closed eye"

