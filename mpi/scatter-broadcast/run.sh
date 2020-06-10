mpirun -np 9 python3 scatter.py
echo ""
mpirun -np 5 python3 gather.py
echo ""
mpirun -np 5 python3 reduce.py
echo ""
mpirun -np 5 python3 allreduce.py
echo ""
mpirun -np 5 python3 alltoall.py
