# sqlnewstracker

## description
This python3 program provides a report of a news database on a linux terminal.

## instructions

### install required software

1. If you haven't already, download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) platform package
2. If you haven't already, download and install [Vagrant](https://www.vagrantup.com/downloads.html)
3. Clone this repo
4. Open `fsnd-virtual-machine.zip`
5. Open `newsdata.zip`

### set up vagrant environment

1. Navigate to `/vagrant` directory in the terminal. (should be in the /fsnd-virtual-machine/ directory that was created when you opened fsnd-virtual-machine.zip)
2. Type `vagrant up` in the terminal to install virtual linux system (this may take a while).
3. Once installation is finished run `vagrant ssh` from your terminal to begin virtual linux session.

### load news database

1. Copy/move `newsdata.sql` to `/vagrant`
2. From the terminal window/tab that is connected to vagrant (the one that you ran `vagrant ssh` in) change into the `/vagrant` directory by running `cd /vagrant`
3. Load the database by running `psql -d news -f newsdata.sql`

### run news log analysis

1. Copy/move `newsapp.py` to `/vagrant`
2. From the terminal window/tab that is connected to vagrant change into the `/vagrant` directory
3. Run the analysis with `psql -d news -f newsdata.sql`
