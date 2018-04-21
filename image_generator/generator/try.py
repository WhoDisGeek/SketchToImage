import os
from utils import *
with open(os.path.join('/home/prime/ProjectWork/training/dataset/gan_files/images10/labels.txt')) as f:
    data = json.loads(f.read())
images_list = []
labels_list = []
for i in data:
    for j in range(i['count']):
        images_list.append(str(i['index']) + '_' + str(j) + '.jpg')
        labels_list.append(str(i['index']))

sample = [
    get_image(os.path.join('/home/prime/ProjectWork/training/dataset/gan_files/images10/images',image_name),
              input_height=256,
              input_width=256,
              resize_height=256,
              resize_width=256) for image_name in images_list]
X = np.array(sample).astype(np.float32)
y = np.asarray(labels_list).astype(np.int)

seed = 547
np.random.seed(seed)
np.random.shuffle(X)
np.random.seed(seed)
np.random.shuffle(y)

y_vec = np.zeros((len(y), 10), dtype=np.float)
for i, label in enumerate(y):
    y_vec[i, y[i]] = 1.0

print(y_vec)