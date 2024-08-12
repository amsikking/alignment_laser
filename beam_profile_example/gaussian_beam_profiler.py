# Third party imports, installable via pip:
import numpy as np
from scipy.optimize import curve_fit

def fit_gaussian(image, verbose=True, plot=True, bounds=None):
    # define gaussian beam function for optimizer:
    def gaussian_beam(r, bg, I0, r0, w0):
        return bg + I0 * np.exp(-2 * ((r - r0) / w0)**2)
    # make x and y axes:
    y_px, x_px = image.shape
    x, y = range(x_px), range(y_px)
    # max project along x and y axis:
    x_max = np.max(image, axis=0)
    y_max = np.max(image, axis=1)
    if bounds is None:
        # -> specify some (loose) sensible bounds for the optimizer:
        bg_min, bg_max = 0, 10 * np.min(image)              # background
        I0_min, I0_max = np.min(image), 2 * np.max(image)   # peak intensity
        mean_min, mean_max = 0, max(x_px, y_px)             # mean
        w0_min, w0_max = 0, max(x_px, y_px)                 # beam 1/e^2 radius        
        bounds = ((bg_min, I0_min, mean_min, w0_min),
                  (bg_max, I0_max, mean_max, w0_max))
    # run the curve fit optimizer:
    xp = curve_fit(gaussian_beam, x, x_max, bounds=bounds)[0]  # x parameters
    yp = curve_fit(gaussian_beam, y, y_max, bounds=bounds)[0]  # y parameters
    xp = np.append(xp, (2 * np.log(2))**0.5 * xp[3]) # add x FWHM
    yp = np.append(yp, (2 * np.log(2))**0.5 * yp[3]) # add y FWHM
    if verbose:
        print('image shape =', image.shape)
        print('x: bg=%0.2f, I0=%0.2f, r0=%0.2f, w0=%0.2f, FWHM=%0.2f'%tuple(xp))
        print('y: bg=%0.2f, I0=%0.2f, r0=%0.2f, w0=%0.2f, FWHM=%0.2f'%tuple(yp))
    if plot:
        # calculate the smooth profile curves:
        x_crv = gaussian_beam(x, *xp[:-1])
        y_crv = gaussian_beam(y, *yp[:-1])
        # plot:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.set_title('Gaussian fit')
        ax.set_ylabel('intensity')
        ax.set_xlabel('pixels')
        ax.plot(x, x_max, color='g', label='x_max', linestyle='--')
        ax.plot(x, x_crv, color='g', label='x_curve: (FWHM=%0.1f)'%xp[4])
        ax.plot(y, y_max, color='b', label='y_max', linestyle='--')
        ax.plot(y, y_crv, color='b', label='y_curve: (FWHM=%0.1f)'%yp[4])
        ax.legend(loc="upper right")
        fig.savefig('guassian_fit', dpi=150)
        fig.show()
    return xp, yp

def get_beam_diameter_mm(xy_parameters, um_per_px, verbose=True):
    # the 1/e^2 diameter:
    x_d0_mm = 1e-3 * 2 * xy_parameters[0][3] * um_per_px # um_per_px from camera
    y_d0_mm = 1e-3 * 2 * xy_parameters[1][3] * um_per_px
    if verbose:
        print('d0_mm = %0.3f, %0.3f, %0.3f (x, y, x/y)'%(
            x_d0_mm, y_d0_mm, x_d0_mm/y_d0_mm))
    return x_d0_mm, y_d0_mm

if __name__ == '__main__':
    # get image:
    from tifffile import imread, imwrite
    image = imread('beam_profile.tif')

    # fit guassian and get parameters:
    xp, yp = fit_gaussian(image, verbose=True, plot=True)

    # get beam diameters based on camera pixel size:
    x_d0_mm, y_d0_mm = get_beam_diameter_mm((xp, yp), um_per_px=3.45)

