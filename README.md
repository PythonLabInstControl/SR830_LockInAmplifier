SR830_LockInAmplifier
=====================

Library for connecting to the Stanford Lock-In Amplifier SR830. (for Linux/Windows)

#### How to get our code

#####Linux:

* Start Command Prompt
* ```sudo apt-get install git-core``` see http://git-scm.com/book/en/v2/Getting-Started-Installing-Git for further information
* ```git clone https://github.com/PythonLabInstControl/SR830_LockInAmplifier.git```

#####Windows:
* Get git for Windows: http://git-scm.com/download/win (download will start automatically)
  * Note that this is a project called Git for Windows (also called msysGit), which is separate from Git itself; for more information on it, go to: http://msysgit.github.io/
  * Another way to get git installed is by installing GitHub for Windows. The installer includes a command line version of Git as well as a GUI: https://windows.github.com/
  * For those of you, who want to use a simple shell in Windows I recommend Cmder, a portable console emulator for Windows with an awesome git integration: http://bliker.github.io/cmder/
* Click the button "Download ZIP" or (within your shell): 

  ```git clone https://github.com/PythonLabInstControl/SR830_LockInAmplifier.git```

#### How to install required drivers

#####Linux:
If you want to download the instructions in form of a pdf-file follow [this link](https://github.com/PythonLabInstControl/SR830_LockInAmplifier/blob/master/GPIB-USB-HS_Configuration_Manual_Linux.pdf) and click the button "Raw" for downloading,
otherwise just follow the instructions bellow:

######Introduction

This manual guides step by step how to set up a **NI\_USB\_GPIB\_HS** adapter under a linux operating system (e.g. Ubuntu). It is an edited summary of following links:

-   <https://twiki.cern.ch/twiki/bin/view/Main/GpibLinux>

-   [http://www.cl.cam.ac.uk/\(\sim\)osc22/tutorials/gpib\_usb\_linux.html](http://www.cl.cam.ac.uk/~osc22/tutorials/gpib_usb_linux.html)

-   <http://rfpoweramp.wordpress.com/2014/07/26/setting-up-ni-gpib-usb-hs-under-linux/>

######Linux GPIB Package

1. update all programm packages: ```sudo apt-get update```

2. download the GPIB package from <http://sourceforge.net/projects/linux-gpib/?source=dlp> and unpack the file 
   (```tar -zxvf \<packagename\>```)

3. install the package with: ```sudo ./configure && sudo make && sudo make install```

The package is correctly installed if no error occurs while importing it in Python (preferable Python 2.7): ```import Gpib```

######Load and set up Kernel Module

1. load Kernel module **ni\_usb\_gpib.ko** (usually at **/lib/modules/3.13.0-35-generic/gpib/ni\_usb**, where the number of the x.xx.x-xx-generic directory can be different)

    ```cd /lib/modules/x.xx.x-xx-generic/gpib/ni_usb```

    ```sudo modprobe ni_usb_gpib```

2. change entry in file **/etc/gpib.conf**

    ```board_type = "ni_usb_b"```
    
    ```name = "gpib0"```

3. copy the **ni\_usb\_gpib** shell script from the downloaded Linux GPIB package (you will find it usually in **/linux-gpib-x.x.xx/usb/ni\_usb\_gpib**) to **/lib/udev**.

4. create a new udev[1] rule:
   create filename **99-linux\_gpib\_ni\_usb.rules** in directory
   **/etc/udev/rules.d/** with following content:
   ```
       SUBSYSTEM=="usb", ACTION=="add", ENV{DEVTYPE}=="usb_device", 
       ATTR{idVendor}=="3923", ATTR{idProduct}=="709b", MODE="660",
       GROUP="plugdev", SYMLINK+="usb_gpib"
       SUBSYSTEM=="usb", ACTION=="add", ENV{DEVTYPE}=="usb_device",
       ATTR{idVendor}=="3923",ATTR{idProduct}=="709b", 
       RUN+="/lib/udev/ni_usb_gpib"    
       KERNEL=="gpib[0-9]*", ACTION=="add", MODE="660", GROUP="plugdev"
   ```
   Notice the specific idProduct number **709b**, for **NI\_USB\_GPIB\_HS** adapter only!
   All idProduct numbers for connected devices can be checked in the terminal with the **lsusb** command.

5. update udev rules: ```sudo udevadm control --reload-rules```

######How to use the Adapter

To get full access to the adapter interface after plug in do:

-   ```sudo gpib_config```

-   ```sudo spyder```

[1] for further information visit <http://en.wikipedia.org/wiki/Udev>

#####Windows:

######Install required software
1. Install **NI-488.2 3.1.2** from http://www.ni.com/download/ni-488.2-3.1.2/4360/en/

   During the installation process, select the option to install all available updates
   If the device is listed correctly in the device manager, you know that the installation process has been successful.
2. Install **PyVISA 1.6**
   * either from the official Website: https://pypi.python.org/pypi/PyVISA
   * or from http://www.lfd.uci.edu/~gohlke/pythonlibs/

######Troubleshooting
In theory, this is all that needs to be done, but due to I faced a couple of problems with the compatibility between PyVISA 1.6 and Python 2.7 this section describes these problems and their solutions.

Problem 1: ```ImportError: No module named pkg_resources```

Solution 1:
  - Install curl
  - ...

#### How to work with Github
In this section I am going to explain one way how you can work with Github. To work in an efficient way use the terminal in Linux and [Cmder](http://bliker.github.io/cmder/) in Windows. Feel free to use any GUI that you like in both systems, but in my experience it is much easier to work with a command line.

##### Command Explanation
```git clone [HTTPS clone URL]```: Copy the online repository to your local machine

```git log```: Displays all commits. return to prompt by typing ```:q```

```git pull```: Download changes from the online repository

```git push```: Load my local changes to the online repository

```git status```
shows the current statuses of all files.
A distinction is made between _modified_, _deleted_, _untracked files_ and _merge CONFLICT_.

* _modified_: I either want to accept the changes with ```git add [filename]``` or I want to cancel them with ```git stash```

* _deleted_: I either want to delete the file with ```git rm [filename]```, or I don't want to delete the file. In this case I run ```git checkout [filename] ```

* _untracked files_: files can either stay untracked and are therefore not included in the repository or I can delete the file using ```git rm [filename]``` or add it to the repository via ```git add [filename]```

* _merge CONFLICT_: open all listed files one after the other and search for the string _====_. Code above _====_ contains changes made by other repository members and code below _====_ contains your changes. After resolving conflicts commit your changes and push again.

```git commit -m "[commitmessage]"```: records changes to your local repository. Should immediately be visible in ```git log```
