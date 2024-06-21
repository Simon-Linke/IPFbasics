# PureData patches

The PureData patches can be used for real-time synthesis utilizing the IPF.

*1_IPF_simple.pd* can be used to calculate the IPF in its most simple Form:

$$ g_+ = g- ln\left( \frac g \alpha \right)$$

Based on this, *2_FM_Synth_simple* shows how to implement a basic FM-synth (combined with some AM) modulated by the IPF.

*3_IPF_beta.pd* can be used to calculate the IPF with an additional reflection point $\beta$.
 
