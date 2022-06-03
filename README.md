# EGU22 short course

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ESMValGroup/EGU22-short-course/main?labpath=notebooks%2FIntroduction_to_ESMValTool.ipynb)
[![Join the chat at https://gitter.im/ESMValGroup/EGU22-short-course](https://badges.gitter.im/ESMValGroup/EGU22-short-course.svg)](https://gitter.im/ESMValGroup/EGU22-short-course?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Learn to analyze Earth System Model data from a Jupyter Notebook with [ESMValTool](https://docs.esmvaltool.org) at [EGU22](https://www.egu22.eu/) session [SC5.14](https://meetingorganizer.copernicus.org/EGU22/session/43187)

## Location

When: Wed, 25 May, 17:00–18:30 (CEST)

Where: [EGU22](https://www.egu22.eu/) Room -2.85/86 and online

## Abstract
> This Short Course is aimed at researchers in climate-related domains, who have an interest in working with climate data. We will introduce the ESMValTool, a Python project developed to facilitate the analysis of climate data through so-called recipes. An ESMValTool recipe specifies which input data will be used, which preprocessor functions will be applied, and which analytics should be computed. As such, it enables readable and reproducible workflows. The tool takes care of finding, downloading, and preparing data for analysis. It includes a suite of preprocessing functions for commonly used operations on the input data, such as regridding or computation of various statistics, as well as a large collection of established analytics.
>
> In this course, we will run some of the available example recipes using ESMValTool’s convenient Jupyter notebook interface. You will learn how to customize the examples, in order to get started with implementing your own analysis. A number of core developers of ESMValTool will be present to answer any and all questions you may have.
>
> The ESMValTool has been designed to analyze the data produced by Earth System Models participating in the Coupled Model Intercomparison Project (CMIP), but it also supports commonly used observational and re-analysis climate datasets, such as ERA5. Version 2 of the ESMValTool has been specifically developed to target the increased data volume and complexity of CMIP Phase 6 (CMIP6) datasets. ESMValTool comes with a large number of well-established analytics, such as those in Chapter 9 of the Intergovernmental Panel on Climate Change (IPCC) Fifth Assessment Report (AR5) (Flato et al., 2013) and has been extensively used in preparing the figures of the Sixth Assessment Report (AR6). In this way, the evaluation of model results can be made more efficient, thereby enabling scientists to focus on developing more innovative methods of analysis rather than constantly having to "reinvent the wheel".

Based on the examples and instructions in [ESMValTool-JupyterLab](https://github.com/ESMValGroup/ESMValTool-JupyterLab).

## Course material

### Jupyterhub log-in page at DKRZ

https://jupyterhub.dkrz.de

### Repository address for git clone in Jupyter notebook

https://github.com/ESMValGroup/EGU22-short-course.git

### Slides 

[ESMValTool slides at EGU2022 short course](./esmvaltool_slides_EGU2022_short_course.pdf)

### Reference

- [ESMValTool Documentation](https://docs.esmvaltool.org/en/latest/)
- [ESMValTool Website](https://www.esmvaltool.org/)
- [ESMValTool Tutorial](https://esmvalgroup.github.io/ESMValTool_Tutorial/index.html)
- [ESMValGroup Project on GitHub](https://github.com/ESMValGroup)
- [ESMValTool Available Recipes](https://docs.esmvaltool.org/en/latest/recipes/index.html)
- [How to Cite ESMValTool](https://www.esmvaltool.org/references.html)
- [ESGF Nodes](https://esgf.llnl.gov/nodes.html)

## Running the notebooks

*During the short course, you will receive instructions on how to run the notebook.*

If you would like continue using ESMValTool after the course, you can use the instructions available here to start the notebook.

## Binder

Click this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ESMValGroup/EGU22-short-course/main?labpath=notebooks%2FIntroduction_to_ESMValTool.ipynb)
Note that no data is available on Binder and resources are limited, so this is only recommended for running the example notebook in this repository (the tool will automatically download the small amount of data that is required to run the example).
If you would like to run larger analyses, it is recommended that you make use of compute infrastructure that is connected to an [ESGF Node](https://esgf.llnl.gov/nodes.html) because there you have all data already available.
Examples of such compute facilities are [Levante at DKRZ](#Levante-at-DKRZ) and [Jasmin at CEDA](#Jasmin), but many more are available. See the [presentation](./esmvaltool_slides_EGU2022_short_course.pdf) for a longer list.

## Levante at DKRZ

On Levante you cannot (yet) choose ESMValTool from the available notebook environments. But you can add it by following these instructions.

1. Go to https://jupyterhub.dkrz.de and log in
2. Click the `Start` button in the column Preset and row Levante
3. Select job profile `5 GB memory, interactive, 12:00h`, enter account number `bk1088` (or the number of another project at DKRZ that gives you access to compute resources, e.g. `bd0854`), leave the other questions empty and click `Start`. See the [Partitions and Limits](https://docs.dkrz.de/doc/levante/running-jobs/partitions-and-limits.html) webpage for more information.
4. Create a new kernel containing ESMValTool (this step only needs to be done once). Start a terminal session and run the command `mamba create -yq -n esmvaltool esmvaltool ipykernel` and wait a few minutes for the command to complete. Next, make the just created conda environment available as a notebook kernel by running `conda run -n esmvaltool python -m ipykernel install --user --name ESMValTool`.
5. Upload the [config-user-v2.5-levante.yml](config-user-v2.5-levante.yml) file and move it to `~/.esmvaltool/config-user.yml`.
6. When opening a notebook or starting a new empty notebook, select the kernel called "ESMValTool".
7. Stop the jupyter lab server when you're done with it to avoid wasting computational resources. To do this, click `File` and the `Hub Control Panel` and then click the red `Stop` button.

## Jasmin

1. Go to https://notebooks.jasmin.ac.uk and log in
4. Create a new kernel containing ESMValTool (this step only needs to be done once). Open a notebook with the default `python` kernel and run the command `!mamba create -yq -n esmvaltool esmvaltool ipykernel` and wait for the command to complete. This can take up to half an hour. Next, make the just created conda environment available as a notebook kernel by running `!conda run -n esmvaltool python -m ipykernel install --user --name ESMValTool`.
5. Upload the [config-user-v2.5-jasmin.yml](config-user-v2.5-jasmin.yml) file and move it to `~/.esmvaltool/config-user.yml`.
6. When opening a notebook or starting a new empty notebook, select the kernel called "ESMValTool".

## Mistral at DKRZ

A notebook environment for ESMValTool version 2.2 is pre-installed on Mistral. Use it following the instructions below.

1. Go to https://jupyterhub.dkrz.de and log in
2. Click the `Start` button in the column Preset and row Mistral
3. Select job profile `5 GB memory, 1 core, prepost, 12:00h`, enter account number `bk1088` (or the number of another project at DKRZ that gives you access to compute resources, e.g. `bd0854`), leave the other questions empty and click `Start`. Note that only job profiles running on the [`prepost` partition](https://docs.dkrz.de/doc/mistral/running-jobs/partitions-and-limits.html) have internet access.
4. Upload the [config-user-v2.2-mistral.yml](config-user-v2.2-mistral.yml) file and move it to `~/.esmvaltool/config-user.yml`.
5. When opening a notebook or starting a new empty notebook, select the kernel called "ESMValTool (based on the latest module esmvaltool)".
6. Stop the jupyter lab server when you're done with it to avoid wasting computational resources. To do this, click `File` and the `Hub Control Panel` and then click the red `Stop` button.

## Locally

1. Download [mambaforge](https://github.com/conda-forge/miniforge#mambaforge). If you are on a Linux machine, you will most likely need to download [Mambaforge-Linux-x86_64](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh). ESMValTool also works on a Mac, but Windows is not supported because not all our dependencies are available for Windows.
2. Install mambaforge by running `bash Mambaforge-$(uname)-$(uname -m).sh`, answer `yes` when asked if you wish the installer to initialize Mambaforge by running conda init. Finalize the installation by restarting your shell or running `source ~/.basrhc`.
3. Run `mamba create --name esmvaltool jupyterlab esmvaltool=2.5`
4. Run `mamba activate esmvaltool`
5. Run `jupyter lab` to start the notebook server. This will open a browser window with a jupyter lab environment.
6. Navigate to the `notebooks` folder using the menu on the left and open the example notebook. When asked which kernel to use, select the Python 3 kernel.
