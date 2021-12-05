# anakecr
A small command line utility to easily add, remove and modify anaconda environments and kernels

I made this for my own use as I kept finding I had to look up the commands and it took multiple (albeit small) steps to do this.

This is currently built and working in linux and very early - not ready yet for actual useage. It is a pet project in early development.

<hr>

## Installation

Clone the repository using the git clone command
In the base directory run the command:

<i>python -m build</i>

<p>This will create a directory called dist which will contain a .whl file which can be installed by pip.</p>
<p>Then run:</p>

<i>pip install dist/anakecr-0.0.1-py3-none-any.whl</i>

<hr>

## Setup

<p>Yet to implement</p>
<p>anakecr set-conda <b>< path to anaconda bin directory ></b> </p>

<hr>

## Usage

anakecr create \<options\>
  - Creates and installs a new kernel into the base jupyter anaconda environment
