# Blender Notes

- [Links](#links)
  - [Useful](#useful)
  - [Cool](#cool)
  - [TODO](#todo)
- [Addons](#addons)
- [Geometry node](#geometry-node)
- [Objects reusing mesh data](#objects-reusing-mesh-data)
- [Adaptive subdivision](#adaptive-subdivision)
- [!Alpha transparency](#alpha-transparency)
- [HDR world backgrounds](#hdr-world-backgrounds)
- [Select sharp edges](#select-sharp-edges)
- [45° edges //TODO elaborate](#45-edges-todo-elaborate)
- [Spherize tool](#spherize-tool)
- [Pie Menus](#pie-menus)
- [Masking data](#masking-data)
- [Applying a property change to multiple objects](#applying-a-property-change-to-multiple-objects)

## Links

### Useful
  - [Creating Realistic Wetmaps](https://youtu.be/f3yzwql_2nw)
  - [NormalMap-Online](http://cpetry.github.io/NormalMap-Online/)
  - [Avoiding pinching when subsurface modeling](https://youtu.be/3rlMzsBWtPY)
  - [How to Work with Blender Lighting](http://www.blenderguru.com/tutorials/make-atmospheric-lighting-blender/#.VIN68vl5N8F)
  - [18 Ways to Speed Up Cycles Rendering](https://youtu.be/8gSyEpt4-60)
  - [The Secret Ingredient to Photorealism](https://youtu.be/m9AT7H4GGrA)
  - [Pro-lighting Studio](https://youtu.be/QVb3261tywQ)
  - [Baking introduction](https://youtu.be/sB09T--_ZvU)

### Cool

  - [Blender 2.8 EEVEE Volumetric Disco Disco](https://youtu.be/mRKUou0zLoA)
  - [Disintegration effect](https://youtu.be/YzKR8QtcozM)
  - [How to Create Toon Style Animation](https://youtu.be/ZiqrCRqyLzE)
  - [How to Create a Paint Splash](https://youtu.be/I0Tz1U6A5vI)
  - [Colorful particles](http://3.bp.blogspot.com/-Gy_rDI34zBw/UN_1NZmoQfI/AAAAAAAAiEI/cYEmEreB-W0/s1600/particleInfo_010.png)
  - [10 Tips for Filming Visual Effects](https://youtu.be/xF0SypG7q8c)
  - [Create a Subway in 20 minutes](https://youtu.be/nb6rSMAooDs)

### TODO

  - [**UV mapping tutorial //TODO-note**](https://youtu.be/L3654VGZObg)
  - [**Primary, secondary and tertiary shapes //TODO-note**](http://www.neilblevins.com/cg_education/primary_secondary_and_tertiary_shapes/primary_secondary_and_tertiary_shapes.htm)
  - [**Easy cushion model //TODO-note**](https://twitter.com/andrewpprice/status/1224544692143964161)


## Addons

- [Time Tracker](https://github.com/uhlik/bpy#time-tracker-for-blender-280)
- [Physical Starlight and Atmosphere](https://youtu.be/Rbx9DlyddF8) *$38*

---

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

## Applying a property change to multiple objects

To change a numeric value on a set of objects, first change the value for one *active* object and then press the `RMB` on the value field and choose `Copy To Selected`. This will apply this change to all the other selected objects that have this property.\
[Source](https://blender.stackexchange.com/questions/6015/applying-numeric-input-attribute-changes-on-multiple-objects-at-the-same-time)

