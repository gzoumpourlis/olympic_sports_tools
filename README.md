# olympic_sports_tools

Publication link : http://cvgl.stanford.edu/papers/cvpr11_liu_a.pdf

Technical report : http://www.cs.ucf.edu/%7Eliujg/papers/cvpr11_liu_a_tech_report.pdf

The unprocessed attributes are copied from Table 3 in the paper's technical report, and pasted in this file : 'Olympic_Attributes.txt'

We have 16 classes of Olympic Sports, and 40 attributes.

Then, we execute parse_attributes.py, and save the following 3 variables in the 'attributes.npz' file:

*attributes*
The attributes are stored in a numpy array of size 16x40, containing ones and zeros.

Values of 1 (integer) in the cell (i,j), mean that the i-th class has the j-th attribute.

Values of 0 (integer) mean that the i-th class does not have the j-th attribute.

*attribute_names*
List of the attribute names

*class_names*
List of the class names
