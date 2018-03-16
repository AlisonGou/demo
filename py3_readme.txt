Starting at 10.5, ArcGIS Server provides the option to use a Python 3 runtime 
for command-line ArcPy scripts. In earlier releases of ArcGIS Server on Linux, 
Python scripts could only be executed in a Linux shell using the Python 2  
runtime included with ArcGIS Server. This experience had limitations regarding 
the use of third-party libraries and working with paths. As of ArcGIS Server 
10.5, select tools can be executed with a Python 3 runtime that is installed 
independently of ArcGIS Server. You can also publish items to a portal with a 
built-in identity store. 

You will need to set up the Python 3 runtime for ArcGIS Server on the same 
machine where ArcGIS Server 10.6 is installed. They both need to be installed 
under the same user account, and ArcGIS Server needs to be authorized properly.  
For supported Linux operating systems, please refer to the ArcGIS Server 10.6 
System Requirements:
http://server.arcgis.com/en/server/latest/install/linux/arcgis-for-server-system-requirements.htm

Install using Conda
===================
The Python 3 runtime for ArcGIS Server on Linux is distributed via conda. 
Conda is a popular package and environment manager application that helps you 
install and update packages and their dependencies. To learn more about conda, 
see the getting started guide for conda:
http://conda.pydata.org/docs/get-started.html

Get Conda
=========
Install the latest version of Anaconda for Python, if you don't already have 
conda. The Python 3 runtime for ArcGIS Server on Linux requires a 64-bit 
installer:
https://www.continuum.io/downloads#linux


Install arcgis-server-10.6-py3 package
======================================
1) If you have already created a conda environment, download and install the 
   Python 3 runtime for ArcGIS Server on Linux using the following command in 
   your terminal:
   conda install -c esri arcgis-server-10.6-py3

   Or, use conda to create a new environment and install arcgis-server-10.6-py3 
   package with this command:
   conda create -c esri -n <condaEnv> arcgis-server-10.6-py3

2) In your terminal, set the ARCGISHOME variable to the installation directory 
   of ArcGIS Server 10.6:
   export ARCGISHOME=/path/to/arcgis/server

   You will need to set the ARCGISHOME variable every time to activate the 
   conda environment for the Python 3 runtime for ArcGIS Server. 

3) Activate the environment by using the following command:
   source activate <condaEnv>

4) When you are done working with ArcPy, deactivate the environment with this 
   command:
   source deactivate <condaEnv>
 
   For more information about managing conda environments, refer to the conda 
   documentation:
   http://conda.pydata.org/docs/using/envs.html
    
Test your install
=================
In the conda environment where the Python 3 runtime for ArcGIS Server is 
installed, run the following command to import arcpy:
(<condaEnv>) [user@servername ~]$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import arcpy
>>> quit()

If the import command produced no messages, you're ready to work with ArcPy
on Linux.

Make sure the correct Python interpreter is being run by using the following 
command:
which python

The path to Python interpreter should be from: 
/path/to/anaconda3/envs/<condaEnv>/bin/python

Now you are setup to use a Python 3 runtime for command-line ArcPy scripts.

Known limitations
=================
For multiprocessing functionality, the default Linux fork mode should be 
avoided for native Linux ArcPy. At this time, please use spawn or forkserver 
mode instead. These modes were introduced with Python 3.4 and work with native 
Linux ArcPy. For reference, see:
https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods


https://conda.io/docs/user-guide/tasks/manage-environments.html
