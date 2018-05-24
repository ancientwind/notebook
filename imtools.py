import os
from PIL import Image

def get_imlist(path):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im,sz):
	pil_im = Image.fromarray(unit8(im))
	return array(pil_im.resize(sz))

