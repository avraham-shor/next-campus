import sys
# import gi.overrides.Gtk as gui
saved_argv = sys.argv.copy()
sys.argv = []
from gi import repository
sys.argv = saved_argv

from PIL import Image, Image

image = Image.open('miri.JPG')
photo = PhotoImage(image)
print(image)

# gui.Label = 'ma nishma'

# print(gui.Label('ma nishma'))
#
# print(help(gui.Label))
#
# print()