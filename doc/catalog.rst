============
The Catalog
============

The access to geospatial data has changed significantly over the past decade. Data has traditionally been accessed by downloading several files to a local computer, then analyzing them with software or programming languages. It has always been difficult to access analysis-ready datasets due to the diversity of data formats (NetCDF, Grib2, Geotiff, Shapefile, etc.) and the variety of access protocols from different providers (Opendap, HTTPS, SFTP, WPS, API Rest, Datamarts, etc.). Beyond that, with the ever-increasing size of geospatial datasets, most modern datasets cannot even fit on a local computer, limiting science's progress.

The catalog presented here consists of large-scale analysis-ready cloud optimized (ARCO) datasets. In order to implement an entry point for these datasets, we have followed the methodology developed by the Pangeo community, which combines multiple technologies:

- Data Lake (or S3, Azure Data Lake Storage, GCS, etc.) : distributed file-object storage
- `Zarr <https://zarr.readthedocs.io/en/stable/>`_ (or alternatively TileDB, COGs) : chunked N-dimensionnal array formats
- `Dask <https://docs.dask.org/en/stable/>`_  (or alternatively Spark, Ray, Distributed) : distributed computing and lazy loading
- `Intake <https://intake.readthedocs.io/en/latest>`_ Catalogs (or alternatively STAC) : a general interface for loading different data formats, mostly but not limited to spatiotemporal assets

For more information, please refer to the `pangeo's website <https://pangeo.io/>`_.

It is important to keep in mind that most datasets in the catalogue have language-agnostic formats (such as Zarr, netcdfs, geojson, etc.), making them accessible through a variety of programming languages (including Python, Julia, Javascript, C, etc.) that implement the specifications for these formats.

   atmosphere