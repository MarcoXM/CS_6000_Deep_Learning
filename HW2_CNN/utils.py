import numpy as np
import matplotlib.pyplot as plt




def imshow(img):
    '''
    @ an image array 
    '''
    img = img / 2 + 0.5  # unnormalize
    plt.imshow(np.transpose(img, (1, 2, 0)))  # convert to channel last


def channel_imshow(img):
    '''
    @ an image array 
    '''
    rgb_img = np.squeeze(img)
    channels = ['red channel', 'green channel', 'blue channel']

    fig = plt.figure(figsize = (36, 36)) 
    for idx in np.arange(rgb_img.shape[0]):
        ax = fig.add_subplot(1, 3, idx + 1)
        img = rgb_img[idx]
        ax.imshow(img, cmap='gray')
        ax.set_title(channels[idx])
        width, height = img.shape
        thresh = img.max()/2.5
        for x in range(width):
            for y in range(height):
                val = round(img[x][y],2) if img[x][y] !=0 else 0
                ax.annotate(str(val), xy=(y,x),
                        horizontalalignment='center',
                        verticalalignment='center', size=8,
                        color='white' if img[x][y]<thresh else 'black')
                
