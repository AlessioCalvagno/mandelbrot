import cmath
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def main():

    # x_img = np.linspace(-2,1.5,500)
    # y_img = np.linspace(-2,2,500)

    x_img = np.linspace(.3,.4,1000)
    y_img = np.linspace(.3,.4,1000)


    max_iter = 1000
    z = 0 + 0j

    img = []

    t = tqdm(total=len(x_img)*len(y_img), desc="Mandelbrot set computation: ")
    for y in y_img:
        img_row = []
        for x in x_img:
            c = complex(x,y)
            z = 0 + 0j
            for i in range(1,max_iter):
                
                if (abs(z) > 2):
                    img_row.append(i)
                    break
                z = z**2 + c
            else:
                img_row.append(0)
            t.update()

        
        img.append(img_row)

    t.close()
    img_arr = np.array(img)

    plt.imsave("fractal.png",img_arr,cmap="magma", origin="lower")

    plt.figure()
    # plt.imshow(img_arr,cmap="magma")
    plt.pcolormesh(x_img,y_img,img_arr,cmap="magma")
    plt.axis("scaled")
    # plt.colorbar()
    plt.show()
    return 


if __name__ == '__main__' :
    main()

