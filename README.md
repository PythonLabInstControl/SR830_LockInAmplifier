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
* Follow [this link](https://github.com/PythonLabInstControl/SR830_LockInAmplifier/blob/master/GPIB-USB-HS_Configuration_Manual_Linux.pdf) to the GPIB-USB-HS_Configuration_Manual_Linux.pdf and click the button "Raw" for downloading

* Follow the instructions in this pdf-File

#####Windows:
* coming soon...

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
