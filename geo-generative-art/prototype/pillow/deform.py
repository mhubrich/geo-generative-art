import copy, math, random


def float_gen(a, b):
    return random.uniform(a, b)


def octagon(x_orig, y_orig, side):
    x = x_orig
    y = y_orig
    d = side / math.sqrt(2)
    oct = []
    oct.append((x, y))
    x += side
    oct.append((x, y))
    x += d
    y += d
    oct.append((x, y))
    y += side
    oct.append((x, y))
    x -= d
    y += d
    oct.append((x, y))
    x -= side
    oct.append((x, y))
    x -= d
    y -= d
    oct.append((x, y))
    y -= side
    oct.append((x, y))
    x += d
    y -= d
    oct.append((x, y))
    return oct


def deform(shape, iterations, variance):
    for i in range(iterations):
        for j in range(len(shape)-1, 0, -1):
            midpoint = ((shape[j-1][0] + shape[j][0])/2 + float_gen(-variance, variance), (shape[j-1][1] + shape[j][1])/2 + float_gen(-variance, variance))
            shape.insert(j, midpoint)
    return shape


def draw_deform(draw, x_orig, y_orig, side, color, basedeforms, finaldeforms, base_var, final_var, num_layers):
    shape = octagon(x_orig, y_orig, side)
    baseshape = deform(shape, basedeforms, base_var)
    for j in range(num_layers):
        tempshape = copy.deepcopy(baseshape)
        layer = deform(tempshape, finaldeforms, final_var)
        draw.polygon(layer, fill=color)
