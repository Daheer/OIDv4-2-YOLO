from parser import args
from converter import run_toolkit

if __name__ == '__main__':

  file_path = args.dataset_path
  yolo_path = args.yolo_path
  classes = args.classes

  run_toolkit(file_path, yolo_path, classes)

  print(f'\n Done processing {yolo_path}')