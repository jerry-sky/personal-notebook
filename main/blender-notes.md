# Blender Notes

## Addons

- [Time Tracker](https://github.com/uhlik/bpy#time-tracker-for-blender-280)

## Geometry node

Can be used to colorize an object according to its position, rotation and such.

## Objects reusing mesh data

Every time you copy an object consider making it a linked copy - meaning to create a new object that uses the mesh from the original object.

## Adaptive subdivision

Use adaptive subdivision to avoid generating too many polygons. Thanks to this method you can save processing power and memory on mesh data by decreasing its detail accordingly to the distance from the camera.

## !Alpha transparency

Do not use alpha transparency. Instead make a blocky thingy that more or less outlines the alpha texture. The reason this method is better is performance - when using alpha transparency you can double your render time.

## HDR world backgrounds
<!-- spellchecker: disable-next-line -->
When using HDRs as the world background enable option *"Multiple importance sampling"* in the *World settings panel*

## Select sharp edges

SHIFT + G $\equiv$ select sharp edges like these that are selected

## 45° edges //TODO elaborate

- `CTRL + F`
- Poke faces
- Tris to quads

## Spherize tool

`ALT + SHIFT + S`

## Pie Menus

Pie Menus can increase productivity significantly, because of the speed at which you can select different options from a given menu. This can be especially seen when you develop a muscle memory over time and remember the direction of mouse movement to perform desired action from the pie menu.

## Masking data

To clear sculpt masking data use
```blender
Mesh: Clear Sculpt-Mask Data
```
