# Simulating landslide sediment transport and runout hazard in Landlab using MassWastingRunout
Jupyter notebooks, example model inputs and presentations for the Landlab MassWastingRunout Clinic at CSDMS in May 2026.

Clinic description:
In this hands-on clinic, participants will simulate landslide runout and sediment transport patterns using the model MassWastingRunout (MWR). MWR is coded in Python and implemented as a component for the package Landlab. MWR uses runout algorithms typically found in landscape evolution and watershed sediment yield models to replicate the complex depositional and erosional behavior of actual landslides. Additional details on MWR be found here: https://esurf.copernicus.org/articles/12/1165/2024/.

By the end of the clinic, it is hoped that participants will have an understanding of how to setup and calibrate MWR to a field site. This clinic consists of a series of brief presentations followed by hands-on Jupyter notebook tutorials. It is divided into three sections: (1) MWR model conceptualization, behavior and limitations, illustrated on virtual terrains; (2) MWR performance at an actual field site and; (3) How to use MWR’s calibration utility to parameterize MWR to site specific landslide runout behavior.

At the end of the second and third sections, we will assist those who wish to set up MWR for their own field site or one of the other example field sites. Model inputs for the example field sites will be provided but can also be found at the link below. MWR can be run at most sites by preparing model inputs following the format of the example inputs.

Example model inputs: https://www.hydroshare.org/resource/55813a5e01764546b76641a7385c2236/

 
 <!-- Links -->
[badge]: https://img.shields.io/badge/Run%20on-EarthscapeHub-orange
[help-desk]: https://csdms.github.io/help-desk/
[jhub]: https://csdms.colorado.edu/wiki/JupyterHub
[jhub-link]: https://explore.openearthscape.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fpfeiffea%2FNST-Clinic-CSDMS-2025&urlpath=tree%2FNST-Clinic-CSDMS-2025%2F&branch=main 


[jhub-info]: https://csdms.colorado.edu/wiki/JupyterHub
[landlab]: https://landlab.readthedocs.io/en/latest/installation.html
[openearthscape]: https://csdms.colorado.edu/wiki/OpenEarthscape

[esurf]:https://esurf.copernicus.org/articles/12/1165/2024/
[tutorials]:https://landlab.csdms.io/generated/tutorials/index.html
[hydroshare]:https://www.hydroshare.org/resource/55813a5e01764546b76641a7385c2236/

The notebooks can be run locally
if a user installs Anaconda and the [landlab][landlab] library on their computer.

Additional example inputs can be found on [hydroshare][hydroshare].

Click this button: [![Run on EarthscapeHub][badge]][jhub-link] to open the lessons directly on the EarthscapeHub *explore* instance, which is a service provided  by the [OpenEarthscape][openearthscape] project. 

> **Note:** The EarthscapeHub *explore* instance is password-protected.
  Please contact the [CSDMS help desk][help-desk] about obtaining a login,
  or visit [this][jhub-info] CSDMS wiki page for more information.

MassWastingRunout and the calibrator utility are described in [Keck et al., 2024][esurf] 

Development of the Landlab MassWastingRunout has been supported by the NSF grant [ICER-1663859] and NASA Disasters Program grant [80NSSC23K1103].
