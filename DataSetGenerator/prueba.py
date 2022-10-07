
import math
import matplotlib.pyplot as plt

def rotatebox( rect, center, degrees ):
    rads = math.radians(degrees)

    newpts = []

    for pts in rect:
        diag_x = center[0] - pts[0]
        diag_y = center[1] - pts[1]

        # Rotate the diagonal from center to top left

        newdx = diag_x * math.cos(rads) - diag_y * math.sin(rads)
        newdy = diag_x * math.sin(rads) + diag_y * math.cos(rads)
        newpts.append( (center[0] + newdx, center[1] + newdy) )

    return newpts

rect = [[50,50],[50,120],[150,120],[150,50]]

rect = rotatebox( rect, (100,100), 135 )
'''
width = 6
height = 6
xmin = 2
ymin = 2
xmax = 4
ymax = 4

puntoX = abs(xmin-xmax)/2 + xmin
puntoY = abs(ymin-ymax)/2 + ymin
ancho = abs(xmin-xmax)
alto = abs(ymin-ymax)

propX = puntoX/width
propY = puntoY/height
propAncho = ancho/width
propAlto = alto/height

#print("0 " + str(propX) + " " + str(propY) + " " + str(propAncho) + " " + str(propAlto))
print("0 {:.6f} {:.6f} {:.6f} {:.6f}\n".format(propX, propY, propAncho, propAlto))
'''