"""
DIGM 131 - Assignment 3: Function Library (scene_functions.py)
===============================================================

OBJECTIVE:
    Create a library of reusable functions that each generate a specific
    type of scene element. This module will be imported by main_scene.py.

REQUIREMENTS:
    1. Implement at least 5 reusable functions.
    2. Every function must have a complete docstring with Args and Returns.
    3. Every function must accept parameters for position and/or size so
       they can be reused at different locations and scales.
    4. Every function must return the name(s) of the Maya object(s) it creates.
    5. Follow PEP 8 naming conventions (snake_case for functions/variables).

GRADING CRITERIA:
    - [30%] At least 5 functions, each creating a distinct scene element.
    - [25%] Functions accept parameters and use them (not hard-coded values).
    - [20%] Every function has a complete docstring (summary, Args, Returns).
    - [15%] Functions return the created object name(s).
    - [10%] Clean, readable code following PEP 8.
"""

import maya.cmds as cmds
import math

def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):

    """Create a simple building from a cube, placed on the ground plane.

    The building is a single scaled cube whose base sits at ground level
    (y = 0) at the given position.

    Args:
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.

    Returns:
        str: The name of the created building transform node.
    """
    building = cmds.polyCube(width = width, height = height, depth = depth)[0]
    #create building from cube.

    cmds.move(position[0], position[1] + height / 2.0, position[2], building)
    #move building to the ground plane.

    return building

    # TODO: Implement this function.
    #   1. Create a polyCube with the given width, height, and depth.
    #   2. Move it so its base sits on the ground at 'position'.
    #      Hint: offset Y by height / 2.0.
    #   3. Return the object name.


def create_tree(trunk_radius=0.5, trunk_height=4, canopy_radius=2,
                position=(0, 0, 0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy.

    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
    trunk = cmds.polyCylinder(r=trunk_radius, h=trunk_height)[0]
    cmds.move(0, trunk_height / 2.0, 0, trunk)
    #create tree trunk with poly cylinder + move tree trunk to ground level

    canopy = cmds.polySphere(r=canopy_radius)[0]
    cmds.move(0, truck_height + canopy_radius, 0, canopy)
    #create tree canopy with poly sphere + move to the height of the trunk

    tree_group = cmds.group(trunk, canopy)
    cmds.move(position[0], position[1], position[2], tree_group)
    #create group for trunk and canopy + move to position

    return tree_group
                    
    # TODO: Implement this function.
    #   1. Create a polyCylinder for the trunk and position it.
    #   2. Create a polySphere for the canopy, positioned on top of the trunk.
    #   3. Group trunk and canopy together using cmds.group().
    #   4. Move the group to 'position'.
    #   5. Return the group name.


def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a simple fence made of posts and rails.

    The fence runs along the X axis starting at the given position.

    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
    """
    parts = []
    spacing = length / (post_count -1)
    # collect objects + determine spacing parameters.

    for i in range(post_count):
        post = cmds.polyCube(w=0.2, h=height, d=0.2)[0]
        cmds.move(i * spacing, height / 2.0, 0, post)
        parts.append(post)
    # loop for the creation of the posts + defining location.

    rail = cmds.polyCube(w=length, h=0.2, d=0.2)[0]
    cmds.move(length / 2.0, height = 0.75, 0, rail)
    parts.append(rail)
    # create the railing + defining location.

    fence_group = cmds.group(parts)
    cmds.move(position[0], position[1], position[2], fence_group)
    #create group for the posts and railing + define the position.

    return fence_group
    
    # TODO: Implement this function.
    #   1. Calculate spacing between posts: length / (post_count - 1).
    #   2. Loop to create 'post_count' thin, tall cubes as posts.
    #   3. Create a long, thin cube as a horizontal rail connecting them.
    #   4. Group everything and move to 'position'.
    #   5. Return the group name.


def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a street lamp using a cylinder pole and a sphere light.

    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """
    pole = cmds.polyCylinder(r=0.1, h=pole_height)[0]
    cmds.move(0, pole_height/ 2.0, 0, pole)
    #create pole with polycylinder + move to ground level.

    light = cmds.polySphere(r=light_radius)[0]
    cmds.move(0, pole_height + light_radius, 0, light)
    #create light with polysphere + move on top of the pole.

    lamp_group = cmds.group(pole, light)
    cmds.move(position[0], position[1], position[2], lamp_group)
    #create group for pole and light + move group to position.

    return lamp_group
    
    # TODO: Implement this function.
    #   1. Create a thin polyCylinder for the pole.
    #   2. Create a polySphere for the light, placed at the top of the pole.
    #   3. Group them, move to 'position', and return the group name.


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    """Place objects created by 'create_func' in a circular arrangement.

    This is a higher-order function: it takes another function as an
    argument and calls it repeatedly to place objects around a circle.

    Args:
        create_func (callable): A function from this module (e.g.,
            create_tree) that accepts a 'position' keyword argument
            and returns an object name.
        count (int): Number of objects to place around the circle.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Additional keyword arguments passed to create_func
            (e.g., trunk_height=4).

    Returns:
        list: A list of object/group names created by create_func.
    """
    results = []

    for i in range(count):
        angle = 2 * math.pi * i / count

        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)

        obj = create_func(position=(z, center[1], z), **kwargs)
        cmds.parent(obj, group)
        results.append(obj)
    # create loop for even distribution + calculate position using math

    group = cmds.group(empty=true, name="circle_group")
    # create group for objects in the circle

    return results
    # TODO: Implement this function.
    #   1. Import the math module (at the top of the file or here).
    #   2. Loop 'count' times. For each iteration:
    #       a. Calculate the angle: angle = 2 * math.pi * i / count
    #       b. Calculate x = center[0] + radius * math.cos(angle)
    #       c. Calculate z = center[2] + radius * math.sin(angle)
    #       d. Call create_func(position=(x, center[1], z), **kwargs)
    #       e. Append the returned name to a results list.
    #   3. Return the results list.
