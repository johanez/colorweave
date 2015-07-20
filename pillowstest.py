from PIL import Image as Im
import sys
import os
#import numpy as np
from operator import itemgetter, mul, attrgetter
import glob

def norm_color(c):
    r, g, b = c
    return (r/255.0, g/255.0, b/255.0)

def extract_colors(fn, n):
	im = Im.open(fn)
	print(fn)
	im = im.quantize(colors=n, kmeans=3).convert("RGB")
	#im = im.convert('P', palette=Im.ADAPTIVE, colors=n).convert("RGB")
	#fn = os.path.basename(fn)
	fn = os.path.splitext(fn)[0] + "_kmeans3_" + str(n) + ".jpg"
	print(fn)
	im.save(fn)
	
	#data = im.getdata()
	#unique, counts = np.unique(data, return_counts=True)

	#lut = im.resize((n, 1))

	#lut.putdata(range(n))
	#lut = list(lut.convert("RGB").getdata())
	#print(lut)
	# norm_lut = map(norm_color, lut)
	# print(norm_lut)
	# plt.hist(data)
	# plt.setp(p, 'facecolor', norm_lut)
	# plt.show()
	#n_pixels = mul(*im.size)
	

# print(np.__version__)
flist = glob.glob("in/*.JPG")
#print(os.path.splitext(flist[0]))

for fn in flist:
 	extract_colors(fn, 10)


#extract_colors(flist[0], 10)