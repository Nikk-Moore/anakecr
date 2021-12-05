import sys, os
import argparse
import re
from .kernelcreator import CreateKernel

COMMAND_HELP = '''
Input command to be run. Please choose from the following options:
create - create a new jupyter kernel
'''

# Create to command line utility parser
parser = argparse.ArgumentParser(prog="anakecr", description="A utility to automate some jupyter tasks utilising the Anaconda(c) distribution")
parser.version = "0.0.1"
parser.add_argument('cmd', metavar='cmd', type=str, help=COMMAND_HELP)
parser.add_argument("-n", "--name", metavar="name", type=str, help="The ipykernel name")
parser.add_argument("-d", "--display", type=str, help="The Display name")
parser.add_argument("-c", "--conda", type=str, help="The path to the anaconda python directory")
parser.add_argument("-r", "--requirements", type=str, help="The path to a requirments file")
parser.add_argument("-p", "--package", type=str, help="Install a specific package")


args = parser.parse_args()

def create_kernel(conda_home):
    if args.name == None:
        sys.exit("Create requires an ipykernel name (-n)")
    if args.display == None:
        args.display = args.name
        #sys.exit("Create requires a display name (-d)")
        new_kernel = CreateKernel(name=args.name, display=args.display, condaexec=conda_home)
        new_kernel.create()

def install_packages(conda_home):
    if args.package != None:
        kernel = CreateKernel(name=args.name, display=args.display, condaexec=conda_home, requirement_file='')
    elif args.requirements != None:
        kernel = CreateKernel(name=args.name, display=args.display, condaexec=conda_home, requirement_file='')
    else:
        sys.exit("Need to pass a package name (-p) or requirements file (-r)")

def main():
    if args.conda == None:
        try:
            path = re.split(":", os.getenv("PATH"))
            anacondas = [s for s in path if os.path.join("conda", 'bin') in s]
            conda_home = str(anacondas[0])
        except:
            sys.exit("Unable to determine conda path, please pass using -c option")
    if args.cmd == "create":
        create_kernel(conda_home)
    elif args.cmd == "install":
        install_packages(conda_home)
    else:
        sys.exit("No command entered...\nPlease use -h for help")

if __name__=='__main__':
    main()    