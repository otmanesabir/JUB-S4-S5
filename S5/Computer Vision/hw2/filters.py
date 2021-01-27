import numpy as np
from scipy import signal

def conv_nested(image, kernel):
    """A naive implementation of convolution filter.

    This is a naive implementation of convolution using 4 nested for-loops.
    This function computes convolution of an image with a kernel and outputs
    the result that has the same shape as the input image.

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))
    
    image_padded = zero_pad(image, Hk//2, Wk//2)
    kernel = np.flip(kernel)
    ### YOUR CODE HERE
    for i in range(Hi):
        for j in range(Wi):
            for a in range(Hk):
                for b in range(Wk):
                    out[i, j] += image_padded[i + a, j + b]*kernel[a, b]
    ### END YOUR CODE
    return out

def zero_pad(image, pad_height, pad_width):
    """ Zero-pad an image.

    Ex: a 1x1 image [[1]] with pad_height = 1, pad_width = 2 becomes:

        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]         of shape (3, 5)

    Args:
        image: numpy array of shape (H, W).
        pad_width: width of the zero padding (left and right padding).
        pad_height: height of the zero padding (bottom and top padding).

    Returns:
        out: numpy array of shape (H+2*pad_height, W+2*pad_width).
    """

    H, W = image.shape
    out = np.zeros(shape=(H + 2*pad_height, W + pad_width*2)) 
    ### YOUR CODE HERE
    out[pad_height:H+pad_height, pad_width:W+pad_width] = image
    ### END YOUR CODE
    return out


def conv_fast(image, kernel):
    """ An efficient implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Hints:
        - Use the zero_pad function you implemented above
        - There should be two nested for-loops
        - You may find np.flip() and np.sum() useful

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))
    kernel = np.flip(kernel)
    ### YOUR CODE HERE
    padded_image = zero_pad(image, Hk//2, Wk//2)
    out = np.zeros_like(image)
    for x in range(Hi):
        for y in range(Wi):
            out[x, y] = (kernel * padded_image[x:x + Hk, y:y + Wk]).sum()
    return out
    ### END YOUR CODE

def conv_faster(image, kernel):
    """
    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE
    ### Used based on the function provided from Scipy : https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html
    out = signal.convolve2d(image, np.flip(kernel), mode='same')
    ### END YOUR CODE

    return out

def cross_correlation(f, g):
    """ Cross-correlation of f and g.

    Hint: use the conv_fast function defined above.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    out = conv_fast(np.conj(f), g)
    ### END YOUR CODE

    return out

def zero_mean_cross_correlation(f, g):
    """ Zero-mean cross-correlation of f and g.

    Subtract the mean of g from g so that its mean becomes zero.

    Hint: you should look up useful numpy functions online for calculating the mean.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    g -= np.mean(g)
    out = conv_fast(np.conj(f), g)
    ### END YOUR CODE

    return out

def correlation_coefficient(patch1, patch2):
    term1 = np.sum((patch1 - np.mean(patch1))*(patch2 - np.mean(patch2)))
    term2 = np.sqrt(np.sum(np.square(patch1 - np.mean(patch1)))*np.sum(np.square(patch2 - np.mean(patch2))))
    return term1/term2

def normalized_cross_correlation(f, g):
    """ Normalized cross-correlation of f and g.

    Normalize the subimage of f and the template g at each step
    before computing the weighted sum of the two.

    Hint: you should look up useful numpy functions online for calculating 
          the mean and standard deviation.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None

    ### YOUR CODE HERE
    Hi, Wi = f.shape
    Hk, Wk = g.shape

    # Set image, target and result value matrix
    ### YOUR CODE HERE
    padded_image = zero_pad(f, Hk//2, Wk//2)
    out = np.zeros_like(f)
    for x in range(Hi):
        for y in range(Wi):
            out[x, y] = correlation_coefficient(padded_image[x:x + Hk, y:y + Wk], g)
    ### END YOUR CODE
    return out
