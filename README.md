# Outflows_large-sample

The goal of this work is to investigate the impact of cold molecular gas on local star formation in spiral arms of the Milky Way galaxy. Particularly, the focus is on the Cygnus X region, a site for active star formation in the local arm.  
There are four main results on this work,

1. Predicting mass, momentum, and energy of molecular outflows in Cyg X from 12CO(3-2) Spectral line emission data - 
  Typically, we need 3 separate spectral lines, namely, 12CO, 13CO, and C18O, for estimating these quantities. However, the last two are observationally expensive. Hence, we had developed an empirical model that can be used to infer these quantities from 12CO data alone. This was done by using all observatons available for a small sample of outflows. (Project link - ). 

2.  The role of outflows in turbulence support for host molecular clouds - 
  We find indication that outflows may be capable of reshaping their local environment, and influencing local star formation in their ambient clouds in Cygnus X. This influence is larger at smaller length scales and diminishes with increasing size of the ambient cloud. 


3. Outflow efficiency & handling missing data with machine learning - 
  Many of the outflows in our study were previously unknown, and their corresponding protostars are unidentified. We estimate the missing protostellar luminosity values using a supervised learning with imposed regularization. I find mechanical luminosity ~  1/1000 of Infrared Luminosity on average, which traces the accretion power. This is consistent with other studies (e.g., Wu et al. 2004). 

4. Influence of local stellar feedback on protostar formation -
  Cygnus X being
a site for many young stars and a rich deposit of molecular gas raises
the question whether there is evidence of triggering in this region.
(Deb et al. 2018) discussed such a case of potential triggering. In this
section we investigate this by looking into any potential association
between radiative feedback and protostellar formation. 


These codes take observational values of outflow candidates as input variables (positions of blue-and redshifted pixels and velocity ranges) and generate visual maps and outflows properties as output (mass, momentum, energy)


