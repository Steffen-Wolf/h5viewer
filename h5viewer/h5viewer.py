from cremi_tools.viewer.volumina import view
import sys
import h5py
import tkinter as tk
from tkinter import filedialog


def auto_reshape(image):
    dim = len(image.shape)

    if dim == 4:
        return image.transpose((1, 2, 3, 0))
    elif dim == 5:
        return image.transpose((2, 3, 4, 0, 1))
    else:
        return image

if __name__ == '__main__':
    if len(sys.argv) > 1:
        h5path = sys.argv[1]
    else:
        root = tk.Tk()
        root.withdraw()
        h5path = filedialog.askopenfilename()

    images = []
    labels = []

    def visitor_func(name, node):
        if isinstance(node, h5py.Dataset):
            images.append(auto_reshape(node.value))
            labels.append(name)

    with h5py.File(h5path, "r") as f:
        f.visititems(visitor_func)

    view(images, labels=labels)
