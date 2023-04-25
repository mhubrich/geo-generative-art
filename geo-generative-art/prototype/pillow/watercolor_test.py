import random
import numpy as np
import geopandas as gpd
from datetime import datetime
from PIL import Image, ImageDraw

from deform import draw_deform


def transform(p, bbox, grid_x, grid_y):
    x, y = np.clip(p.x, bbox[0], bbox[2]), np.clip(p.y, bbox[1], bbox[3])
    x_trans = int(grid_x * ((x - bbox[0]) / (bbox[2] - bbox[0])))
    y_trans = int(grid_y * ((y - bbox[1]) / (bbox[3] - bbox[1])))
    return x_trans, grid_y - y_trans


def main():
    random.seed(0)
    bbox = (-123.14789772033691, 49.27150084847537, -123.1058406829834, 49.29524015790929)
    width, height = 1500, 1000
    shapealpha = 0.02
    side_min = 15
    side_max = 30
    layers_min = 20
    layers_max = 25
    base_deforms = 1
    final_deforms = 3
    base_variance = 50
    final_variance = 20
    colors = [(155, 93, 229), (241, 91, 181), (254, 228, 64), (0, 187, 249), (0, 245, 212), (155, 93, 229)]
    random.shuffle(colors)

    im = Image.new('RGB', (width, height), (216, 240, 239))
    draw = ImageDraw.Draw(im, 'RGBA')

    paths = ['data/cafe.geojson', 'data/starbucks.geojson', 'data/timhortons.geojson', 'data/mcdonalds.geojson', 'data/subway.geojson', 'data/burgerking.geojson']
    for i, path in enumerate(paths):
        color = colors[i] + (int(shapealpha*255), )
        df = gpd.read_file(path)
        for p in df.geometry:
            x_orig, y_orig = transform(p, bbox, width, height)
            side = random.randint(side_min, side_max)
            num_layers = random.randint(layers_min, layers_max)
            draw_deform(draw, x_orig, y_orig, side, color, base_deforms, final_deforms, base_variance, final_variance, num_layers)
        shapealpha += 0.005
    im.save('img_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png', 'PNG')


if __name__ == "__main__":
    main()
