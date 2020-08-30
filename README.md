# ResFacenet
This package is intended as a __pytorch hub__ entry point for my trained facenet model on this repo [khrlimam/facenet](https://github.com/khrlimam/facenet).
This pretrained model can be used for anyone who want to use it for transfer learning or any other applications.

This model trained on VGGv2 (used the test set one) dataset and tested on LFW dataset and gained 92% accuracy.

This work is distributed under MIT license, so I hope you consider the license's policy. Cheers!

### How to use
1. First thing first! Please install Pytorch framework by following the installation guide that suites your OS distribution. Refer to this link https://pytorch.org. After you successfully installed the pytorch framework then you're ready to continue to the next step.
2. Install the package `pip install res-facenet`
3. the pretrained model can be used with:
 ```python
from res_facenet.models import model_920, model_921
model920 = model_920()
model921 = model_921()
 ```
 There're two model you can use first `model_920` that is the model with 92% accuracy and `model_921` that is model with 92.135% accuracy.
 After instantiating the model you are free to use the pretrained weight for transfer learning or just to test the model. To use this model for inference you can follow the instructions below:
 ```python
 
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
 
#prepare preprocess pipeline
preprocess_pipelines = [transforms.Resize(224), 
                        transforms.CenterCrop(224), 
                        transforms.ToTensor(), 
                        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                             std=[0.229, 0.224, 0.225])]
trfrm = transforms.Compose(preprocess_pipelines)
topil = transforms.ToPILImage()
totensor = transforms.Compose(preprocess_pipelines[:-1])

# read the image and transform it into tensor then normalize it with our trfrm function pipeline
img1 = trfrm(Image.open(img1_path)).unsqueeze(0)
img2 = trfrm(Image.open(img2_path)).unsqueeze(0)

# do forward pass
embed1, embed2 = model920(a), model920(b)

# compute the distance using euclidean distance of image embeddings
euclidean_distance = F.pairwise_distance(embed1, embed2)

# we use 1.5 threshold to decide wether images are genuine or impostor

threshold = 1.5

genuine = destance <= threshold

 ```
 
 
 The demo app can be found at this repo: http://github.com/khrlimam/demo-facenet
