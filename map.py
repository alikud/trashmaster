import pygame as pg
import pytmx

# config
# TILE_SIZE = 16

# def preparedMap(screenSize):
#     tileImage = pg.image.load('tile1.png')
#     surface = pg.Surface(screenSize)

#     for x in range(0, screenSize[0], TILE_SIZE):
#         for y in range(0, screenSize[1], TILE_SIZE):
#             surface.blit(tileImage, (x, y))
#     return surface
def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)
class TiledMap:
    #loading file
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
    
    #rendering map
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tilewidth))
    
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    def __init__(self,width,height):
        self.camera = pg.Rect(0,0, width, height)
        self.width = width
        self.height = height

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)

    # def apply_rect(self, rect):
    #     return rect.move(self.camera.topleft)
    
    def update(self,target):
        x = -target.rect.x + int(1024/2)
        y = -target.rect.y + int(768 / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 1024), x)  # right
        y = max(-(self.height - 768), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)




