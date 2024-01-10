from pyiron_base import JOB_CLASS_DICT


JOB_CLASS_DICT.update(
    {
	"QEMinimize": "quantum_espresso.job",
	"QEStatic": "quantum_espresso.job",
    }
)
