# dchecker2

A tool to perform scheduled data integrity check on VIVO's researcher's database.

## Installation

We recommend you run dchecker from a virtual environment in order to prevent
conflicts with other packages. This assumes you have git version control
installed on your system.

DChecker uses Python 3. Verify that you have Python 3 installed with this
command:

```sh
    python --version
```

Next, clone the dchecker repository, create a virtual environment, and install
dchecker into that virtual environment.

```sh
    git clone https://github.com/ctsit/dchecker2.git
    cd dchecker2
    python3 -m venv .env
    source .env/bin/activate
    pip install --editable .
```

## Configuration

Parameters for running the script are set in plaintext cfg files located in the
config directory. You need to provide:

+ A mail server to send the report
+ A from address to send the report from
+ A to address to recieve the report
+ A SPARQL endpoint URL

You can also specify the following optional parameters:

+ A path to the folder containing the queries
+ A subject for the report

## Running

The command to run dchecker using a configuration file is:

  ```sh
      dchecker2 debug.cfg
  ```

## Adding new queries

Queries are run sequentially out of the `queries` subdirectory. To add a new
query, save it in a `.rq` file and it will be run automatically when the
program is started.
