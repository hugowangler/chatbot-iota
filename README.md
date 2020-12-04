# D7046E - Project - Chatbot Iota
One part of the course D7046E Neural Networks and Learning Machines at LTU.

## Setup
Create a conda environment from the YAML file by running

```
conda env create -f chatbot.yml
```

To activate the newly created environment run

```
conda activate chatbot
```

## Usage
### CLI
To start the CLI do the following

- make sure the conda environment is activated
- `cd` in to the project directory
- run `python src/cli/cli.py`

the CLI should now be running and you should start getting prompted about different subjects.


## Development
### Adding new dependencies to the conda environment
Whenever a new dependency is needed in the project the conda enviornment file `chatbot.yml` has to be updated. This can be done (after you have installed the depencency yourself) by running
```
conda env export > chatbot.yml
```

### Updating your local conda environment
To update your own conda environment after new dependencies has been added run
```
conda env update --f chatbot.yml
```
