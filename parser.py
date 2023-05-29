import argparse

parser = argparse.ArgumentParser(description='Toolkit Parser')

parser.add_argument('-d', '--dataset_path', type = str, required=True, help='Path to the dataset downloaded with OID Tooklit e.g. OID/Dataset')
parser.add_argument('-y', '--yolo_path', type = str, default = './YOLO_Dataset', help='Path to save the YOLO dataset')
parser.add_argument('-c', '--classes', type = str, nargs = '+', help='Same as classes flag used in OID Tooklit. Separated by single space')

args = parser.parse_args()