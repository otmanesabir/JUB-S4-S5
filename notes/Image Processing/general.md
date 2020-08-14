---
attachments: [elementary_dilation.png]
tags: [ImgProc]
title: Review
created: '2020-05-28T15:54:19.192Z'
modified: '2020-05-29T11:41:34.600Z'
---

# Review

[//]: # (Primary = #BB86FC)
[//]: # (Secondary = #03DAC5)
[//]: # (Secondary = #FF0266)

<h2 style="color:#BB86FC">Basic Operations</h2>
<h3 style="color:#03DAC5">Erosion</h3>

In grayscale morphology, images are functions mapping a Euclidean space or grid $E$ into $\R \cup \{\infty, - \infty\}$, where $\R$ is the set of reals, $\infty$ is an element larger than any real number, and $-\infty$ is an element smaller than any real number.

Denoting an image by $f(x)$ and the grayscale structuring element by $b(x)$, where $B$ is the space that $b(x)$ is defined, the grayscale erosion of $f$ by $b$ is given by
<br>

$(f \ominus b)(x) = inf_{y \in B} [f(x + y) - b(y)]$

Such that $inf$ is the infimum, meaning the greatest element that is less than or equal to all elements within a subset.


<h3 style="color:#03DAC5">Dilation</h3>

Dilation on the other hand, is another basic operatin in mathematical morphology. Given the same Eunclidean space $E$ and a mapping into $R \cup \{\infty, -\infty\}$, where $\R$ is the set of reals, $\infty$ is an element greater than any real number, and $-\infty$ is an element less than any real number.

Denoting an image by $f(x)$ and the grayscale structuring element by $b(x)$, where $B$ is the space that $b(x)$ is defined, the grayscale dilation of $f$ by $b$ is given by

$(f \oplus b)(x) = sup_{y \in B} [f(y) - b(x - y)]$

where $sup$ is the supermum, meaning that the element is the least element in the set that is greater than or equal to all elements of S, if such an element exists.


<h3 style="color:#03DAC5">Opening</h3>

The opening of $A$ by $B$ is obtained by the erosion of A by B, followed by dilation of the resulting image by B:

$A \circ B = (A \ominus B) \oplus B$

In morphological opening, the erosion operation removes the objects that are smaller than structuring element B and the dilation operation (approximately) restores the size and shape of the remaining objects. However, restoration accuracy in the dilation operation depends highly on the type of structuring element and the shape of the restoring objects.


<h3 style="color:#03DAC5">Differences</h3>

This duality property illustrates the fact that erosions and dilations do not process the objects and their background symmetrically: the erosion _shrinks_ the objects but _expands_ their background, while the dilation _expands_ the objects but _shrinks_ their background. Both these operations are increasing transformations.

<h3 style="color:#03DAC5">Important</h3>

Dilation adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries. The number of pixels added or removed from the objects in an image depends on the size and shape of the structuring element used to process the image.

The value of the output pixel is the maximum value of all pixels in the neighborhood. In a binary image, a pixel is set to 1 if any of the neighbouring pixels have the value 1.
Morphological dilation makes objects more visible and fills in small holes in objects.
<br>
For erosion, the value of the output pixel is the _minimum_ value of all pixxelsin the neighbourhood. In a binary image, a pixel is set to 0 if any of the neighboring pixels have the value 0. Morphological erosion removes islands and small objects so that only substantive objects remain.


<h2 style="color:#BB86FC">Noise filtering - bilateral filtering</h2>

<h3 style="color:#03DAC5">Mean Filter</h3>

The idea of mean filtering is simply to replace each pixel value in an image with the mean ('average') value of its neighbors, including itself. This has the effect of eliminating pixels values which are unrepresentative of their surroundings. Mean filtering is usually thought of as a convolution filter - it is based around a kernel.

This filter makes noise less apparent, but the image gets softened.  If the size of the mean filter is increased to 5x5, we obtain an image with less noise and less high frequency detail.

This filter preforms badly in images containing salt and pepper shot noise. Since the shot noise pixels values are often very different from the surrounding values, they tend to significantly distort the pixel average calculated by the mean filter.


Two main problems with mean filtering are:

* A single pixel with a very unrepresentative value can significantly affect the mean valye of all the pixels in its neighborhood.

* When the filter neighborhood straddles an edge, the filter will interpolate the new values for pixels on the edge and so will blur that edge. This is a problem if sharp edges are required.

<h3 style="color:#03DAC5">Median Filter</h3>

The median filter is normally used to reduce noise in an image, somewhat like the mean filter. However, it often does a better job than the mean filter of perserving useful detail in the image.

Like the mean filter, the median filter considers each pixel in the image in turn and looks at its nearby neighbors to decide whether or not it is representative of its surroundings. Instead of simply replacing the pixel value with the _mean of the neighboring pixel values, it replaces it with the _median_ of those values. The median is calculated by first sorting all the pixel values from the surrounding neighborhood into numerical order and then replacing the pixel being considered with the middle pixel value.


This filter has two advantages over the mean filter:

* The median is a more robust average than the mean and so a single very unrepresentative pixel in a neighborhood will not affect the median value significantly.

* Since the median value must actually be the value of one of the pixels in the neighborhood, the median filter does not create new unrealistic pixel values when the filter straddles an edge. For this reason the median filter is much better at perserving sharp edges than the mean filter.

This filter performs a little worse than the mean filter on guassian noise but preforms much better on images with salt and pepper noise.

One of the major problems with the median filter is that it is relatively expensive and complex to compute. To find the median it is necessary to sort all the values in the neighborhood into numerical order and this is relatively slow, even with fast sorting algorithms such as quicksort. 

<h3 style="color:#03DAC5">Guassian Filter</h3>

The Guassian smoothing operator is a 2-D convolution operator that is used to blur images and remove detail and noise. In this sense it is similar to the mean filter, but it uses a different kernel that represents the shape of a Guassian.

The guassian filter is good at dealing with guassian noise but does a bad job at salt and pepper filters since it smears out the noise all around the image.

<h3 style="color:#03DAC5">Bilateral Filter</h3>

The bilateral filter uses the same idea as a weighted average of pixels. It is a blur that favors similar values. 

It is the sum over the image of the value of each pixel weighted by how different it is in intensity so that similar values are considered more and further away is how far it is from the pixel into consideration. The functions are typically guassian. 

The bilateral filter is non-linear, edge perserving and noise-reducing smoothing filter for images.

$BF[I] = \frac{1}{W_p} \Sigma G_{\sigma_s}(||p - q||)G_{\sigma_r}(|I_p - I_q|)I_q$

The bilateral filters in its direct form can introduce several types of image artifacts:

* Staircase effect - intensity plateaus that lead to images appearing like cartoons.
* Gradient reversal - introduction of false edges in the images.


<h2 style="color:#BB86FC">Morophological Reconstruction</h2>

<h3 style="color:#03DAC5">Defintion</h3>

Morphological reconstructrion can be thought of conceptually as repeated dilations of an image, called the marker image, until the contour of the marker image fits under the second image, called the mask image. In morphological reconstruction, the peaks in the marker image "spread out", or dilate. Morphological reconstruction is based on morphological dilate but it does hold the following unique properties:

* Processing is based on two images, a marker and a mask, rather than one image and a structuring element.

* Processing is based on the concept of pixel connectivity, rather than a structuring element.
* Processing repeats until stability, the image no longer changes.

<h3 style="color:#03DAC5">Understanding the Marker and Mask</h3>

Morphological reconstruction processes one image, called the marker, based on the characteristics of another image, called the mask. The high points, or peaks, in the marker image specify where processing begins. The processing continues until the image values stop changing.


<h2 style="color:#BB86FC">Geodesic Transformations</h2>

All morphological transformations discussed so far involved combinations of _one_ input image with specific structuring elements. The approach taken with geodesic transformations is to consider _two_ input images. A morphological transformation is applied to the first image and it is then forced to remain either above or below the second image. Authorized morphological transformations are restricted to elementary erosions and dilations. The choice of specific structuring elements is therefore eluded. 

<h3 style="color:#03DAC5">Elementary geodesic transformations</h3>

We first define the geodesic dilation and the dual geodesic erosion. We then show how to construct a self-dual geodesic transformation by combining these two operations.


<h3 style="color:#FF0266">Geodesic dilation</h3>
A geodesic dilation involves two images, a marker image and a mask image. By definition, both images must have the same definition domain and the mask image must be greater than or equal to the marker image. The marker image is first dilated by the elementary isotropic structuring element. The resulting dilated image is then forced to remain below to the mask image. The mask image acts therefore as a limit to the propogation of the dilation of the marker image.

Let $f$ denote the marker image and $g$ the mask image ($D_f = D_g$ and $f \leq g$). The _geodesic dilation_ of size 1 of the marker image $f$ with respect to the mask image _g_ is denoted $\delta_{g}^{1}(f)$ and is defined as the point-wise minimum between the mask image and the elementary dilation $\delta^1$ of the marker image:

$\delta^{1}_{g}(f) = \delta^{1}(f) \lor g$.

When dealing with binary images, the mask is often refered to as the geodesic mask and the marker image the marker set. Geodesic dilations on binary image and a 1-D signal are illustrated below.

![Icon](@attachment/elementary_dilation.png)

Geodesic dilation of a binary input image or a set $Y$ within a geodesic mask $X$. The marker set is first dilated by the elementary isotropic structuring element and then intersected with the geodesic mask: $\delta_X(Y) = \delta^1(Y) \cap X$


<h3 style="color:#FF0266">Geodesic Erosion</h3>

The geodesic erosion of size $n$ of a marker image $f$ with respect to a mask image $g$ is obtained by performing $n$ successive geodesic erosions of $f$ with respect to $g$:


<h3 style="color:#FF0266">Regional Extrema</h3>

Regional maxima are connected components of pixels with an intensity value t, surrounded by pixels with a lower value.

<h3 style="color:#FF0266">Regional Minima</h3>

Regional minima are connected componenets of pixels with an intensity less than t, surrounded by pixels with a higher value.



<h2 style="color:#BB86FC">Machine Learning</h2>

<h3 style="color:#FF0266">Backpropagation</h3>

Backpropagation aims to minimize the cost function by adjusting network’s weights and biases. The level of adjustment is determined by the gradients of the cost function with respect to those parameters.

<h3 style="color:#FF0266">Activation Function</h3>

Activation functions are mathematical equations that determine the output of a neural network. The function is attached to each neuron in the network, and determines whether it should be activated (“fired”) or not, based on whether each neuron’s input is relevant for the model’s prediction.




