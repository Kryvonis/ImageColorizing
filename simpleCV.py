from PIL import Image, ImageChops
from matplotlib.pyplot import imshow,show

def image_overlay(src, color):
    hair = Image.open(src)
    color = Image.new("RGBA", hair.size, (*color,255))
    white = Image.new("RGBA", hair.size, (0, 0, 0, 0))
    res_mul = ImageChops.multiply(hair, color)
    res_mul.save("steps/1.png")
    res_scr = ImageChops.screen(res_mul, res_mul)
    res_scr.save("steps/2.png")
    res = Image.composite(res_scr, white, hair)
    return res


def image_color(src, color):
    hair = Image.open(src)
    color = Image.new("RGBA", hair.size, color)
    white_col = Image.new("RGBA", hair.size, (0, 0, 0, 0))
    res = Image.blend(hair, color, alpha=0.6)
    res = Image.composite(res, white_col, hair)
    return res


def image_multiply(src, color):
    hair = Image.open(src)
    color = Image.new("RGBA", hair.size, color)
    white_col = Image.new("RGBA", hair.size, (0, 0, 0, 0))
    res = ImageChops.multiply(hair, color)
    res = Image.composite(res, white_col, hair)
    return res


# image_color('images/ab_thumb_female_hair_straight_long.png').save("test.color.png")
im_res = image_overlay('images/imgpsh_fullsize.png', (38, 170, 119)).save("skin_image_overlay_f89e40.png")

# res = Image.fromqimage(im_res)
# res.save('overlay_f89e40')
# im_res.save("overlay_f89e40")
# image_overlay('images/ab_thumb_female_hair_straight_long.png', [221, 89, 38]).save('overlay_dd5926')

# ###############
# #### COLOR ####
# ###############
# color = (248,158,64,255)
# white = (0,0,0,0)
# hair = Image.open('images/ab_thumb_female_hair_straight_long.png')
# color = Image.new("RGBA",hair.size,color)
# white_col = Image.new("RGBA",hair.size,white)
# # res = Image.alpha_composite(hair,color)
# # res = ImageChops.blend(color,hair,2)
# res = Image.blend(hair,color,alpha=0.6)
# res = Image.composite(res,white_col,hair)
# res.save("test_color.png")
#
# ##################
# #### MULTIPLY #### TESTED OK
# ##################
# color = (198,94,66,255) #c65e42
# white = (0,0,0,0)
#
# hair = Image.open('images/ab_thumb_female_hair_straight_long.png')
# color = Image.new("RGBA",hair.size,color)
# white_col = Image.new("RGBA",hair.size,white)
#
# res = ImageChops.multiply(hair,color)
# res = Image.composite(res,white_col,hair)
# res.save("test_multiply_c65e42.png")
#################
#### OVERLAY ####
#################

# color = (248, 158, 64, 255)
# white = (0, 0, 0, 0)
# hair = Image.open('images/ab_thumb_female_hair_straight_long.png')
# color = Image.new("RGBA", hair.size, color)
# white = Image.new("RGBA", hair.size, white)
#
# res_mul = ImageChops.multiply(hair, color)
# res_mul.save("steps/1.png")
# res_scr = ImageChops.screen(res_mul, res_mul)
# res_scr.save("steps/2.png")
# res = Image.composite(res_scr, white, hair)
#
# res.save("test_overlay_f89e40.png")
#
# color = (221, 89, 38, 255)
# white = (0, 0, 0, 0)
# hair = Image.open('images/ab_thumb_female_hair_straight_long.png')
# color = Image.new("RGBA", hair.size, color)
# white = Image.new("RGBA", hair.size, white)
#
# res_mul = ImageChops.multiply(hair, color)
# res_mul.save("steps/1.png")
# res_scr = ImageChops.screen(res_mul, res_mul)
# res_scr.save("steps/2.png")
# res = Image.composite(res_scr, white, hair)
#
# res.save("test_overlay_dd5926.png")


# imshow(res)
# # mh.imsave('test.png', images.astype(numpy.uint8))
# show()
