# CAD-DR: CAD Dimensionality Reduction

## Introduction
A 3D convolutional autoencoder for the purpose of dimensionality reduction of CAD models. The autoencoder is based on the EfficientNet architecture. The development took place on a system having the following specifications:

- CPU: Ryzen 7 4800H
- GPU: Nvidia GTX 1660 Ti
- Ubuntu 22.04

## Details
- The models was trained on 800 models from the ABC dataset
- The train dataset comprises of 200 models from the same
- Input format: STL
- The STL files are first converted to point cloud (.ply), and then to 3D binary voxel arrays

## Requirements
The model was created using TensorFlow 2.14. Usage of GPU is suggested, and the TensorFlow installation for the same can be done using pip: 
**pip install tensorflow\[and-cuda\]**

### Other required libraries too can be installed via pip:
| Library | Version |
|---------|---------|
| numpy | 1.26.1 |
| pandas | 2.1.1 |
| pyntcloud | 0.3.1 |
| matplotlib | 3.8.0 |
| open3d | 0.17.0 |

The autoencoder.ipynb file contains code for visualizing in open3d as well as matplotlib.  
The matplotlib visualization will work on all systems while the open3d visualization is geared towards a higher quality, interactive visualization.  

## Instructions

### Training
1. Once you clone the repository, create folders in the main directory called "abc-dataset-stl" and "abc-dataset-ply"
2. Download a chunk ABC dataset in STL format.
3. Move 1000 STL files to the abc-dataset-stl directory
4. The autoencoder notebooks can then be run. Additional informations can be found in the notebooks.
5. In case you wish to train the model on a larger dataset, the code can be modified accordingly.
