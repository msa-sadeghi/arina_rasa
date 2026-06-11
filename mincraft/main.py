from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

application.asset_folder = application.package_folder / "assets"
application.development_mode = False
app = Ursina()


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model="cube",
            texture="white_cube",
            color=color.azure,
            position=position,
            origin_y=0.5,
            scale=(1, 2, 1),
            collider="box",
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            if key == "right mouse down":
                Voxel(position=self.position + mouse.normal)


for z in range(20):
    for x in range(20):
        Voxel(position=(x, 0, z))
player = FirstPersonController()
player_body = Entity(
    parent=player, model="cube", color=color.azure, scale=(1, 2, 1), y=-1
)


def input(key):
    if key == "escape":
        application.quit()


app.run()
