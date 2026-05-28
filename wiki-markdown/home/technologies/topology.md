# Notes from the literature
<img src="/media/wg/news-202204111013564732.png" class="wiki-image" alt="Embedded Image">

<img src="/media/home/technologies/news-202204111013561764.png" class="wiki-image" alt="Embedded Image">

[via [https://www.deltaww.com/en-us/news/Delta-ami-smart-meter](https://www.deltaww.com/en-us/news/Delta-ami-smart-meter) ]

## gridds : A Data Science Toolkit for Energy Grid Machine Learning
https://github.com/LLNL/gridds

<note>MIT License

Copyright (c) 2022 Alexander Ladd
</note>
Recent research on distributed energy resources (DER) has been focused on aggregating data and feedback control to enhance the reliability and performance of energy grid. The ability to forecast load factor at transformers and substations can greatly improve demand and supply side load management. Similarly, detecting incipient failures for key devices in the system can reduce the entire grid failure, which effectively enhances the reliability of the energy grid. Machine learning models, such as fault detection and time series forecasting models, present new and innovative approaches to solving these aforementioned challenges [7, 10, 45].

[There] are many types of identifiable faults, ranging from arching faults, where errant electrical currents discharge energy over the course of several microseconds [11], to distribution management system faults corresponding to load flow over the course of several days [34], to incipient transformer faults over the course of months. Energy standards, such as the Institute of Electrical and Electronics Engineers (IEEE) Standard 1547, [4] and monitoring with wide area monitoring systems (WAMS) [32, 57] have enabled large scale data collection and storage. WAMS for numerous localities are recording and storing advanced metering infrastructure (AMI), outage management systems data (OMS) and supervisory control data acquisition (SCADA), and geographic information systems (GIS).

[https://dl.acm.org/doi/pdf/10.1145/3538637.3539614](https://dl.acm.org/doi/pdf/10.1145/3538637.3539614)

### Anomaly detection
[We] utilize data from a micro-phasor measurement unit (𝜇PMU), a synchrophasor commonly used in WAMS measurement and control of dynamic grid and microgrid applications. 𝜇PMUs report reports four measurements (voltage magnitude, voltage phase angle, current magnitude, and current phase angle per phase) on three phases, resulting in 3 × 4 = 12 channels of highly-resolved data [31]. The utilized 𝜇PMU dataset is sourced from a US-based utility company. For this study, we focused on one month of fault labelled 𝜇PMU data and performed our experiments using three channels of voltage magnitude from this dataset. Results are shown on randomly selected non-contiguous hours of concatenated 𝜇PMU data. Models were trained on 3 randomly selected 1 hour segments of training data consisting of an average of 20 faults. Models are tested using the remaining 14 unseen hours containing roughly 140 faults. This process is repeated through K-Fold cross validation with K=5.

<img src="/media/home/technologies/p542-ladd-supp4.png" class="wiki-image" alt="Embedded Image">

https://colab.research.google.com/github/LLNL/gridds/blob/master/docs/source/autoregression.ipynb

https://colab.research.google.com/github/LLNL/gridds/blob/master/docs/source/autoregression_visualization.ipynb

Touched up requirements.txt:

<csv hdr_rows=0 file=:home:technologies:requirements.csv maxlines=10>requirements.txt</csv>

requirements.txt {{ :home:technologies:requirements.csv |}}

`!git clone https://github.com/LLNL/gridds`

`!pip install -r requirements.txt`

At least one dependency unmet: Our proposed method uses a data-driven deep learning method called Latent Ordinary Differential Equations (LatentODE) for data imputation, followed by a Bayesian non-parametric method called **distance-dependent Chinese Restaurant Franchise** (dd-CRF) for unsupervised discovery of latent states of the energy grid.

<note warning>/content/gridds/experimenter.py in <module>
     17 from abc import ABCMeta, abstractmethod
     18 import numpy as np
---> 19 from ddcrf.run_ddcrf import run_ddcrf
     20 import gridds.tools.utils as utils
     21 from sklearn import preprocessing

ModuleNotFoundError: No module named 'ddcrf'</note>
