# Quantum Espresso Wrapper with `pyiron_base`

Test it on: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jan-janssen/quantum_espresso_pyiron_base/resources?labpath=example.ipynb)

## Explanation 
* `quantum_espresso/job.py` - Job class for the quantum espresso simulation code based on the `pyiron_base.TemplateJob` class. 
* `quantum_espresso/__init__.py` - The job classes have to be stored in a python module. In this case the python module is named `quantum_espresso` just like the simulation code. 
* `resources/quantum_espresso/bin/run_qeminimize_0.0.1.sh` - The shell scripts to call the quantum espresso simulation code have to be stored in the `resource` directory in a subfolder named `quantum_espresso` just like the module the job class is defined in. 
* `resources/quantum_espresso/bin/run_qeminimize_0.0.1_mpi.sh` - `pyiron_base` internally uses shell scripts ending with `*_mpi.sh` to identify shell scripts for parallel execution.
* `resources/quantum_espresso/bin/run_qestatic_0.0.1.sh` - In analogy to the shell scripts for structure optimization also the shell scripts for static calculations are included in the resource directory. 
* `resources/quantum_espresso/bin/run_qestatic_0.0.1_mpi.sh` - Again the shell script for parallel execution is included as well. 
* `resources/quantum_espresso/potentials/Al.pbe-n-kjpaw_psl.1.0.0.UPF` - This is the pseudo potential for qunatum espresso. It is also stored in the resource directory in the subfolder `potentials`. 
* `.pyiron` - The location of the `resource` directory for `pyiron_base` can be defined in the pyiron configuration file, which is typically located in the users home directory. 
* `environment.yml` - Conda environment to define the dependencies.
* `example.ipynb` - Jupyter notebook which contains the workflow to calculate the bulk modulus. 
