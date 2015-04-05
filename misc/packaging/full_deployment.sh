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
	#   "test": runs Django tests in the application. Useful for verifying features that were expected are working

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
				unpackageApp
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
				unpackageApp
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

		echo "Install tools"
		apt-get $install_args p7zip-full
		apt-get $install_args git
		
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
		
		pip install django
		pip install --allow-all-external mysql-connector-python
		pip install django-enumfield
		pip install mod_wsgi
		mod_wsgi-express install-module
	}

	unpackageApp()
	{ #Unpackage our App if we got it off the net.
		echo "Extracting App"
		echo "you will be asked to enter the Development Key of the Application as the password"
		7z x ProjectEchelonFull.7z
		mkdir -v /var/www/src
		echo "Copying base files into Deployment Directory"
		cp -rv src /var/www/src
		
	}
	
	configureDependencies()
	{ #Write our custom config files over the default installs
		configureSQL
		configureApache
		# For Apache http://askubuntu.com/questions/569550/assertionerror-using-apache2-and-libapache2-mod-wsgi-py3-on-ubuntu-14-04-python
	}

	configureApache()
	{
	#1st Part, enable WSGI
		echo "Configuring Apache"
		a2enmod wsgi
		# Write te wsgi.load
		echo "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi-py34.cpython-34m.so" >> /etc/apache2/mods-available/wsgi.load
		
		# Write wsgi.conf
		echo "<IfModule mod_wsgi.c>" > /etc/apache2/mods-available/wsgi.conf
		echo "WSGIPythonHome /usr" >> /etc/apache2/mods-available/wsgi.conf
		# Put other optimizations here
		
		# First Restart
		service apache2 restart
		
	#2nd Part, Enable SSL
		mkdir -v /etc/apache2/ssl
		# Copy the certificates
		cp -v apache.key /etc/apache2/ssl/apache.key
		cp -v apache.crt /etc/apache2/ssl/apache.crt
		
		a2ensite enable ssl
		a2ensite default-ssl
		
		# Second Restart
		service apache2 restart
		
	#3rd Part, Finish putting up the site
		echo "Overwriting Deafult Apache files"
		# Copy over the apache config files
		cp -v 000-default.conf /etc/apache2/sites-enabled/000-default.conf
		cp -v default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf
	}

	configureSQL()
	{ # Make the SQL database comply to our needs without heavily modifying it
		# To transmit the SQL password, it can be hashed first in a MySQL shell using 'SELECT PASSWORD("[SomeStringHere]")'
		echo "Configuring local MySQL instance. You will have to input your ROOT password several times"
		echo "Password will not be echoed"
		mysql -u root -p -e "create user 'eve'@'localhost' identified by PASSWORD '*EC1C5005C380E9E2B4E50EE8749AC9AA4EA96F15'"
		mysql -u root -p -e "create database echelon;"
		# Read in the database image that has been packaged
		mysql -u root -p < echelon_db_backup.sql
		
		echo "MySQL has been configured."
	}

	getDevelepmentSource()
	{ #Retrieve the publicly available source
		echo "GITTING"

	}

	doEchelonTests()
	{ # Make the program run the tests
		# FYI: the way to run unit tests is to go to EchelonPlanner/src/ and do "python manage.py test"
		echo "Running tests on echelon. These will fail if the app was not installed correctly or was changed in the process"
		python3 /var/www/src/manage.py test
	}
	
	start()
	{ # Call the application to start. Analogous to main()
		### START OF EXECUTION ###
		# Check if Root
		if [[ $EUID -ne 0 ]]
		then
			echo "Must be root to install Echelon Planner" 2>&1
			echo "Exiting."
			exit 1
		else				
			# First, check if it's Ubuntu 14.04. This might 
			lsb_release -a
			echo "This script may not complete correctly if Release < 14.04"
			# Hand it over.
			checkArguments $1 $2
		fi
	}

	# Call the driving function and finish.
	start $1 $2