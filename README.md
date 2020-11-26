# D7046E - Project - Chatbot Iota
One part of the course D7046E Neural Networks and Learning Machines at LTU.

## Setup
Create a conda environment from the YAML file by running

```bash
conda env create -f chatbot.yml
```

To activate the newly created environment run

```bash
conda activate chatbot
```

## Development
### Adding new dependencies to the conda environment
Whenever a new dependency is needed in the project the conda enviornment file `chatbot.yml` has to be updated. This can be done (after you have installed the depencency yourself) by running
```bash
conda env export > chatbot.yml
```

### Updating your local conda environment
To update your own conda environment after new dependencies has been added run
```bash
conda env update --f chatbot.yml
```
