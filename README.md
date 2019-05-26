# MPLS-Network-Automation
This repository is a catch-all for the Python scripts and select router configuration files needed to create GNS3 MPLS networks for my Master's thesis. This is only a small portion of the various iterations of an MPLS simulated work that precedded the actual network automation via the Python scripts showcased in this repositiory. Note that this automation is specific to GNS3 and that the Mininet automation files are **not** included here.
## Instalation Instructions

### Download Files
The necesary files can be [downloaded here](https://github.com/nortorious-flame89/MPLS-Network-Automation.git). 

### Additional installations & Running the scripts
-Other things this project requires is Python 3.x which can be [downloaded here](https://www.python.org/download/releases/3.0/). 
  * Be sure to scroll down to the download tab of the webpage.
  
-Unzip the files installed in the **download** section and save them all under the same directory. 

-GNS3 stands for **Graphical Network Simulator 3** and, for Windows users, must be downloaded in a VM environment. GNS3 academy recommends **VMWare vSphere.** Please refer to [this link](https://docs.gns3.com/1Bn-s1Izkjp13HxcPF4b8QSGfkWJYG_dpMt9U1DQjvZ4/) for documentation on how to install and run GNS3 in a VM. Linux users (*Ubuntu in particular*) can run GNS3 natively. The following terminal commands will do the trick for Ubuntu 18.04. 
  * `sudo apt-get update`
  * `sudo apt-get upgrade` 
  * `sudo add-apt-repository ppa:gns3/ppa`
  * `sudo apt-get install gns3-gui`

-Open and run the python files in your IDE of choice. If you'd like to install Atom, use the following terminal command:  
  * `sudo apt-get update`
  * `sudo add-apt-repository ppa:webupd8team/atom`
  * `sudo apt-get install atom`
  
-To build up the GNS3 network images of routers, switches and automation containers must **legally** downloaded. David Bombal is an excellent educator that shows how to download those images. In particular, a linux automation container must be obtained in order to run the scripts directly using **Nano**, a popluar linux editor. Instructions for learning how to create nano files are in this [YouTube video](https://www.youtube.com/watch?v=gyKiDczLIZ4).

## License
This repository is provided under the MIT License. If you would like to read what that entails, please refer to the [license](https://github.com/nortorious-flame89/MPLS-Network-Automation/blob/master/LICENSE) page in this repository.
