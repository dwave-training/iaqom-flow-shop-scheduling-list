[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-flow-shop-scheduling-list?quickstart=1)
  
# Flow Shop Scheduling With The Stride<sup>TM</sup> Hybrid Solver Using A List Variable

For the flow shop scheduling problem, convert the mathematical formulation into a model in Python. Use a list variable to represent the decision variable, and formulate the problem so that it is compatible for submission to the Stride hybrid solver.

The objective is to minimize the makespan, which is the period starting with the start time of the first job on the first machine and ending with the completion time of the last job on the last machine. The decision variable represents the order in which the jobs are scheduled. 

This problem has the following constraints:
- All jobs must be processed on all machines in the same order.
- Every job must be processed on every machine. 
- Each machine can only process one job at a time.
- Once a job starts, it cannot be paused and must be completed.

Build the nonlinear model, add the constants to the model, define the decision variable, and set the objective function. Then submit the problem to the Stride hybrid solver to obtain the best solution.

In this exercise, the processing time for 3 jobs on 2 machines are provided as a `2x3` array. The total number of machines and jobs are also provided.

## Exercise

Build a nonlinear model that minimizes the makespan. Formulate the problem so that it is compatible for submission to the Stride Hybrid solver, and then submit the model to the solver to obtain the best solution.

In `fss_list_submit.py`, do the following:

   1. Import the relevant package(s).

   2. Create a nonlinear model object called `model`.

   3. Add the problem constant to the model object by adding `processing_times_matrix` to the model object and naming it `processing_times`.
   
   4. Define the decision variable as a list symbol that represents the order in which the jobs are scheduled and store it in `S`. 

   5. Build the logic required for the objective expression for the makespan by looping over both the machines using the index `machine_m` and the positions in the job sequence using the index `k`. That is, for each machine and job position, do the following:
      - Define the processing time of the current job on the current machine and store it in `process_time`.
      ```math
      process\_time = processtime_{machine\_m,S[k]} 
      ```
      - Define the completion time of the current job on the current machine and store it in `completion_time` as follows:

         - For the first job on the first machine, set the completion time of the current job equal to its processing time as follows:

            Set the completion time of the current job equal to its processing time.
            ```math
            completiontime_{0,S[0]} = processtime_{0,S[0]}
            ```
         - For all the remaining jobs on the first machine:

            Set the completion time of the current job equal to the completion time of the previous job on the same machine plus the processing time of the current job. 
            ```math
            completiontime_{0,S[k]} = completiontime_{0,S[k-1]} + processtime_{0,S[k]}
            ```
         - For the first job on the remaining machines:

            Set the completion time of the current job equal to the completion time of the same job on the previous machine plus its processing time on the current machine.
            ```math
            completiontime_{m,S[0]} = completiontime_{m-1,S[0]} + processtime_{m,S[0]}
            ```
         - For all the remaining jobs on the remaining machines:

            Define the completion time of the current job. Because the job cannot start until the current job has finished processing on the previous machine and the previous job has finished processing on the current machine, you must take the later of these two completion times and add the processing time of the current job.

            Hint: Import the `maximum` function from the `dwave.optimization.mathematical` module.

            ```math
            completiontime_{m,S[k]} = max(completiontime_{m-1,S[k]} + completiontime_{m,S[k-1]}) + processtime_{m,S[k]}
            ```
      - After calculating the `completion_time` for the current job, append it to the list in `end_times` associated with `machine_m`. 

   6. After exiting both loops, define the makespan as the completion time of the last job on the last machine and store it in `makespan`.

   7. Set the objective function to minimize `makespan`. 
   
   8. Lock the model explicitly to prevent further changes.

   9. Instantiate the nonlinear sampler and name it `sampler`.
   
   10. Submit the nonlinear model to the Stride hybrid solver. Label your problem “FSS_List" using the `label` parameter. Note that this label is case-sensitive and uses an underscore. When you submit your problem, this label will display in your Leap dashboard.

   11. Return the best solution for the list variable symbol and store it in `order_state`.

   12. Return the best solution's objective value and store it in `objective_value`.