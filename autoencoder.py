import numpy as np
import pandas as pd
from pyntcloud import PyntCloud
import os
import tensorflow as tf
from keras.layers import Input, Conv3D, MaxPooling3D, UpSampling3D
from keras.models import Model
import numpy as np
import matplotlib.pyplot as plt

def list_files_in_directory(directory_path):
    file_list = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_list.append(filename)
    return file_list

directory = "abc-dataset-ply/"
files = sorted(list_files_in_directory("abc-dataset-ply/"))
dataset = []
def convert_to_binvox(path):
    point_cloud = np.loadtxt(path, skiprows=12)[:, 0:3]
    df = pd.DataFrame(data=point_cloud, columns=['x','y','z'])
    cloud = PyntCloud(df)
    voxelgrid_id = cloud.add_structure("voxelgrid", n_x=128, n_y=128, n_z=128)
    voxelgrid = cloud.structures[voxelgrid_id]
    Binary_voxel_array = voxelgrid.get_feature_vector(mode="binary")
    dataset.append(Binary_voxel_array)

for i in files:
    path = "abc-dataset-ply/" + i
    convert_to_binvox(path)

print(len(dataset))


train_data = dataset[:20]
test_data = dataset[20:]

original_dim = (128, 128, 128)
X_train = np.array(test_data, dtype=np.float32)
encoding_dim = 64

input_layer = Input(shape=original_dim + (1,))  # Add 1 channel dimension
x = Conv3D(32, (3, 3, 3), activation='relu', padding='same')(input_layer)
x = MaxPooling3D((2, 2, 2), padding='same')(x)
x = Conv3D(64, (3, 3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling3D((2, 2, 2), padding='same')(x)

x = Conv3D(64, (3, 3, 3), activation='relu', padding='same')(encoded)
x = UpSampling3D((2, 2, 2))(x)
x = Conv3D(32, (3, 3, 3), activation='relu', padding='same')(x)
x = UpSampling3D((2, 2, 2))(x)
decoded = Conv3D(1, (3, 3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(X_train, X_train, epochs=5, batch_size=2)