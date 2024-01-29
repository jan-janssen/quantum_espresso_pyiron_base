# Quantum Espresso Wrapper with `pyiron_base`

Test it on: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jan-janssen/quantum_espresso_pyiron_base/jobflow?labpath=example.ipynb)

## Explanation 
* `espresso/pseudo/Al.pbe-n-kjpaw_psl.1.0.0.UPF` - This is the pseudo potential for qunatum espresso. By placing it in `~/espresso/pseudo`, it is automatically detected by quantum espresso.
* `environment.yml` - Conda environment to define the dependencies.
* `example.ipynb` - Jupyter notebook using `jobflow` 
* `adis_tools` - parser developed by Marnik Bercx @mbercx
