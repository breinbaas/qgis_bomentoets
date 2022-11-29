def lines_intersect(p1, p2, p3, p4):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return False
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return False
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return False
    return True

def line_in_or_intersects(rect, line):
    xmax = max([line[0][0], line[1][0]])
    xmin = min([line[0][0], line[1][0]])
    ymax = max([line[0][1], line[1][1]])
    ymin = min([line[0][1], line[1][1]])

    line_in_rect = xmax <= rect['right'] and rect['left'] <= xmin and ymax <= rect['top'] and rect['bottom'] <= ymin

    if line_in_rect:
        return True

    topleft = rect['left'], rect['top'] 
    topright = rect['right'], rect['top'] 
    bottomleft = rect['left'], rect['bottom']
    bottomright = rect['right'], rect['bottom']

    if lines_intersect(topleft, topright, line[0], line[1]):
        return True
    if lines_intersect(topright, bottomright, line[0], line[1]):
        return True
    if lines_intersect(bottomright, bottomleft, line[0], line[1]):
        return True
    if lines_intersect(bottomleft, topleft, line[0], line[1]):
        return True

    return False


if __name__=="__main__":
    print("testing testing...")
    p1 = (0,0)
    p2 = (5,5)
    p3 = (0,2)
    p4 = (5,2)
    p5 = (-1, 0)
    p6 = (-1, 5)
    
    # should intersect
    assert lines_intersect(p1, p2, p3, p4) == True
    # should not intersect
    assert lines_intersect(p1, p2, p5, p6) == False

    rect = {'left':0, 'right':10, 'top':10, 'bottom':0}

    line1 = ((1,1),(9,9)) # in rect
    assert line_in_or_intersects(rect, line1) == True
    line2 = ((-5,5),(15,5))
    assert line_in_or_intersects(rect, line2) == True
    line3 = ((-5,0), (-5,10))
    assert line_in_or_intersects(rect, line3) == False





    

    

        



