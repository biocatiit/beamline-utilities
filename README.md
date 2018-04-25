# BioCAT beamline utilities

This project contains miscelanious beamline utilities for the BioCAT beamline (Sector 18) at the APS.

The most useful utilities are:

**beam_size** - which contains scripts for plotting and scanning beam size using the Newport motors and a knife edge.

**pyfai_integration** - which contains scripts for reading in a RAW .cfg file and then
integrating Pilatus 1M .tiff files into .dat files. Note that this needs the compiled polygonMaskingExt file
to be copied from the RAW folder into this folder in order for it to work.
