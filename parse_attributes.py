import numpy as np
import matplotlib.pyplot as plt
import os

attr_file = 'Olympic_Attributes.txt'
attr_npz_file = 'attributes'
attr_npz_path = os.path.join(os.getcwd(), attr_npz_file)
N_classes = 16
N_attributes = 40

class_names = ['basketball_layup',
               'bowling',
               'clean_and_jerk',
               'discus_throw',
               'diving_platform_10m',
               'diving_springboard_3m',
               'hammer_throw',
               'high_jump',
               'javelin_throw',
               'long_jump',
               'pole_vault',
               'shot_put',
               'snatch',
               'tennis_serve',
               'triple_jump',
               'vault'
                ]
attribute_names = []
attributes = np.zeros((N_classes, N_attributes))

cnt_line = 0
cnt_classes = 0
cnt_attributes = 0

file = open(attr_file, 'r')
for line in file:
    line = line.rstrip('\n')
    if cnt_line==0:
        print('----------------------------------------------')
        print('Parsing attribute name')
        print('')
        cnt_classes = 0
        cnt_attributes += 1
        # parsing attribute name and index
        attribute_names.append(line)
    else:
        # parsing attribute value
        attributes[cnt_classes, cnt_attributes-1] = int(line)
        print('Class {:02d} \t| Attribute {:02d}'.format(cnt_classes+1, cnt_attributes+1))
        cnt_classes += 1
    if cnt_classes==N_classes:
        cnt_line = 0
    else:
        cnt_line += 1

np.savez(attr_npz_path, attributes, class_names, attribute_names)

#plt.imshow(attributes)
#plt.show()

fig, ax = plt.subplots()
im = ax.imshow(attributes)

# We want to show all ticks...
ax.set_xticks(np.arange(len(attribute_names)))
ax.set_yticks(np.arange(len(class_names)))
# ... and label them with the respective list entries
ax.set_xticklabels(attribute_names)
ax.set_yticklabels(class_names)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(class_names)):
    for j in range(len(attribute_names)):
        text = ax.text(j, i, attributes[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Classes & attributes")
fig.tight_layout()
plt.show()
