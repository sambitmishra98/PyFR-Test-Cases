#!/bin/bash

#SBATCH -J "s-2"
##SBATCH --exclusive
#SBATCH --cpus-per-gpu=1
#SBATCH --gpu-bind=closest
#SBATCH --use-min-nodes
#SBATCH --time=7-00:00:00
#SBATCH --output=i-1.out
#SBATCH --no-requeue

#SBATCH -p amd
#SBATCH --gres=gpu:3
#SBATCH --nodes=1
#SBATCH --ntasks=3
backend='hip'

meshf='/mnt/share/sambit98/REFERENCE_SIMULATIONS/github-pyfr-tests/PyFR-Test-Cases/paper-on-GPU-accelerated/TGV/p4/TGV_p3.pyfrm'

. /etc/profile.d/modules.sh
module purge
. ~/virtual-environments/my-pyfr/bin/activate

    export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
    export PATH=$HOME/.local/bin/:$PATH
    export LDPATH=$HOME/.local/lib/:$LDPATH
    export LDPATH=$HOME/.local/lib64/:$LDPATH
    export CPATH=$HOME/.local/include/:$CPATH
    export CPPATH=$HOME/.local/include/:$CPPATH
    export LD_LIBRARY_PATH=$HOME/.local/lib/:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=$HOME/.local/lib64/:$LD_LIBRARY_PATH
    export PKG_CONFIG_PATH=$HOME/.local/lib/pkgconfig:$PKG_CONFIG_PATH
    export PKG_CONFIG_PATH=$HOME/.local/lib64/pkgconfig:$PKG_CONFIG_PATH
    export PATH=/usr/local/cuda/bin/:$PATH

pyfr_runner="/home/grads/s/sambit98/github/my-pyfr/pyfr/pyfr"

numnodes=$SLURM_JOB_NUM_NODES
mpi_tasks_per_node=$(echo "$SLURM_TASKS_PER_NODE" | sed -e  's/^\([0-9][0-9]*\).*$/\1/')
np=$[${numnodes}*${mpi_tasks_per_node}]

python_runner="~/virtual-environments/my-pyfr/bin/python3"

echo "Running on master node: `hostname`"
echo "Time: `date`"
echo "Current directory: `pwd`"
echo -e "JobID: $SLURM_JOB_ID\n======"
echo -e "\nnumtasks=$SLURM_NTASKS, numnodes=$numnodes, mpi_tasks_per_node=$mpi_tasks_per_node (OMP_NUM_THREADS=$OMP_NUM_THREADS)"
echo "Time: `date`"

start="mpirun -n $np $python_runner $pyfr_runner"
CMD="time $start run -b $backend $meshf t-2.ini"; echo -e "\nExecuting command:\n==================\n$CMD\n"; eval $CMD 
echo -e "\nSimulation ends\n"
