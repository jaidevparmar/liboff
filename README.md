# liboff
LibreOffice + Python + VSCode 

LibreOffice comes with an internal Python that has a rather limited set of functionality. It is suitable for simple macro tasks but is severly limited when it comes to adding packages like numpy, scipy that are needed in scientific computing and big data with Python. LibreOffice would provide a nice presentation frontend for us for data input, output and analysis.

These are my experiences in integrating LibreOffice with [Python](https://www.python.org/) and development using Microsoft Visual Studio Code on Windows (Windows 10+).

You will need to install the following software:
1. [LibreOffice](https://www.libreoffice.org/download/download-libreoffice/)
2. [Miniconda distribution](https://docs.conda.io/en/latest/miniconda.html)
3. [VS Code](https://code.visualstudio.com/)

## Step 1 Get the inbuilt Python Version in LibreOffice
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

As of writing this document the latest version of Python available on Conda site is 3.8.13 but we need version 3.8.14 that is inside LibreOffice. Now even if the minor version of Python (3.8.13) is not matching with the minor version of Python in LibreOffice (3.8.14) they are binary compatible (in theory), For now let's go ahead and install the latest version available in Conda. In future we should upgrade to the exact version when it is available in Conda to be in perfect sync. 

> conda create -n liboff python=3.8.13

![image](https://user-images.githubusercontent.com/117054974/198950244-8e3177fa-1f7c-4b95-8cc3-205d8eed68a0.png)

Once the liboff virtual environment is created we could activate it by using the command

>conda activate liboff

![image](https://user-images.githubusercontent.com/117054974/198951678-32aff44e-8a73-4a61-9ae0-fe252383da5c.png)

## Step 3 Configure VS Code
### Select the python environment created in the previous step
Start the VS Code and select liboff:conda interpreter by clicking on the bottom right button of the status bar. Now open a folder where you wish to create your files.

![image](https://user-images.githubusercontent.com/117054974/199009975-eba8fe03-2afa-45af-bc9a-ec8ca3fc3678.png)

This will bring up the list of Conda environments. We need to select the liboff virtualenv created in the previous step.

![image](https://user-images.githubusercontent.com/117054974/199004394-4a048fac-f86b-44e4-a7b8-ca041dfd3929.png)

### Edit the settings.json file in the workspace
Go to \>File\>Preferences\>Settings and select "Workspace" Tab

![image](https://user-images.githubusercontent.com/117054974/199005327-22df58ec-d738-4ebc-8bc9-e27c5159aed1.png)

In the search bar type "terminal.integrated.env". This will filter the settings to this specific settings variable. Now click on "Edit in settings.json". This will create a new settings.json in the .vscode folder in your workspace. 

![image](https://user-images.githubusercontent.com/117054974/199006017-a5a15d42-1870-4127-825d-ed941d4e9aa4.png)

Add the below variables to your settings.json file.
```json
{
    "terminal.integrated.env.windows": {
        "URE_BOOTSTRAP" : "vnd.sun.star.pathname:C:\\Progra~1\\LibreOffice\\program\\fundamental.ini",
        "UNO_PATH" : "C:\\Progra~1\\LibreOffice\\program",
        "PYTHONPATH" : "${env:PYTHONPATH};C:\\Progra~1\\LibreOffice\\program",
        "PATH" : "${env:PATH};C:\\Progra~1\\LibreOffice\\program"
    },
    "python.analysis.extraPaths": [
        "uno",
        "C:\\Program Files\\LibreOffice\\program"
    ],
}
```
### Start LibreOffice with options to listen on a channel

> "C:\Program Files\LibreOffice\program\soffice.exe" --accept=socket,host=localhost,port=2002;urp;

### Run the test.py script in VS Code

![image](https://user-images.githubusercontent.com/117054974/199015556-d6d00f3c-2f4d-42d8-9d80-5e2b4d7a0e26.png)

If the Default terminal is not set to the cmd (e.g. is set to powershell) then the Conda environment will not activate. You will need to change the default terminal to Windows CMD. This can be down by the drop-down in the terminal that is started and clicking "Select Default Profile"

![image](https://user-images.githubusercontent.com/117054974/199015982-fdcbc27c-46fd-4404-9793-584e1472afd0.png)

Select "Command Prompt" from the drop-down list

![image](https://user-images.githubusercontent.com/117054974/199018226-a4ee2514-4591-4cff-881e-75ea94ed03c4.png)

Again try to run the script and if everything goes fine, you should see a Test.pdf file in the workspace folder!
