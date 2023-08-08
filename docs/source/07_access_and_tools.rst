.. _access-data-tools:

Access to Earth observation data and tools for visualisation
============================================================

A wide variety of ways exist to access and work with Earth observation data for visualisation purposes. Which data access routes and/or visualisation tools an individual chooses will depend on some combination of the following considerations:

* Is an appropriate "off-the-shelf" visualisation is readily available through an existing service (quicker/easier/less flexible), or do you need to develop your own approach (slower/more difficult/more flexible)?
* Is a single image enough to illustrate the complexity of the topic, or are a series of images/animation needed?
* Is imagery suitable and sufficient on it's own, or is more detailed data analysis and visualisation required?

Below, we present some visualising approaches that address these considerations, beginning with the most convenient and least complex and proceeding in order of complexity until we arrive at code-based tools that offer unlimited flexibility.

.. _viewers:

Viewers
-------
Viewers are online platforms that show spatial maps or imagery based on underlying data sets. In general, these maps are based on pre-generated layers and do not show the data itself (e.g. in the case of a Web Mapping Service or WMS).

* `EUMETView <https://view.eumetsat.int/>`_

Many viewers extend their capability to offer either analysis tools to interrogate/manipulate the data, or links to the primary data itself.

* `MyOcean Pro <https://data.marine.copernicus.eu/viewer/expert>`_
* `Sentinel Hub EO Browser <https://apps.sentinel-hub.com/eo-browser>`_
* `KNMI climate explorer <https://climexp.knmi.nl/start.cgi>`_

.. _dashboards:

Dashboards
----------
Dashboards typically bring together data from various sources to either give an up-to-date snapshot of a region, or show how a system is varying in time.

* `OSI SAF sea ice dashboard <https://osisaf-hl.met.no/v2p1-sea-ice-index>`_
* `Met Norway Sea ice viewer <https://cryo.met.no/en/sea-ice-index>`_
* `Copernicus Atmopsheric Monitoring Service NRT portal <https://atmosphere.copernicus.eu/charts/packages/cams/>`_
* `Le Monde climate dashboard <https://www.lemonde.fr/les-decodeurs/article/2023/04/28/neuf-indicateurs-pour-mesurer-l-urgence-climatique_6148399_4355771.html>`_

.. _software-packages:

Software for image generation and analysis
------------------------------------------
Where "off the shelf" options for data visualisation do not exist, it is often necessary to use specific software packages to generate your own. Below is a list of some of the commonly used open-source software packages for working with Earth observation data. 

* `SNAP <https://step.esa.int/main/download/snap-download/>`_
* `QGIS <https://www.qgis.org/en/site/>`_
* `Copernicus Marine Service QGIS plugin <https://marine.copernicus.eu/services/user-learning-services/qgis-plugin-cmems-netcdf>`_

.. _code-based-approaches:

Thematic code based approaches
------------------------------
Developing your own code can be time consuming, but offers the most flexible way of working Earth observation data and opens up a near-unlimited range of options for visualisation. R, and in particular Python, are two of the most commonly used open-source languages for geospatial work, and there are a large number of libraries that support working with satellite data in both cases. Both R and Python are supported by Project Jupyter, allowing them to be used to construct Jupyter Notebooks which facilitate training on using code. The landscape of available code options is ever changing, and publishing a comprehensive list of them here will be immediately out of date. However, we can recommend some start points. 

* If you are working with EUMETSAT data you will find all of our Python based training code on our `EUMETLAB GitLab group <https://gitlab.eumetsat.int/eumetlab>`_. This contains a number of repositories containing Jupyter Notebooks showing how to work with our marine and atmospheric composition data.
* A similar catalogue of Jupyter Notebooks can be found in the `WEkEO Copernicus DIAS <https://www.wekeo.eu/>`_ catalog
* Jupyter Books on `dust <https://dust.trainhub.eumetsat.int/docs/index.html>`_, `aerosol <https://dust.trainhub.eumetsat.int/docs/index.html>`_ and `fire https://fire.trainhub.eumetsat.int/docs/index.html>`_ detection can be found on the EUMETSAT TrainHub portal.
* The `SatPy python package <https://satpy.readthedocs.io/en/stable/>`_ offers extensive options for data visualisation for those working with weather satellites.

Reports
-------
* `Copernicus Marine Service State of the Ocean report <https://marine.copernicus.eu/access-data/ocean-state-report/ocean-state-report-6>`_
* `Copernicus Climate Change Service state of the climate report <https://climate.copernicus.eu/esotc/2022/globe-in-2022>`_

