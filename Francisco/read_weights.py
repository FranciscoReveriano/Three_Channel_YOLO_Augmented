import torch


weights = "/home/franciscoAML/Documents/DSIAC/Five_Classes/Version6/Three_Channel/yolov3/weights/ultralytics68.pt"
weights2 = "/home/franciscoAML/Documents/DSIAC/Five_Classes/Version6/Three_Channel/yolov3/weights/new_coco/Color_YOLOv3_SPP_April.pt"
chkpt = torch.load(weights2)

for param in chkpt["optimizer"]:
    print(param)