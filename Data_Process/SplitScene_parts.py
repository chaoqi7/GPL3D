import argparse
import os
from plyfile import PlyData, PlyElement
import numpy as np
from sklearn.decomposition import PCA

parser = argparse.ArgumentParser()
parser.add_argument("--rootdir", default='', type=str)
parser.add_argument("--destdir",default='', type=str)
parser.add_argument("--oper", type=str, default='test',help='train/vali/test')
args = parser.parse_args()

# create the directory
train_filenames = ["Lille1.ply", "Lille2.ply"]
test_filenames = ["Paris.ply"]

if args.oper=='test':
    filenames = test_filenames
    save_dir = os.path.join(args.destdir, "test_50_pointclouds")
elif args.oper=='train':
    filenames = train_filenames
    save_dir = os.path.join(args.destdir, "train_50_pointclouds")
os.makedirs(save_dir, exist_ok=True)

for filename in filenames:
    if args.oper=='test':
        fname = os.path.join(args.rootdir, "training_50_classes", filename)
    elif args.oper == 'train':
        fname = os.path.join(args.rootdir, "training_50_classes", filename)
    print(fname)
    plydata = PlyData.read(fname)
    print(plydata)
    x = plydata["vertex"].data["x"].astype(np.float32)
    y = plydata["vertex"].data["y"].astype(np.float32)
    z = plydata["vertex"].data["z"].astype(np.float32)
    reflectance = plydata["vertex"].data["reflectance"].astype(np.float32)
    object_label = plydata["vertex"].data["label"].astype(np.float32)
    class_label = plydata["vertex"].data["class"].astype(np.float32)

    pts = np.concatenate([
        np.expand_dims(x, 1),
        np.expand_dims(y, 1),
        np.expand_dims(z, 1),
        np.expand_dims(reflectance, 1),
        np.expand_dims(object_label, 1),
        np.expand_dims(class_label, 1)
    ], axis=1).astype(np.float32)

    pca = PCA(n_components=1)
    pca.fit(pts[::10, :2])
    pts_new = pca.transform(pts[:, :2])
    hist, edges = np.histogram(pts_new, pts_new.shape[0] // 1700000)

    count = 0

    for i in range(1, edges.shape[0]):
        mask = np.logical_and(pts_new <= edges[i], pts_new > edges[i - 1])[:, 0]
        np.save(os.path.join(save_dir, os.path.splitext(filename)[0] + f"_{count}"), pts[mask])
        count += 1

    hist, edges = np.histogram(pts_new, pts_new.shape[0] // 1700000 - 2,
                               range=[(edges[1] + edges[0]) // 2, (edges[-1] + edges[-2]) // 2])

    for i in range(1, edges.shape[0]):
        mask = np.logical_and(pts_new <= edges[i], pts_new > edges[i - 1])[:, 0]
        np.save(os.path.join(save_dir, os.path.splitext(filename)[0] + f"_{count}"), pts[mask])
        count += 1