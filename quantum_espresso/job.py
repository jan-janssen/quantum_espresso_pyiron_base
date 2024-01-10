import os
import shutil
from ase.calculators.espresso import Espresso
from ase.io import write
from pwtools import io
from pyiron_base.jobs.job.template import TemplateJob
from pyiron_base import state


def copy_potentials(structure):
    element_lst = list(set(structure.get_chemical_symbols()))
    pot_dict = {}
    for path in state.settings.resource_paths:
        qe_path = os.path.join(path, "quantum_espresso", "potentials")
        for file in os.listdir(qe_path):
            element = file.split(".")[0]
            if element in element_lst and element not in pot_dict.keys():
                pot_dict[element] = os.path.join(qe_path, file)
    for pot_file in pot_dict.values():
        shutil.copyfile(pot_file, os.path.join(job_qe_minimize.working_directory, os.path.basename(pot_file)))


def write_input_calc_minimize(input_dict, working_directory="."):
    filename = os.path.join(working_directory, 'input.pwi')
    os.makedirs(working_directory, exist_ok=True)
    input_data_relax = {
        'calculation': 'vc-relax',
        'cell_dofree': 'ibrav',
    }
    write(
        filename=filename, 
        images=input_dict["structure"], 
        Crystal=True, 
        kpts=input_dict["kpts"], 
        input_data=input_data_relax, 
        pseudopotentials=input_dict["pseudopotentials"],
        tstress=True, 
        tprnfor=True
    )
    copy_potentials(structure=input_dict["structure"])


def write_input_calc_static(input_dict, working_directory="."):
    filename = os.path.join(working_directory, 'input.pwi')
    os.makedirs(working_directory, exist_ok=True)
    input_data_static = {
        'calculation': 'scf', # A string describing the task to be performed.
    }
    write(
        filename=filename, 
        images=input_dict["structure"], 
        Crystal=True, 
        kpts=input_dict["kpts"], 
        input_data=input_data_static, 
        pseudopotentials=input_dict["pseudopotentials"],
        tstress=True, 
        tprnfor=True
    )
    copy_potentials(structure=input_dict["structure"])


def collect_output_calc_minimize(working_directory="."):
    filename = os.path.join(working_directory, 'output.pwo')
    return {"structure": io.read_pw_md(filename)[-1].get_ase_atoms()}


def collect_output_calc_static(working_directory="."):
    filename = os.path.join(working_directory, 'output.pwo')
    out = io.read_pw_scf(filename)
    return {
        "energy": out.etot,
        "volume": out.volume,
    }


class QEMinimize(TemplateJob):
    def __init__(self, project, job_name):
        super().__init__(project, job_name)
        self.input.update({  # Default Parameter 
            "structure": None, 
            "pseudopotentials": {"Al": "Al.pbe-n-kjpaw_psl.1.0.0.UPF"}, 
            "kpts": (3, 3, 3),
        })

    def write_input(self):
        write_input_calc_minimize(input_dict=self.input.to_builtin(), working_directory=self.working_directory)

    def collect_output(self):
        self.output.update(collect_output_calc_minimize(working_directory=self.working_directory))
        self.to_hdf()


class QEStatic(TemplateJob):
    def __init__(self, project, job_name):
        super().__init__(project, job_name)
        self.input.update({  # Default Parameter 
            "structure": None, 
            "pseudopotentials": {"Al": "Al.pbe-n-kjpaw_psl.1.0.0.UPF"}, 
            "kpts": (3, 3, 3),
        })

    def write_input(self):
        write_input_calc_static(input_dict=self.input.to_builtin(), working_directory=self.working_directory)

    def collect_output(self):
        self.output.update(collect_output_calc_static(working_directory=self.working_directory))
        self.to_hdf()
