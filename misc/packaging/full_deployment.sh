#!/bin/bash

# This script takes care of everything related to setting up the Echelon Planner
# in a working Linux distro with the 'apt' package manager
# It is separated into 3 sections:
#   1. Global Variable Declaration
#   2. Function Section
#   3. Main Function and final call to Main
#
# Installation of Echelon Planner (User must have root privileges)
# It is expected that the installation of the application be straightforward and modular with this script
# Therefore, the following are valid parameters:
#   "install"
#       "all": Default option, install latest stable build
#       "dependencies": Doesn't install EchelonPlanner, but merely it's dependencies
#       "nightly": Retrieve a latest image from the git repo and use that
#       "echelon": Doesn't worry about dependencies, just unpackages the application and configures it
#   "uninstall"
#       "": Removes the app only
#       "with-dependencies": Removes the app and all dependecies
#   "verify": checks that everything is where it's supposed to be and has been correctly written
#   "test": runs Django tests in the application. Useful for verifying features that were expected are working
#   "time-dilation": t h i n g s  w i l l  g o  v e  r  y  s  l    o    w   l   y.

#############################################################################################################
# Global Variables Section. Handle With Care

#############################################################################################################

#############################################################################################################
# Function Section
# If in PyCharm, do "Alt+7" or "Structure" to see this entire section quicker than scrolling down

checkArguments()
{ #Verify the arguments being taken into this function coincide with any of the expected
    echo "HI"

}

installDependencies()
{ #Do all the "apt-get installs" and "pip install" here
    echo "INSTALL"
}

configureDependencies()
{ #Write our custom config files over the default installs
    echo "Overwriting"
}

unpackageTar()
{ #Unpackage our App if we got it off the net.
    echo "Extracting App"
}

getDevelepmentSource()
{ #Retrieve the publicly available source
    echo "GITTING"

}

uninstallEchelon()
{ # Remove all possible traces of the echelon app
    echo "Uninstalling"

}

uninstallAllDependencies()
{ # Remove EVERYTHING
    echo "WAT!"

}

verifyDependecies()
{ # See that all needed packages exist
    echo "checking"
}

doEchelonTests()
{ # Make the program run the tests
    echo "testy!"
}

doTimeDilation()
{ #pull a fubar on the internal clock
    echo "Slowing down time"

}
start()
{ # Call the application to start. Analogous to main()
    checkArguments $1 $2
}

# Call the driving function and finish.
start $1 $2