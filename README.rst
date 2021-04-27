======================
US Nonprofits Datasets
======================

This repository is a brief exploration of the IRS tax filing data (`EOBMF <https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf>`_ & `990 Extracts <https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data>`_) for tax-exempt entities in the US. 

Installation
---------------------------------
1. ``git clone`` this repository
2. From inside the repo, run ``poetry shell`` to create a venv
3. Then install the modules using ``poetry install``
4. You can then explore the notebook by running ``jupyter notebook notebooks/eda.ipynb`` 


System Requirements
-------------------------------
1. Python 3.X 
2. Poetry 1.1.6 (or latest) (I've found using `pipx <https://pipxproject.github.io/pipx/installation/>`_ is the smoothest to install poetry because it can be installed by simply running ``pipx install poetry``)


Useful Links
-------------------------------
1. `990 Tax Form <https://www.irs.gov/pub/irs-pdf/f990.pdf>`_ 
2. `EOBMF Documentation <https://www.irs.gov/pub/irs-soi/eo_info.pdf>`_