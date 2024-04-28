Getting Started
===============

This document provides detailed steps to get started with the NYC Taxi Zone Visualization project. Follow these instructions to set up the project on your local machine.

Installation Instructions
-------------------------

**Clone the Repository**
   Clone the project repository to your local machine using the following command:

   .. code-block:: bash

      git clone https://github.com/yourusername/nyc-taxi-zones.git
      cd nyc-taxi-zones

**Install Dependencies**
   Make sure you have Python installed, and then run the following command to install the required Python packages:

   .. code-block:: bash

      pip install -r requirements.txt

**Prepare the Data**
   Execute the data processing scripts to download and prepare the data for visualization. This step involves cleaning and formatting raw data into a structured format:

   .. code-block:: bash

      python src/data/process_data.py

**Generate Visualizations**
   Once the data is prepared, you can generate visualizations by running the visualization scripts:

   .. code-block:: bash

      python src/visualization/visualize.py

Following these steps will set up the NYC Taxi Zone Visualization project on your system, ready for you to run and explore the taxi trip data visualizations.
