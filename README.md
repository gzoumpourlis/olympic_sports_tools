# olympic_sports_tools

This repo contains two scripts that help parsing the Olympic Sports dataset, from the following publication:

Juan Carlos Niebles, Chih-Wei Chen and Li Fei-Fei, "Modeling Temporal Structure of Decomposable Motion Segments for Activity Classification", ECCV 2010

Dataset's paper : http://vision.stanford.edu/documents/NieblesChenFei-Fei_ECCV2010.pdf

Dataset website : http://vision.stanford.edu/Datasets/OlympicSports/

The scripts are the following:

# 1. parse_attributes.py (used to save a numpy array with some class-related attributes)

# 2. convert_Olympic.py (used to convert the videos from .seq to .avi format)

----------------------------------

# Parsing class-related attributes

The class-related attributes are taken from the following publication:

J. Liu, B. Kuipers, S. Savarese, "Recognizing Human Actions by Attributes", CVPR 2011

Publication link : http://cvgl.stanford.edu/papers/cvpr11_liu_a.pdf

Technical report : http://www.cs.ucf.edu/%7Eliujg/papers/cvpr11_liu_a_tech_report.pdf

The unprocessed attributes are copied from Table 3 in the paper's technical report, and pasted in this file :
```
Olympic_Attributes.txt
```

We have 16 classes of the Olympic Sports dataset, and 40 attributes.

Then, we execute
```
python parse_attributes.py
```
and save the following 3 variables in the 'attributes.npz' file:

*attributes* :
The attributes are stored in a numpy array of size 16x40, containing ones and zeros.

Values of 1 (integer) in the cell (i,j), mean that the i-th class has the j-th attribute.

Values of 0 (integer) mean that the i-th class does not have the j-th attribute.

*attribute_names* :
List of the attribute names

*class_names* :
List of the class names

You can see the correspondences in the saved Attributes_Olympic.png image.

<p>
  <img src="https://github.com/gzoumpourlis/olympic_sports_tools/raw/master/Attributes_Olympic.png" width="640" title="Class names and class-related attributes">
</p>


----------------------------------

# Converting the videos from .seq to .avi format

To convert the videos of the dataset from .seq file format to .avi, we execute:
```
python convert_Olympic.py
```

This script will need a file named "video_Olympic.list", containing all the videos. This file already exists in this repo.
If you want to create this on your own for a modified version of the dataset, you can execute the following command:
```
ls /path/to/your/dataset/*/*.avi > video_Olympic.list
```
Then using a text editor you can simply find and replace the substring of the exported directories, so that you only keep the class names and the video names in your final file (as in the already saved file).
