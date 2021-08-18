# Producing Latex images of equations to be used in GUI's or somewhere else

from PIL import Image
from sympy import preview

# type the equation in the latex form
equation = r'$$g_{00}$$'

# storing the image
preview(equation, viewer='file', filename='g00.png', euler=False,
        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 600', '-bg', 'Transparent'])

# re-size the image if needed
im = Image.open('g00.png')
size = (20, 200)
im.thumbnail(size, Image.ANTIALIAS)
out_dim = im.size
out_name = 'g00.png'
im.save(out_name, "PNG")
im.close()
