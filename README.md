# EGU22 short course

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ESMValGroup/EGU22-short-course/main?labpath=notebooks%2F1_Introduction_to_ESMValTool.ipynb)
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

## Running the notebooks

## ESMValTool v2.2 on Mistral at DKRZ

A notebook environment for ESMValTool version 2.2 is pre-installed on Mistral. Use it following the instructions below.

1. Go to https://jupyterhub.dkrz.de and log in
2. Click the `Start` button in the column Preset and row Mistral
3. Select job profile `5 GB memory, 1 core, prepost, 12:00h`, enter account number `bk1088` (or the number of another project at DKRZ that gives you access to compute resources, e.g. `bd0854`), leave the other questions empty and click `Start`. Note that only job profiles running on the [`prepost` partition](https://docs.dkrz.de/doc/mistral/running-jobs/partitions-and-limits.html) have internet access.
4. Upload the [config-user-v2.2-mistral.yml](config-user-v2.2-mistral.yml) file and move it to `~/.esmvaltool/config-user.yml`.
5. When opening a notebook or starting a new empty notebook, select the kernel called "ESMValTool (based on the latest module esmvaltool)".
6. Stop the jupyter lab server when you're done with it to avoid wasting computational resources. To do this, click `File` and the `Hub Control Panel` and then click the red `Stop` button.

## ESMValTool v2.5 on Levante at DKRZ

On Levante you cannot (yet) choose ESMValTool from the available notebook environments. But you can add it by following these instructions. 

1. Go to https://jupyterhub.dkrz.de and log in
2. Click the `Start` button in the column Preset and row Levante
3. Select job profile `5 GB memory, interactive, 12:00h`, enter account number `bk1088` (or the number of another project at DKRZ that gives you access to compute resources, e.g. `bd0854`), leave the other questions empty and click `Start`. See the [Partitions and Limits](https://docs.dkrz.de/doc/levante/running-jobs/partitions-and-limits.html) webpage for more information.
4. Create a new kernel containing ESMValTool (this step only needs to be done once). Start a terminal session and run the command `mamba create -yq -n esmvaltool esmvaltool ipykernel` and wait a few minutes for the command to complete. Next, make the just created conda environment available as a notebook kernel by running `conda run -n esmvaltool python -m ipykernel install --user --name ESMValTool`.
5. Upload the [config-user-v2.5-levante.yml](config-user-v2.5-levante.yml) file and move it to `~/.esmvaltool/config-user.yml`.
6. When opening a notebook or starting a new empty notebook, select the kernel called "ESMValTool".
7. Stop the jupyter lab server when you're done with it to avoid wasting computational resources. To do this, click `File` and the `Hub Control Panel` and then click the red `Stop` button.

## ESMValTool v2.5 on Jasmin

1. Go to https://notebooks.jasmin.ac.uk and log in
4. Create a new kernel containing ESMValTool (this step only needs to be done once). Open a notebook with the default `python` kernel and run the command `!mamba create -yq -n esmvaltool esmvaltool ipykernel` and wait for the command to complete. This can take up to half an hour. Next, make the just created conda environment available as a notebook kernel by running `!conda run -n esmvaltool python -m ipykernel install --user --name ESMValTool`.
5. Upload the [config-user-v2.5-jasmin.yml](config-user-v2.5-jasmin.yml) file and move it to `~/.esmvaltool/config-user.yml`.
6. When opening a notebook or starting a new empty notebook, select the kernel called "ESMValTool".
