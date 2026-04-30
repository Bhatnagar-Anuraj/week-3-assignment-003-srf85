"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]
# Create a ground plane.

sf.create_building(width=5, height=10, depth=5, position=(-10, 0, -12))
sf.create_building(width=7, height=5, depth=7, position=(-15, 0, -10))
sf.create_building(width=5, height=3, depth=5, position=(-18, 0, -6))
sf.create_building(width=3, height=15, depth=3, position=(-9, 0, -5))
sf.create_building(width=5, height=9, depth=5, position=(-3, 0, -1))
sf.create_building(width=5, height=11, depth=5, position=(-13, 0, -5))
sf.create_building(width=6, height=6, depth=6, position=(-10, 0, -12))
#create seven buildings in the distance/ varying sizes.

sf.create_tree(position=(-13, 0, -9))
sf.create_tree(position=(-10, 0, -5))
sf.create_tree(position=(-8, 0, -12))
sf.create_tree(position=(-13, 0, -8))
sf.create_tree(position=(-11, 0, -10))
#create five trees in between building in the distance.

sf.place_in_circle(sf.create_lamp_post, count=10, radius=20)
#Place 10 lamp posts in a circle of radius 20.

sf.place_in_circle(sf.create_tree, count=8, radius=25)
#Place 8 trees in a circle of radius 25.

sf.create_lamp_post(position=(0, 0, 0))
#create lamp post in the center the circle.

sf.create_fence(length=10, post_count=5, position=(-6, 0, -2
#create fence in between building and lamp posts.

# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
