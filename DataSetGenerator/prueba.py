def yolo2points(values,size):

    values = values[:-1]
    values = values.split(" ")
    values[0] = float(values[0])
    values[1] = float(values[1])
    values[2] = float(values[2])
    values[3] = float(values[3])
    values[4] = float(values[4])

    width = size[0]
    height = size[1]

    propX = values[1]
    propY = values[2]
    propAncho = values[3]
    propAlto = values[4]

    puntoX = width * propX
    puntoY = height * propY
    ancho = width * propAncho
    alto = height * propAlto

    puntos = [(puntoX-ancho/2,puntoY-alto/2),(puntoX+ancho/2,puntoY-alto/2),(puntoX+ancho/2,puntoY+alto/2),(puntoX-ancho/2,puntoY+alto/2)]
    return(puntos)

print(yolo2points("0 0.450000 0.217333 0.132000 0.242667\n",(500,375)))

import math
def rotatebox(rect, center, degrees):
    rads = math.radians(degrees)

    newpts = []

    for pts in rect:
        diag_x = center[0] - pts[0]
        diag_y = center[1] - pts[1]

        newdx = diag_x * math.cos(rads) - diag_y * math.sin(rads)
        newdy = diag_x * math.sin(rads) + diag_y * math.cos(rads)
        newpts.append( (center[0] + newdx, center[1] + newdy) )

    return newpts

print(rotatebox([(2,2),(4,2),(4,4),(2,4)],(1,1),90))