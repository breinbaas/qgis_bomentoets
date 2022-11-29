from typing import List, Tuple
from math import hypot

class ReferenceLinePoint:
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l

class ReferenceLine:
    def __init__(self):
        self.points = []
        self.epoints = []

    def bounding_box(self, offset: int=0):
        """Get a bounding box around the referenceline (with or without some offset)
        
        Returns dict with left, top, right, bottom
        """
        xs = [p.x for p in self.points]
        ys = [p.y for p in self.points]

        left = round(min(xs)) - offset
        right = round(max(xs)) + offset
        top = round(max(ys)) + offset
        bottom = round(min(ys)) - offset

        return {'left':left, 'top':top, 'right':right, 'bottom': bottom}

    @classmethod
    def from_points(self, points: List[Tuple[float, float]]):
        result = ReferenceLine()
        l = 0
        for point in points:
            x = float(point[0])
            y = float(point[1])            
            if len(result.points) != 0:
                l += hypot(x-result.points[-1].x, y-result.points[-1].y)            
            result.points.append(ReferenceLinePoint(x=x, y=y, l=l))
            

        result.calculate_equidistance_points()
        return result

    def calculate_equidistance_points(self, distance: int=1):
        """Create a line with points with a regular spacing"""
        
        if len(self.points) < 2:
            return
        
        lmin = round(self.points[0].l)
        lmax = round(self.points[-1].l)

        # chainages, lats, lons
        self.epoints = []
        for l in range(int(lmin), int(lmax), distance):
            for i in range(1, len(self.points)):
                l1, x1, y1 = (
                    self.points[i - 1].l,
                    self.points[i - 1].x,
                    self.points[i - 1].y,
                )
                l2, x2, y2 = (
                    self.points[i].l,
                    self.points[i].x,
                    self.points[i].y,
                )
                if l1 <= l < l2:
                    x = x1 + (l - l1) / (l2 - l1) * (x2 - x1)
                    y = y1 + (l - l1) / (l2 - l1) * (y2 - y1)

                    self.epoints.append(
                        ReferenceLinePoint(
                            l=round(l, 2),
                            x=round(x, 2),
                            y=round(y, 2),
                        )
                    )

    def closest_point_to_xy(self, x: float, y: float) -> Tuple[float, float]:
        """Return the closest point on the reference line to the given point

        Args:
            lat (float): Latitude of the point
            lon (float): Longitude of the point

        Returns:
            x, y 
        """
        result = None
        dlmin = 1e9
        for p in self.epoints:
            dl = hypot((p.x - x), (p.y-y))
            if dl < dlmin:
                dlmin = dl
                result = p.x, p.y
        return result