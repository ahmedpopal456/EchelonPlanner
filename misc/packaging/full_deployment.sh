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
    #1st argument is $1
    # 1. Argument is empty
    if [[ -z $1 ]]
    then
        echo "No Arguments Found. Try typing \'help\' for argument list"
    fi

    ### 2. Install ###
    if [[ $1 == "install" ]]
    then
        #2.1 all
        if [[ $2 == "all" ]]
        then
            echo "Installing all parts of EchelonPlanner"
            installBaseDependencies
            unpackageTar
            configureDependencies
        fi
        #2.2 dependencies
        if [[ $2 == "dependencies" ]]
        then
            echo "Installing Dependencies Only"
            installBaseDependencies
            configureDependencies
        fi
        #2.3 nigthly
        if [[ $2 == "nightly" ]]
        then
            echo "VerifyingDependencies"
            #If you're doing a nightly installation, I'll assume you have all the necessary dependencies
            verifyDependencies
            getDevelepmentSource
            doEchelonTests
        fi
        #2.4 echelon
        if [[ $2 == "echelon" ]]
        then
            unpackageTar
            configureDependencies
        fi
    fi

    ### 3. Uninstall ###
    if [[ $1 == "uninstall" ]]
    then
        uninstallEchelon
        uninstallAllDependencies
        echo "Removing all"
    fi

    ### 4. Verify ###
    if [[ $1 == "verify" ]]
    then
        verifyDependencies
    fi

    ### 5. test ###
    if [[ $1 == "test" ]]
    then
        doEchelonTests
    fi

    # 6. time dilation
    if [[ $1 == "time-dilation" ]]
    then
        doTimeDilation
    fi

    echo "Deployment Script Complete."

}

installBaseDependencies()
{ #Do all the "apt-get installs" and "pip install" here
    checkApt = $(which apt-get)
    if [[ -z checkApt ]] # If we don't have apt-get, then exit
    then
        echo "Package Manager \'apt-get\' is not available in this system"
        echo "Aborting"
        exit
    fi

    install_args="install --assume-yes"

    echo "Installing Python3 and PIP"
    apt-get $install_args python3
    apt-get $install_args python3-pip

    echo "Installing MySQL Server"
    apt-get $install_args mysql-server mysql-client

    echo "Installing Apache Web Server"
    apt-get $install_args apache2

    echo "Installing Python PIP modules"
    installPythonDependencies

    echo "Dependency installation is complete"
}

installPythonDependencies()
{ #Install all PIPS!
    # According to each system then
    # for Debian, true_pip="pip-3.2"
    # for Ubuntu, true_pip="pip3"
    # for any other generic system, true_pip="python3 -m pip"

#    true_pip="pip-3.2"
#    echo "Checking installed PIP"
#    if [[ -z $(which $true_pip) ]]
#    then
#        true_pip="pip3"
#    fi
#    if [[ -z $(which $true_pip) ]]
#    then
#        # If all fails, default
#        true_pip="python3 -m pip"
#    fi
#
#    CHECK=$($true_pip help | grep cannot)
#    if [[ ! $CHECK == "" ]]
#    then
#        # String was not empty, so there WAS a problem. Advise and ABORT
#        echo "Could not successfully install PIP for Python 3"
#        echo "Dependencies NOT met. Aborting"
#        exit
#    fi
    python3 -m pip install virtualenv
    echo "Creating Virtual Env"
    mkdir /var/www/echelon
    python3 -m virtualenv /var/www/echelon/env



    true_pip="python3 -m pip"

    pip install django
    pip install --allow-all-external mysql-connector-python
    pip install django-enumfield
    pip install mod_wsgi
    mod_wsgi-express install-module
}

configureDependencies()
{ #Write our custom config files over the default installs
    echo "Overwriting"
    # For Apache http://askubuntu.com/questions/569550/assertionerror-using-apache2-and-libapache2-mod-wsgi-py3-on-ubuntu-14-04-python
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

verifyDependencies()
{ # See that all needed packages exist
    echo "checking"
}

doEchelonTests()
{ # Make the program run the tests
    # FYI: the way to run unit tests is to go to EchelonPlanner/src/ and do "python manage.py test"
    echo "testy!"
}

doTimeDilation()
{ #pull a fubar on the internal clock
    echo "Slowing down time"

}
start()
{ # Call the application to start. Analogous to main()
    #TODO: CHECK IF USER IS ROOT!
    checkArguments $1 $2
}

# Call the driving function and finish.
start $1 $2