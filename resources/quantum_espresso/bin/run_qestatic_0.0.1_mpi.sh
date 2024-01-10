#!/bin/bash
mpirun -np $1 pw.x -in input.pwi > output.pwo
