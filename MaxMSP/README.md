# PureData patches

The MaxMSP patches can be used for real-time synthesis utilizing the IPF.

*1_IPF_beta.maxpat* provides the core functions to compute the IPF with one additional reflection point $\beta$:

$$ g_+ = g- ln\left( \frac 1 \alpha\left( g - \beta *e^{g-g_-} \right)\right)$$

*2_IPF_beta_applied.maxpat* applies this formula in a patch that allows for iterative calculation of the IPF. 
