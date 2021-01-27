import numpy as np

def conv(image, kernel):
    """ An implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    # For this assignment, we will use edge values to pad the images.
    # Zero padding will make derivatives at the image boundary very big,
    # whereas we want to ignore the edges at the boundary.
    pad_width0 = Hk // 2
    pad_width1 = Wk // 2
    pad_width = ((pad_width0,pad_width0),(pad_width1,pad_width1))
    padded = np.pad(image, pad_width, mode='edge')

    ### YOUR CODE HERE
    kernel = np.flip(kernel)
    for x in range(Hi):
        for y in range(Wi):
            out[x, y] = (kernel * padded[x:x + Hk, y:y + Wk]).sum()
    ### END YOUR CODE

    return out

def gaussian_kernel(size, sigma):
    """ Implementation of Gaussian Kernel.

    This function follows the gaussian kernel formula,
    and creates a kernel matrix.

    Hints:
    - Use np.pi and np.exp to compute pi and exp.

    Args:
        size: int of the size of output matrix.
        sigma: float of sigma to calculate kernel.

    Returns:
        kernel: numpy array of shape (size, size).
    """

    kernel = np.zeros((size, size))

    ### YOUR CODE HERE
    k = (size -  1)//2
    for i in range(size):
        for j in range(size): 
            nom = np.exp(-(np.square(i - k) + np.square(j - k)) / 2*np.square(sigma))
            den = 2*np.pi*np.square(sigma)
            kernel[i][j] = nom / den
    ### END YOUR CODE

    return kernel

def partial_x(img):
    """ Computes partial x-derivative of input img.

    Hints:
        - You may use the conv function in defined in this file.

    Args:
        img: numpy array of shape (H, W).
    Returns:
        out: x-derivative image.
    """


    ### YOUR CODE HERE
    image = np.copy(img)
    Dx = np.array([[0, 0, 0], [0.5, 0, -0.5], [0, 0, 0]])
    out = conv(image, Dx)
    ### END YOUR CODE

    return out

def partial_y(img):
    """ Computes partial y-derivative of input img.

    Hints:
        - You may use the conv function in defined in this file.

    Args:
        img: numpy array of shape (H, W).
    Returns:
        out: y-derivative image.
    """

    ### YOUR CODE HERE
    image = np.copy(img)
    Dy = np.array([[0, 0.5, 0], [0, 0, 0], [0, -0.5, 0]])
    out = conv(image, Dy)
    ### END YOUR CODE

    return out

def gradient(img):
    """ Returns gradient magnitude and direction of input img.

    Args:
        img: Grayscale image. Numpy array of shape (H, W).

    Returns:
        G: Magnitude of gradient at each pixel in img.
            Numpy array of shape (H, W).
        theta: Direction(in degrees, 0 <= theta < 360) of gradient
            at each pixel in img. Numpy array of shape (H, W).

    Hints:
        - Use np.sqrt and np.arctan2 to calculate square root and arctan
    """
    G = np.zeros(img.shape)
    theta = np.zeros(img.shape)

    ### YOUR CODE HERE
    H, W = img.shape
    image = np.copy(img)
    Gx = partial_x(image)
    Gy = partial_y(image)
    G = np.sqrt(Gx**2 + Gy**2)
    theta = np.arctan2(Gy, Gx)
    theta = theta  * 180 / np.pi
    for i in range(H):
        for j in range(W):
            if theta[i,j] < 0:
                theta[i,j] = -theta[i,j]
    ### END YOUR CODE
    return G, theta

def non_maximum_suppression(G, theta):
    """ Performs non-maximum suppression.

    This function performs non-maximum suppression along the direction
    of gradient (theta) on the gradient magnitude image (G).

    Args:
        G: gradient magnitude image with shape of (H, W).
        theta: direction of gradients with shape of (H, W).

    Returns:
        out: non-maxima suppressed image.
    """
    H, W = G.shape
    out = np.zeros((H, W))

    # Round the gradient direction to the nearest 45 degrees
    theta = np.floor((theta + 22.5) / 45) * 45
    ### BEGIN YOUR CODE
    Gpad = np.pad(G, ((1,1),(1,1)), mode='edge')
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            try:
                out[i, j] = 0
                comp_val = 255
                if theta[i - 1, j - 1] == 0.0 or theta[i - 1, j - 1] == 180.0:
                    comp_val = max(Gpad[i, j - 1], Gpad[i, j + 1])
                elif theta[i - 1, j - 1] == 45.0:
                    comp_val = max(Gpad[i-1, j+1], Gpad[i+1, j-1])
                elif theta[i - 1, j - 1] == 90.0:
                    comp_val = max(Gpad[i  + 1, j], Gpad[i - 1, j])
                elif (theta[i - 1, j - 1] == 135.0):
                    comp_val = max(Gpad[i-1, j-1], Gpad[i+1, j+1])
                if (Gpad[i,j] >= comp_val):
                    out[i - 1,j - 1] = Gpad[i, j]
                else:
                    out[i - 1,j - 1] = 0
            except IndexError:
                continue
    ### END YOUR CODE
    return out

def double_thresholding(img, high, low):
    """
    Args:
        img: numpy array of shape (H, W) representing NMS edge response.
        high: high threshold(float) for strong edges.
        low: low threshold(float) for weak edges.

    Returns:
        strong_edges: Boolean array representing strong edges.
            Strong edeges are the pixels with the values greater than
            the higher threshold.
        weak_edges: Boolean array representing weak edges.
            Weak edges are the pixels with the values smaller or equal to the
            higher threshold and greater than the lower threshold.
    """

    strong_edges = np.zeros(img.shape, dtype=np.bool)
    weak_edges = np.zeros(img.shape, dtype=np.bool)
    H, W = img.shape
    ### YOUR CODE HERE

    for i in range(H):
        for j in range(W):
            if img[i, j] >= high:
                strong_edges[i, j] = True
            elif img[i, j] >= low and img[i, j] < high:
                weak_edges[i, j] = True

    ### END YOUR CODE

    return strong_edges, weak_edges


def get_neighbors(y, x, H, W):
    """ Return indices of valid neighbors of (y, x).

    Return indices of all the valid neighbors of (y, x) in an array of
    shape (H, W). An index (i, j) of a valid neighbor should satisfy
    the following:
        1. i >= 0 and i < H
        2. j >= 0 and j < W
        3. (i, j) != (y, x)

    Args:
        y, x: location of the pixel.
        H, W: size of the image.
    Returns:
        neighbors: list of indices of neighboring pixels [(i, j)].
    """
    neighbors = []

    for i in (y-1, y, y+1):
        for j in (x-1, x, x+1):
            if i >= 0 and i < H and j >= 0 and j < W:
                if (i == y and j == x):
                    continue
                neighbors.append((i, j))

    return neighbors

def link_edges(strong_edges, weak_edges):
    """ Find weak edges connected to strong edges and link them.

    Iterate over each pixel in strong_edges and perform breadth first
    search across the connected pixels in weak_edges to link them.
    Here we consider a pixel (a, b) is connected to a pixel (c, d)
    if (a, b) is one of the eight neighboring pixels of (c, d).

    Args:
        strong_edges: binary image of shape (H, W).
        weak_edges: binary image of shape (H, W).
    
    Returns:
        edges: numpy boolean array of shape(H, W).
    """

    H, W = strong_edges.shape
    indices = np.stack(np.nonzero(strong_edges)).T
    edges = np.zeros((H, W), dtype=np.bool)

    # Make new instances of arguments to leave the original
    # references intact
    weak_edges = np.copy(weak_edges)
    edges = np.copy(strong_edges)

    ### YOUR CODE HERE
    for i in range(H):
        for j in range(W):
            if (weak_edges[i, j] == True):
                for x, y in get_neighbors(i, j, H, W):
                    if (strong_edges[x, y]):
                        edges[i, j] = True

    ### END YOUR CODE

    return edges

def canny(img, kernel_size=5, sigma=1.4, high=20, low=15):
    """ Implement canny edge detector by calling functions above.

    Args:
        img: binary image of shape (H, W).
        kernel_size: int of size for kernel matrix.
        sigma: float for calculating kernel.
        high: high threshold for strong edges.
        low: low threashold for weak edges.
    Returns:
        edge: numpy array of shape(H, W).
    """
    ### YOUR CODE HERE
    edge = np.zeros(img.shape)
    kernel = gaussian_kernel(kernel_size, sigma)
    smoothed = conv(img, kernel)
    G, theta = gradient(smoothed)
    nms = non_maximum_suppression(G, theta)
    strong_edges, weak_edges = double_thresholding(nms, high, low)
    edge = link_edges(strong_edges, weak_edges)
    ### END YOUR CODE

    return edge


def hough_transform(img):
    """ Transform points in the input image into Hough space.

    Use the parameterization:
        rho = x * cos(theta) + y * sin(theta)
    to transform a point (x,y) to a sine-like function in Hough space.

    Args:
        img: binary image of shape (H, W).
        
    Returns:
        accumulator: numpy array of shape (m, n).
        rhos: numpy array of shape (m, ).
        thetas: numpy array of shape (n, ).
    """
   # Rho and Theta ranges
    thetas = np.deg2rad(np.arange(-90.0, 90.0))
    width, height = img.shape
    diag_len = np.ceil(np.sqrt(width * width + height * height))   # max_dist
    rhos = np.linspace(-diag_len, diag_len, int(diag_len * 2.0))
    
    # Cache some resuable values
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)
    
    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((int(2 * diag_len), num_thetas), dtype=np.uint64)
    y_idxs, x_idxs = np.nonzero(img)  # (row, col) indexes to edges
    
    # Vote in the hough accumulator
    for i in range(len(x_idxs)):
      x = x_idxs[i]
      y = y_idxs[i]
    
      for t_idx in range(num_thetas):
        # Calculate rho. diag_len is added for a positive index
        rho = int(round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len)
        accumulator[rho, t_idx] += 1
    
    return accumulator, thetas, rhos
