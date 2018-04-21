import os
import shutil
import json

root_dir = '/home/prime/ProjectWork/training/dataset'
current_dataset_path = 'sketchy/images and sketches mapped/256x256/photo/tx_000000000000'
final_root_dir = os.path.join(root_dir, 'gan_files')
final_dataset_name = 'images10'

classes_list_path = 'classes10.txt'
classes_list = []
with open(classes_list_path) as f:
    classes_list.extend(f.read().splitlines())

os.chdir(root_dir)
folder_count = 0
labels = []
list_of_all_classes = os.listdir(current_dataset_path)

os.makedirs(os.path.join(final_root_dir, final_dataset_name, 'images'), exist_ok=True)
for c in classes_list:
    # print(os.path.join(rootDir,current_dataset,sub_dir))
    # if os.path.isdir(os.path.join(rootDir,sub_dir)):
    # print('in ', sub_dir)

    if c in list_of_all_classes:
        print(c, ' Exists')
    else:
        print(c, "Doesn't Exists")
        continue


    count = 0

    for filename in os.listdir(os.path.join(root_dir, current_dataset_path, c)):
        # print(filename)
        initial_img = os.path.join(root_dir, current_dataset_path, c, filename)
        final_filename = str(folder_count) + '_' + str(count) + '.jpg'
        final_img = os.path.join(final_root_dir, final_dataset_name, 'images', final_filename)
        shutil.copy(initial_img, final_img)
        count = count + 1

    # print({'index': folder_count,
    #        'name': c,
    #        'count': count
    #        })

    labels.append({'index': folder_count,
                   'name': c,
                   'count': count
                   })
    folder_count = folder_count + 1
# print(labels)
# for i in labels:
#     print(i)

with open(os.path.join(final_root_dir, final_dataset_name, 'labels.txt'), 'w') as outfile:
    dump = json.dumps(labels)
    outfile.write(dump)
