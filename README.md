# ResFacenet
This package is intended as an __pytorch hub__ entry point for my trained facenet model on this repo [khrlimam/facenet](https://github.com/khrlimam/facenet).
This pretrained model can be used for anyone who want to use it for transfer learning or any other applications.

This model trained on VGGv2 dataset and tested on LFW dataset and gained 92% accuracy.

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
 After instantiating the model you are free to use the pretrained weight for transfer learning or just to test the model.
 The demo app can be found at this repo: http://github.com/khrlimam/demo-facenet