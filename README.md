# OIDv4-2-YOLO
An extension of Open Images Dataset v4 (OIDv4) toolkit for converting annotations to YOLO format.

```
   o-o  o-O-o o-o         o  o      o          o   o  o-o  o      o-o 
  o   o   |   |  \        |  |      |           \ /  o   o |     o   o
  |   |   |   |   O o   o o--O     -o- o-o       O   |   | |     |   |
  o   o   |   |  /   \ /     |      |  | |       |   o   o |     o   o
   o-o  o-O-o o-o     o      o      o  o-o       o    o-o  O---o  o-o 
```
# Installation

1. Clone this repository <br>
`git clone https://github.com/Daheer/OIDv4-2-YOLO.git`
2. Install the required packages <br>
`pip install -r requirements.txt`
3. Download your OID dataset with [OIDv4 Tooklit](https://github.com/EscVM/OIDv4_ToolKit) <br>
`python OIDv4_Toolkit/main.py downloader --classes Apple Orange --type_csv validation`
4. Run OIDv4 2 YOLO <br>
`python main.py --dataset_path OID/Dataset --yolo_path AppleOrangesDataset --classes Apple Orange`

# Results
```
 AppleOrangesDataset   
  └─ train
  |    │
  |    └─ images
  |    |  └─ 2fe4f21e409f0a56.jpg
  |    |      0fdea8a716155a8e.jpg
  |    └─ labels
  |       └─ 2fe4f21e409f0a56.txt
  |           0fdea8a716155a8e.txt
  └─ validation
  |
  └─ data.yaml
```
We get a dataset that is ready to go into a YOLO model for training <br>
`python train.py --dataset AppleOrangesDataset/data.yaml`

# Contact

<table align = 'center'>
    <tbody>
        <tr>
            <td><a href="mailto: dahiru.ibrahim@outlook.com">
            <img height="50" src="https://www.vectorlogo.zone/logos/gmail/gmail-ar21.svg" />
            </a></td>
            <td><a href="https://www.youtube.com/@deedaxinc">
            <img height="50" src="https://www.vectorlogo.zone/logos/youtube/youtube-ar21.svg" />
            </a></td>
            <td><a href="https://github.com/Daheer/OIDv4-2-YOLO">
            <img height="50" src="https://www.vectorlogo.zone/logos/github/github-ar21.svg" />
            </a></td>
            <td><a href="https://twitter.com/DeedaxInc">
            <img height="50" src="https://www.vectorlogo.zone/logos/twitter/twitter-ar21.svg" />
            </a></td>
            <td><a href="http://instagram.com/deedax_inc">
            <img height="50" src="https://www.vectorlogo.zone/logos/instagram/instagram-ar21.svg"/>
            </a></td>
        </tr>
    </tbody>
</table>
