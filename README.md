# Simulating landslide sediment transport and runout hazard in Landlab using MassWastingRunout (MWR)
This repository contains Jupyter notebooks, example model inputs and presentations for the Landlab MassWastingRunout Clinic at CSDMS in May 2026.

Training description:
In this hands-on training, participants simulate landslide runout and sediment transport patterns using the model MassWastingRunout (MWR). MWR is coded in Python and implemented as a component for the package Landlab. MWR uses runout algorithms typically found in landscape evolution and watershed sediment yield models to replicate the complex depositional and erosional behavior of actual landslides. It includes a calibration utility For a full description of MWR and the calibration utility refer to [Keck et al., 2024][esurf] 

By the end of this training, participants will have an understanding of how to setup and calibrate MWR to a field site. 

Model inputs for the example field sites are are available online at this [hydroshare][hydroshare] website. MWR can be run at most sites by preparing model inputs following the format of the example inputs. Step-by-step directions for preparing MWR inputs using ArcPro are described in the 


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

The notebooks can be run locally if a user installs Anaconda and the [landlab][landlab] library on their computer.

Click this button: [![Run on EarthscapeHub][badge]][jhub-link] to open the lessons directly on the EarthscapeHub *explore* instance, which is a service provided  by the [OpenEarthscape][openearthscape] project. 

> **Note:** The EarthscapeHub *explore* instance is password-protected.
  Please contact the [CSDMS help desk][help-desk] about obtaining a login,
  or visit [this][jhub-info] CSDMS wiki page for more information.

Development of the Landlab MassWastingRunout has been supported by the NSF grant [ICER-1663859] and NASA Disasters Program grant [80NSSC23K1103].