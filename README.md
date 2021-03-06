# MPLS-Network-Automation
This repository is a catch-all for the Python scripts and select router configuration files needed to create GNS3 MPLS networks completed for my graduate thesis. It is only a snapshot of the various configurations for the simulated network devices that preceded the final simulated networks. This repository showcases the Python scripts used for network automation. Note that they are specific to GNS3 and that the Mininet automation scripts are **not** included here.
## Installation Instructions

### Download Necessary Files
The necessary files are all included in the repository. 

### Additional Installations 
Other things this project requires is Python 3.x which can be [downloaded here](https://www.python.org/download/releases/3.0/). 
  * Be sure to scroll down to the download tab.
  
Unzip the files installed in the **download** section and save them all under the same directory. 

GNS3 stands for **Graphical Network Simulator 3** and, for Windows users, must be downloaded in a VM environment. GNS3 academy recommends **VMWare vSphere.** Please refer to [this link](https://docs.gns3.com/1Bn-s1Izkjp13HxcPF4b8QSGfkWJYG_dpMt9U1DQjvZ4/) for documentation on how to install and run GNS3 in a VM. Linux users (*Ubuntu in particular*) can run GNS3 natively. The following terminal commands will do the trick for Ubuntu 18.04. 
  * `sudo apt-get update`
  * `sudo apt-get upgrade` 
  * `sudo add-apt-repository ppa:gns3/ppa`
  * `sudo apt-get install gns3-gui`

Open and run the python files in your text editor (or IDE) of choice. If you'd like to install Atom, use the following terminal command:  
  * `sudo apt-get update`
  * `sudo add-apt-repository ppa:webupd8team/atom`
  * `sudo apt-get install atom`

## Populating GNS3 Network & Running the Scripts
To populate the GNS3 MPLS network, images of routers, switches and automation containers, must be **legally** downloaded. David Bombal is an excellent educator that shows how to download those images [here](https://www.youtube.com/watch?v=oEP5eXftWJI). In particular, a Linux automation container must be obtained in order to run the scripts directly using **Nano**, a popluar Linux editor. Instructions for learning how to create Nano files are in this [YouTube video](https://www.youtube.com/watch?v=gyKiDczLIZ4).

## License
This repository is provided under the MIT License. If you would like to read what that entails, please refer to the [license](https://github.com/noor-fernandez/MPLS-Network-Automation/blob/master/LICENSE) page in this repository.
