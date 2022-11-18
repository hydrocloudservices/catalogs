.. catalogs documentation master file, created by
   sphinx-quickstart on Thu Nov 17 08:44:52 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

EO-catalog documentation
====================================
Introduction
--------
eo-catalog is a catalog of Earth observation big data whose objective is to facilitate access to data by an exhaustive documentation of the steps required to get there.

This project does not want to reinvent the wheel. We use technologies that are already well established in the field of earth observation to format and organize our datasets (intake, STAC, zarr, netcdf, etc.). When not required, we don't change anything in a dataset, we just point to the original provider's servers. What we do however is that we maintain one single catalog from multiple providers and for each dataset, we document the steps required to access it in multiple programming languages. For some datasets, we also take extra steps such as rechunking the data, deaggregate or decumulate some variables, all to make life easier for users.

This project was born out of a fundamental need to share common data sources when we were doing research. We collaborate with researchers, engineers, data scientists from academia to industry. In multidisciplinary projects, we have experienced difficulties in sharing and working on large common datasets. Although the centralization of data brought by cloud computing has made this task easier for us, the fact remains that there is still a significant learning curve to interact with these datasets and that the documentation to achieve this via different programming languages is sometimes limited.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   notebooks/ipynb/catalog
   notebooks/ipynb/index.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
