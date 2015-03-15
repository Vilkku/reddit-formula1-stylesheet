from os import listdir, path
from PIL import Image
import subprocess
import sys

flair_directory = path.join(path.dirname(__file__), 'flair')
sheet_output = 'sheet.png'
css_output = 'flair.css'

try:
    subprocess.check_call(['montage', path.join(flair_directory, '*'), '-tile', '1x', '-geometry', '20x16+1+1', '-background', 'none', 'sheet.png'])
except subprocess.CalledProcessError:
    pass
except OSError:
    sys.exit('Error calling ImageMagick montage')

try:
    subprocess.check_call(['optipng', sheet_output])
except subprocess.CalledProcessError:
    pass
except OSError:
    print 'Error calling OptiPNG, output has not been optimized'

css_flair = []
vpos = 1

for i, name in enumerate(listdir(flair_directory)):
    im = Image.open(path.join(flair_directory, name))
    width, height = im.size
    name = name.split('.')
    name = name[0].replace(' ', '').replace('-', '')
    css_flair.append('.flair-%(name)s:before{background-position:-1px -%(vpos)dpx}' % {'name': name, 'vpos': vpos})
    # 2 is the padding around the image which is set in the montage geometry option
    vpos = vpos + (height+2)

fo = open(css_output, 'w')
fo.write('\n'.join(css_flair))
fo.close()
