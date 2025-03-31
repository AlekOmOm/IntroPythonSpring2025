"""

"""

import os
import numpy as np
import matplotlib.pyplot as plt


def get_image(path = 'flower.png'):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(script_dir, path) 

    return plt.imread(img_path)

def Image(image, title):
    return np.array(
        [
            (image,  title)
        ],
        dtype=[('image', 'object'), ('title', 'U32')]
    )

def compare_images(data):
    MAX_COLS = 4 
    SIZE = (5, 5) # 5x5 inches (width, height (aka. columns, rows))

    n = len(data) # number of images (arrays of object and title)
    cols = min(n, MAX_COLS)
    rows = n // cols + 1 # cols + 1, because of the title

    fig, axs = plt.subplots(rows, cols, figsize=(cols * SIZE[0], rows * SIZE[1]))

    axs = np.atleast_1d(axs).flatten()

    data = np.atleast_1d(data).flatten()

    # ----------------------------------------
    for ax, (img, title) in zip(axs, data): # zip: iterate both arrays in parallel
        ax.imshow(img)
        ax.set_title(title)
        ax.axis('off')

    # remove empty axes
    for ax in axs[n:]: 
        ax.axis('off')

    # ----------------------------------------
    #plt.tight_layout()
    plt.show()


# --------------------------------------------
# -------------- main exercises --------------

def read_simple_image():
    img = get_image()

    # Show image
    plt.imshow(img)

    # __main__ that just runs plt.show()
    plt.show()

def read_manipulate_image():
    img = get_image()
    manipulated_img = img.copy()


    manipulated_img[::2, ::2] = 0  # manipulate image
    area = np.array([0, 0, 100, 100]) # at 0,0 with 100x100 size
    zoomed = zoom_image(img, area)
    print (img)
    print (zoomed)


    compare_images([
        Image(img, 'Original'),
        Image(manipulated_img, 'Manipulated'),
        Image(zoomed, 'Zoomed')
    ])

def zoom_image(img, zoom):
    """
    Zoom into an zoom area of an image.
    - img: image to zoom into
    - zoom: 4-tuple (x, y, width, height) of the area to zoom
    """

    zoomed = img[
            zoom[1]:zoom[1]+zoom[3],
            zoom[0]:zoom[0]+zoom[2]]

    return Image(
        zoomed,
        'Zoomed'
    )




# --------------------------------------------
def main():
    #read_simple_image()    
    read_manipulate_image()

if __name__ == '__main__':
    main()
