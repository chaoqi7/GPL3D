# GPL3D DataSet from Instance-incremental Scene Graph Generation from Real-world Point Clouds via Normalizing Flows

## Data process of GPL3D
Step 1. Download the [Paris-Lille-3D](https://npm3d.fr/paris-lille-3d)

Step 2. [Split each scene into different parts](Data_Process/SplitScene_parts.py)

Step 3. [Split each part into different objects](Data_Process/SplitPart_objects.py).

## Class Labels

[Object Class Labels:](GPL3D/meta/class_names.py)

 road <br>
sidewalk <br>
island <br>
Vegetal_ground <br>
building <br>
other_natural <br>
tree <br>
potted_plant <br>
signage <br>
bollard <br>
trash_can <br>
barrier <br>
pedestrian <br>
car <br>
unclassified

[Relationship Class Labels:](GPL3D/meta/rel_names.py)

adjacent to <br>
on <br>
close to <br>
supported by <br>
leaning against <br>
spatial proximity <br>
behind <br>
in front of <br>
part of

## DataSet

[Lille with unclassified objects](DataSet/Lille_50_SceneGraphAnnotation_withunclass.json) <br>
[Paris with unclassified objects](DataSet/Paris_50_SceneGraphAnnotation_withunclass.json) <br>
[Lille without unclassified objects](DataSet/Lille_50_SceneGraphAnnotation.json) <br>
[Paris without unclassified objects](DataSet/Paris_50_SceneGraphAnnotation.json)

## Environments
Ubuntu 16.04 <br>
Python 3.7 <br>
sklearn 1.0 <br>
plyfile 0.7.4
