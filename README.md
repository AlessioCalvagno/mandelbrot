# mandelbrot

With this simple python script you can see Mandelbrot fractals through matplotlib library ✨.

Mandelbrot set is an awesome mathematical object that lives in the complex plane, where its boundaries create a very chic fractal structure 😍.

🔍 For more details about Mandelbrot set and its properties, check the [Wikipedia page](https://www.wikiwand.com/en/articles/Mandelbrot_set) 👀.

This script computes, displays and saves an image of a fractal section (see below on how to run the script); the image is saved as `fractal.png`.

![fractal](https://github.com/user-attachments/assets/f3673c99-7951-43a2-9559-37c001b801c8)

# How to run the script

To run script these python packages are required:
- numpy
- matplotlib
- tqdm
  
If not already done, you can install it with pip:

```
pip install numpy matplotlib tqdm
```

Then run script with:
```
py mandelbrot.py
```
After that in the terminal a progess bar will help track computation
![image](https://github.com/user-attachments/assets/2359aba9-a3df-4903-8acf-3fdd36596daf)

And in the end an image will be shown and saved.

# Customize fractal section to plot
Inside `mandelbrot.py` look for `x_img` and `y_img` definition, and change linspace arguments to plot a different section (`x_img` corresponds to Real axis, `y_img` corresponds to Imaginary axis in the complex plane).

```py
x_img = np.linspace(.3,.4,1000)
y_img = np.linspace(.3,.4,1000)
```

Have fun 😁
