# liboff
LibreOffice + Python + VSCode 

LibreOffice comes with an internal Python that has a rather limited set of functionality. It is suitable for simple macro tasks but is severly limited when it comes to adding packages like numpy, scipy that are needed in scientific computing and big data with Python. LibreOffice could provide a nice presentation frondend for us.

These are my experiences in integrating LibreOffice with [Python](https://www.python.org/) and development using Microsoft Visual Studio Code on Windows (Windows 10+).

You will need to install the following software:
1. [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/)
2. [Miniconda distribution](https://docs.conda.io/en/latest/miniconda.html)
3. [VS Code](https://code.visualstudio.com/)

## Step 1 Get inbuilt Python Version in LibreOffice
First step is to determine the version of the internal Python that has come with the installed LibreOffice. 

Download the source code of the this project. It has a file called pythonversion.py, copy this file to 
C:\Program Files\LibreOffice\share\Scripts\python location 
![image](https://user-images.githubusercontent.com/117054974/198940223-e8a79a9f-61a4-41e1-901e-6e18a6429c77.png)

If you get a warning that the folder is not writable, you could create a subfolder called myscripts and give it write permission and copy it there. 
![image](https://user-images.githubusercontent.com/117054974/198940056-67282ce0-fba4-4461-a677-2346e6be07bc.png)

Create a new writer or calc document, then click on Tools\>Macros\>Organize Macros\>Python, the Python Macros Dialog will come up. 
![Macrolocation](https://user-images.githubusercontent.com/117054974/198939409-3c07b7ff-2ee2-473b-855b-a041939d2f2e.png)

Now click on pythonversion\>PythonVersion inside the Macros Dialog and click on the Run button.
![image](https://user-images.githubusercontent.com/117054974/198940650-6c0fc027-75e9-473f-ac5e-6af643644bd1.png)

The writer should now display the version of Python that is inbuilt inside the LibreOffice.
![image](https://user-images.githubusercontent.com/117054974/198942332-016cd4bb-ebba-4e47-bafb-e6ceb9028dcd.png)

## Step 2 Create virtualenv in Miniconda/Anaconda
Start the Miniconda/Anaconda Prompt from the Start Menu or Search

![image](https://user-images.githubusercontent.com/117054974/198943831-72b2bb5e-a695-44c7-b46f-cec785df1a83.png)

As of writing this document the latest version of Python available on Conda site is 3.8.13 but we need version 3.8.14. Even if the minor version of Python (3.8.13) is not matching with the minor version of Python in LibreOffice (3.8.14) they are binary compatible (in theory), in future we could upgrade when the exact version is available to be in sync. For now let's go ahead an install the latest version available in Conda.

> conda create -n liboff python=3.8.13
![image](https://user-images.githubusercontent.com/117054974/198950244-8e3177fa-1f7c-4b95-8cc3-205d8eed68a0.png)
