import os
import shutil
from tqdm.auto import tqdm
import imagesize
import yaml

def run_toolkit(path_to_dataset, path_to_yolo, classes):
  
  print("""
   o-o  o-O-o o-o         o  o      o          o   o  o-o  o      o-o 
  o   o   |   |  \        |  |      |           \ /  o   o |     o   o
  |   |   |   |   O o   o o--O     -o- o-o       O   |   | |     |   |
  o   o   |   |  /   \ /     |      |  | |       |   o   o |     o   o
   o-o  o-O-o o-o     o      o      o  o-o       o    o-o  O---o  o-o                                                                                                   
  """
  )

  # -------------------------------
  # Generate YOLO dataset structure
  # -------------------------------
  # main_folder   
  # └─- train
  # |    │
  # |    └─- images
  # |    |   └─- 2fe4f21e409f0a56.jpg
  # |    |       0fdea8a716155a8e.jpg
  # |    └─- labels
  # |        └-─ 2fe4f21e409f0a56.txt
  # |            0fdea8a716155a8e.txt
  # └-─ validation
  # |
  # └-─ data.yaml

  os.mkdir(path_to_yolo) if not os.path.exists(path_to_yolo) else None
  splits = os.listdir(path_to_dataset)

  # create paths for YOLO splits and OID splits and zip them e.g. ('/content/OID/Dataset', '/content/YOLO_Dataset')
  yolo_splits_paths = list(map(lambda split: os.path.join(path_to_yolo, split), splits))
  oid_splits_paths = list(map(lambda split: os.path.join(path_to_dataset, split), splits))
  splits_paths = zip(oid_splits_paths, yolo_splits_paths)

  _ = [
      os.mkdir(path) or os.mkdir(os.path.join(path, 'images')) or os.mkdir(os.path.join(path, 'labels'))
      for path in yolo_splits_paths if not os.path.exists(path)
      ]

  # create a dictionary to map class names to indices
  labels_dictionary = {
    class_name: index
    for index, class_name in enumerate(classes)
  }

  # ------------------------
  # Process each split found
  # ------------------------

  for oid, yolo in splits_paths:
    for class_name in os.listdir(oid):

      images_path = os.path.join(oid, class_name)
      labels_path = os.path.join(images_path, 'Label')
      
      # process each image in the current class
      for image in tqdm(os.listdir(images_path), desc = f'Processing {class_name}'):
        if image.endswith('jpg'):
        
          width, height = imagesize.get(os.path.join(images_path, image))
          label_path = os.path.join(labels_path, image[:-3] + 'txt')
      
          lines = []
      
          with open(label_path, 'r') as f:
            for line in f.readlines():
      
              line = line.split()
              
              # replace class names with their corresponding indices
              line[0] = str(labels_dictionary[line[0]])

              # ---------------------------------------------------
              # Convert bounding box coordinates from xyxy --> xywh
              # ---------------------------------------------------

              # normalize bounding box coordinates
              bbox_left = min([float(line[1])/width, float(line[3])/width])
              bbox_top = min([float(line[2])/height, float(line[4])/height])
              bbox_w = abs(float(line[1])/width - float(line[3])/width)
              bbox_h = abs(float(line[2])/height - float(line[4])/height)
      
              # convert
              line[1] = str((bbox_left + bbox_w / 2))
              line[2] = str((bbox_top + bbox_h / 2))
              line[3] = str(bbox_w)
              line[4] = str(bbox_h)
      
              lines.append(' '.join(line) + '\n')
      
          shutil.copy2(os.path.join(images_path, image), os.path.join(yolo, 'images', image))
      
          # write the corresponsing .txt file
          with open(os.path.join(yolo, 'labels', image[:-3] + 'txt'), 'w') as f:
            for line in lines:
              f.write(line)

  # create the data dictionary for the data.yaml file
  data = {
      'train': '../train/images' if os.path.exists(path_to_yolo + '/train') else None,
      'val': '../validation/images' if os.path.exists(path_to_yolo + '/validation') else None,
      'test': '../test/images' if os.path.exists(path_to_yolo + '/test') else None,
      'nc': len(classes),  
      'names': classes 
  }

  # write the data.yaml file
  with open(os.path.join(path_to_yolo, 'data.yaml'), 'w') as file:
      documents = yaml.dump(data, file)