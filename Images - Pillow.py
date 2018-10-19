from PIL import Image
from PIL import ImageFilter

img = Image.open('Vladan, July-August 2014 (8).JPG')
# img = Image.open('Tallinn 2014 (469).JPG')

'''
print(img.size)                                 # img size in pixels
print(img.mode)                                 # RGB, CMYK,... (most often it will be RGB)
print(img.format)                               # JPG, PNG,...
img.show()                                      # open img in the default image viewer (Photos, Photoshop,...)
img.save('Vladan, July-August 2014 (8).png')    # save img in a different format, like png

cropped_img = img.crop((2000, 100, 2600, 700))  # crop the original image specifying the area to crop (in pixels),
cropped_img.show()                              # i.e. the coordinates of the upper left and the lower right corners

signature_img = Image.open('My Signature GIF.gif')
area = (500, 500, 1287, 692)
img.paste(signature_img, area)                  # paste another image on top of img, given the area where to paste;
img.show()                                      # make sure to do the corresponding math, area MUST correspond to
                                                # the area of the other image (signature_img in this case)

r, g, b = img.split()                           # split img into its RGB channels / bands / components
r.show()
g.show()
b.show()
# new_img_1 = Image.merge("RGB", (r, g, b))       # merge an RGB image from its channels / bands / components
new_img_1 = Image.merge("RGB", (g, b, r))       # change the order of channels to get some cool effects
new_img_1.show()

img2 = Image.open('Tallinn 2014 (469).JPG')
r2, g2, b2 = img2.split()
new_img_2 = Image.merge("RGB", (g, b2, r2))     # combine channels from different images for some ghostly effects
new_img_2.show()

img.show()                                      # open img in the default image viewer (Photos, Photoshop,...)
img_resized = img.resize((300, 300))            # resize img to a desired size (img distortions can occur)
img_resized.show()                              # open img in the default image viewer (Photos, Photoshop,...)

img_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)   # flip img left to right, top to bottom, or just rotate it
img_rotate = img.transpose(Image.ROTATE_90)         # rotate image 90 degrees counterclockwise
img_rotate_arbitrary = img.rotate(-30)              # rotate image 30 degrees clockwise
                                                    # see http://matthiaseisen.com/pp/patterns/p0201/ for more rotation
img_mirror.show()
img_rotate.show()
img_rotate_arbitrary.show()

img_bw = img.convert('L')                       # convert img to B/W (L stands for luminosity)
img_blur = img.filter(ImageFilter.BLUR)         # blur img
img_blur = img.filter(ImageFilter.GaussianBlur(12))         # blur img more heavily; default is 2, and 12 blurs it well
img_details = img.filter(ImageFilter.DETAIL)    # highlight details
img_edges = img.filter(ImageFilter.FIND_EDGES)  # find edges ("bold" lines)
img_bw.show()
img_blur.show()
img_details.show()
img_edges.show()
'''
