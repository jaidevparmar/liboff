# liboff
LibreOffice + Python + VSCode 

LibreOffice comes with an internal Python that has a rather limited set of functionality. It is suitable for simple macro tasks but is severly limited when it comes to adding packages like numpy, scipy that are needed in scientific computing and big data with Python. LibreOffice could provide a nice presentation frondend for us.

These are my experiences in integrating LibreOffice with [Python](https://www.python.org/) and development using Microsoft Visual Studio Code on Windows (Windows 10+).

You will need to install the following software:
1. [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/)
2. [Miniconda distribution](https://docs.conda.io/en/latest/miniconda.html)
3. [VS Code](https://code.visualstudio.com/)

##Step 1
First we need to determine the version of the internal Python that comes with LibreOffice. 

Download the source code of the this project. It has a file called pythonversion.py, copy this file to 
C:\Program Files\LibreOffice\share\Scripts\python location (If you get a warning that the folder is not writable, you could create a subfolder called myscripts and give it write permission and copy it there). Create a new writer document, then click on Tools\>Macros\>Organize Macros\>Python, the Python Macros Dialog will come up. Now click on pythonversion\>PythonVersion inside the Macros Dialog and click on the Run button. The writer should now display the version of Python that is inbuild in LibreOffice.

