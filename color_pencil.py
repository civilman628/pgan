#!/usr/bin/env python
# encoding: utf-8

"""
=================================================
color pencil drawing implementation
usage:
    cd {file directory}
    python color_pencil.py {path of img file you want to try}
"""


import numpy as np
import sys
from PIL import Image
from pencil import get_s, get_t, save_output
import cv2


def color_draw(im, gammaS=1, gammaI=0.1):
    #im = Image.open(path)
    im=Image.fromarray(im,mode='RGB')

    if im.mode == 'RGB':
        ycbcr = im.convert('YCbCr')
        Iruv = np.ndarray((im.size[1], im.size[0], 3), 'u1', ycbcr.tobytes())
        type = "colour"
    else:
        Iruv = np.array(im)
        type = "black"

    S = get_s(Iruv[:, :, 0], gammaS=gammaS)
    #T = get_t(Iruv[:, :, 0], type, gammaI=gammaI)
    Ypencil = S # S * T

    new_Iruv = Iruv.copy()
    new_Iruv.flags.writeable = True
    new_Iruv[:, :, 0] = Ypencil * 255
    colorpencil = np.array ( Image.fromarray(new_Iruv,'YCbCr').convert('RGB'),dtype='uint8')
    #sketch = np.array(S*255,dtype='uint8')
    
    return colorpencil

    #R = cv2.cvtColor(new_Iruv, cv2.COLOR_YCR_CB2BGR)
    #img = Image.fromarray(R)
    # img.show()

    #name = path.rsplit("/")[-1].split(".")[0]
    #suffix = path.rsplit("/")[-1].split(".")[1]

    #save_output(Image.fromarray(S * 255), name + "_s", suffix)
    #save_output(Image.fromarray(T * 255), name + "_t", suffix)
    #save_output(img, name + "_color", suffix)

'''
if __name__ == "__main__":
    import time
    start = time.time()
    args = sys.argv
    length = len(args)
    if length > 1:
        path = args[1]
        color_draw(path=path)
    else:
        color_draw()
    print ('time consumes: {}'.format(time.time() - start))
'''