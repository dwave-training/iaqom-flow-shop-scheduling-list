[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-flow-shop-scheduling-list?quickstart=1)
  
# Flow Shop Scheduling with the Stride<sup>TM</sup> Hybrid Solver using a List Variable

For the flow shop scheduling problem, convert the mathematical formulation into a model in Python. Use a list variable to represent the decision variable, and formulate the problem so that it is compatible for submission to the Stride hybrid solver.

The objective is to minimize the makespan, which is the period starting with the first job on the first machine and ending with the completion of the last job on the last machine. The decision variable represents the order in which the jobs are scheduled. 

This problem has the following 4 constraints:
- All jobs process on machines in the same order.
- Every job must be processed on every machine. 
- Each machine can only process one job at a time.
- Once a job starts, it cannot be paused and must be completed.

Build the nonlinear model, add the constants to the model, define the decision variable, and set the objective function. Then submit the problem to the Stride hybrid solver to obtain the best solution.

In this exercise, the processing time for 3 jobs on 2 machines are provided as a `2x3` array. The total number of machines and jobs are also provided.

## Exercise

Build a nonlinear model that minimizes the makespan. Formulate the problem so that it is compatible for submission to the Stride Hybrid solver, and then submit the model to the solver to obtain the best solution.

Open the code file `fss_list_submit.py`.

   1. Create a nonlinear model object called `model` and import the required package.

   2. Add the problem constant to the model object.
      - Add `processing_times_matrix` to the model object and name it `processing_times`.
   
   3. Define the decision variable as a list symbol that represents the order in which the jobs are scheduled and store it in `S`. 

   4. Build the objective expression for the makespan. Loop over the machines using the index `machine_m` and over the positions in the job sequence using the index `k`. For each machine and job position, complete the following steps: 
      - Define the processing time of the current job on the current machine and store it in `process_time`.
      ```math
      process\_time = processtime_{machine\_m,S[k]} 
      ```
      - Define the completion time of the current job on the current machine and store it in `completion_time`.

         - For the first job on the first machine:

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

            Define the completion time of the current job. The job cannot start until the following conditions are satisfied: the current job has finished processing on the previous machine and the previous job has finished processing on the current machine. Take the later of these two completion times and add the processing time of the current job.

            Hint: Import the `maximum` function from `dwave.optimization.mathematical` module.

            ```math
            completiontime_{m,S[k]} = max(completiontime_{m-1,S[k]} + completiontime_{m,S[k-1]}) + processtime_{m,S[k]}
            ```
      - After calculating the `completion_time` for the current job, append it to the list in `end_times` associated with `machine_m`. 

   5. After exiting both loops, define the makespan as the completion time of the last job on the last machine and store it in `makespan`.

   6. Set the objective function to minimize the `makespan`. 
   
   7. Lock the model explicitly to prevent further changes.

   8. Instantiate the nonlinear sampler and name it `sampler`.
   
   9. Submit the nonlinear model to the Stride hybrid solver. Give this problem a label on your Leap dashboard by using the `label` parameter. Use the label `FSS_List`. Note that this label is case sensitive and uses an underscore.

   10. Return the best solution for the list variable symbol and store it in `order_state`.

   11. Return the objective value of the best solution and store it in `objective_value`.