# Producing Latex images of equations to be used in GUI's or somewhere else

from PIL import Image
from sympy import preview

# type the equation in the latex form
equation = r'$$\Sigma m_{{\nu}} = 0$$'

# storing the image
preview(equation, viewer='file', filename='masslessnu.png', euler=False,
        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])

# re-size the image if needed
im = Image.open('masslessnu.png')
size = (60, 200)
im.thumbnail(size, Image.ANTIALIAS)
out_dim = im.size
out_name = 'masslessnu.png'
im.save(out_name, "PNG")
im.close()
