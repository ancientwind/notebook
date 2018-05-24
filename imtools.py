import os
from PIL import Image
from pylab import *

def get_imlist(path):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im,sz):
	pil_im = Image.fromarray(unit8(im))
	return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    '''Histogram equalization of a grayscale image.'''

    # get image histogram
    imhist, bins = histogram(im.flatten(), bins=nbr_bins, normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf

def compute_average(imlist):
    """ Compute the average of a list of images. """
    # open first image and make into array of type float
    averageim = np.array(Image.open(imlist[0]), 'f')
    
    from imname in imlist[2:]:
        try:
            averageim += np.array(Image.open(imname))
        except:
            print(imname, '...skipped')
    averageim /= len(imlist)
    
    return np.array(averageim, dtype='uint8')
