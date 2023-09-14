.. _code-based-approaches:

Thematic code based approaches
------------------------------
Developing your own code can be time consuming, but offers the most flexible way of working Earth observation data and opens up a near-unlimited range of options for visualisation. `R <https://www.r-project.org/>`_, and Python are two of the most commonly used open-source languages for geospatial work, and there are a large number of libraries that support working with satellite data in both cases. 

Both R and Python are supported by Project Jupyter, allowing them to be used to construct `Jupyter Notebooks <https://jupyter.org/>`_ which facilitate training on using code. The landscape of available code options is ever changing, and publishing a comprehensive list of them here will be immediately out of date. 

However, we can recommend some start points.

* A catalogue of Jupyter Notebooks for working with Copernicus marine and atmosphere data can be found in the `WEkEO Copernicus DIAS <https://notebooks.apps.mercator.dpi.wekeo.eu/>`_ catalog

.. raw:: html

    <embed>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">⚙️ Unlock the power of data processing with our <a href="https://twitter.com/hashtag/JupyterLab?src=hash&amp;ref_src=twsrc%5Etfw">#JupyterLab</a>!<br><br>Analyze and share data-driven insights using this versatile environment 💻<br><br>Experience how cloud computing enables collaborative workflows and efficient data exploration 🔍<a href="https://t.co/5UxAkRaSqj">https://t.co/5UxAkRaSqj</a> <a href="https://t.co/12hvIS1iBr">pic.twitter.com/12hvIS1iBr</a></p>&mdash; WEkEO_dias (@WEkEO_dias) <a href="https://twitter.com/WEkEO_dias/status/1692093557799059503?ref_src=twsrc%5Etfw">August 17, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </embed>


* If you are working with EUMETSAT data you will find all of our Python based training code on our `EUMETLAB GitLab group <https://gitlab.eumetsat.int/eumetlab>`_. This contains a number of repositories containing Jupyter Notebooks showing how to work with our marine and atmospheric composition data.
* Jupyter Notebooks on `dust <https://dust.trainhub.eumetsat.int/docs/index.html>`_, `aerosol <https://dust.trainhub.eumetsat.int/docs/index.html>`_ and `fire <https://fire.trainhub.eumetsat.int/docs/index.html>`_ detection can be found on the EUMETSAT TrainHub portal.
* The `SatPy python package <https://satpy.readthedocs.io/en/stable/>`_ offers extensive options for data visualisation for those working with weather satellites.
* `Radiant Earth <https://mlhub.earth/>`_ provide Jupyter Notebooks and training data to help you work with Earth observation data and machine learning techniques. 

There are also a variety of cloud based infrastructures that can support you in connecting code to data.

* The `Copernicus WEkEO Data and Information Access System (DIAS) <https://www.wekeo.eu/>`_ cloud platform offers a free Jupyter Hub that you can use to develop cloud-based code to exploit many Copernicus data records, including those from the Sentinel satellite series. It also offers a scalable cloud infrastructure for more advanced data processing.
* `Google Earth Engine <https://earthengine.google.com/>`_ can be used to explore a wide catalogue of free and open satellite data, particularly when the application is focussed on land applications.

------------

.. image:: ../../../img/footer.png
   :width: 50%
   :alt: Copernicus implementation logo
   :align: right