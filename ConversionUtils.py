import open3d as o3d
import numpy as np
from pathlib import Path
import os
from pyntcloud import PyntCloud
import pandas as pd

class ConversionUtils:
    def list_files_in_directory(directory_path):
        file_list = []
        for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                file_list.append(filename)
        return file_list
    
    def stl_to_ply(path, x):
        imported_file_name = Path(path).stem
        mesh = o3d.io.read_triangle_mesh(path)
        pcd = mesh.sample_points_uniformly(number_of_points=x)
        exported_file_name = "abc-dataset-ply/" + imported_file_name + ".ply"
        o3d.io.write_point_cloud(exported_file_name, pcd, write_ascii=True, compressed=False, print_progress=False)
    
    def convert_to_binvox(path):
        point_cloud = np.loadtxt(path, skiprows=12)[:, 0:3]
        df = pd.DataFrame(data=point_cloud, columns=['x','y','z'])
        cloud = PyntCloud(df)
        voxelgrid_id = cloud.add_structure("voxelgrid", n_x=64, n_y=64, n_z=64)
        voxelgrid = cloud.structures[voxelgrid_id]
        Binary_voxel_array = voxelgrid.get_feature_vector(mode="binary")
        return Binary_voxel_array