# MaxMSP patches

The MaxMSP patches can be used for real-time synthesis utilizing the IPF.

*1_IPF_beta.maxpat* provides the core functions to compute the IPF with one additional reflection point $\beta$:

$$ g_+ = g- ln\left( \frac 1 \alpha\left( g - \beta *e^{g-g_-} \right)\right)$$

*2_IPF_beta_applied.maxpat* applies this formula in a patch that allows for iterative calculation of the IPF. 

*3_Additiv_Synth.maxpat*  is an Example of the IPF modulating the spectrum of a sound using additive synthesis.

*4_sgran-ipf.maxpat* uses the IPF to modulate the shape and width of the probability distribution for an advanced granular synthesis based on [stochgran-tilde](https://github.com/trian-gles/stochgran-tilde) (see: K. McAuliffe, M. Helmuth (2023). The New Stochgran: Expanded Granular Synthesis Tools. In: Proceedings of the ICMC 2023
Shenzen, China)
