"""
Requirements:
    Objective: Minimize the makespan.
    Constraints:
        - All jobs process on machines in the same order.
        - Every job must be processed on every machine.
        - Each machine can only process one job at a time.
        - Once a job starts, it cannot be paused and must be completed.
Given constants:
    processing_times_matrix (array): A 2x3 array representing the processing times of 3 jobs on 2 machines.
    num_machines (int): Number of machines.
    num_jobs (int): Number of jobs.
"""

# TODO: Import any required packages.
import numpy as np



#TODO: Initialize the nonlinear model object called `model`.


# Define the constants.
# Processing times matrix (for 3 jobs on 2 machines).
processing_times_matrix = np.array([[10, 5, 7], [20, 10, 15]])

# The total number of machines and jobs.
num_machines, num_jobs = processing_times_matrix.shape

#TODO: Add the problem constant to the model object.
# Hint: Add `processing_times_matrix` to the model object and name it `processing_times`


#TODO: Define the decision variable as a list variable and store it in `S`.


# Build the logic required for the objective: Minimize the makespan.

# Create an empty end times list
end_times = []

# Looping over the machines:
for machine_m in range(num_machines):

    # Each row stores the completion times for `machine_m`
    end_times.append([])

    # Looping over the jobs:
    for k in range(num_jobs):
        #TODO: Define the processing time of the current job on the current machine and store it in `process_time`.
        

        # For the first machine:
        if machine_m == 0:
            # For the first job on the first machine:
            if k == 0:
                #TODO: Set the completion time of the current job equal to its processing time and store it in `completion_time`.
                

            # For all the remaining jobs on the first machine:
            else:
                #TODO: Set the completion time of the current job equal to the completion time of the previous
                # job on the same machine plus the processing time of the current job and store it in `completion_time`.
                

        #TODO: For the remaining machines after the first one:    
        
            #TODO: For the first job on the remaining machines:
            
                #TODO: Set the completion time of the current job equal to the completion time of the same job
                # on the previous machine plus its processing on the current machine and store it in `completion_time`.
                

            #TODO: For the remaining jobs on the remaining machines:
            
                #TODO: Define the completion time of the current job. The job cannot start until the following conditions
                # are satisfied: the current job has finished processing on the previous machine and the previous job has finished on the current machine.
                # Add the processing time to the later of these two completion times and store the result in `completion_time`.
                # Hint: Import the `maximum` function from `dwave.optimization.mathematical` module.
                

        #TODO: Store the completion time in the list for the current machine.
        

#TODO: Define the makespan (the time at which the last job finishes processing on the last machine) and store it in `makespan`.


#TODO: Set the objective function: Minimize the `makespan`.


#TODO: Lock the model explicitly to prevent changes.


#TODO: Instantiate the nonlinear sampler and name it `sampler`.


#TODO: Submit the nonlinear model to the Stride hybrid solver. Use the label "FSS_List", which is case sensitive and uses an underscore.


# Process and print solution
print("\nSubmit the flow shop scheduling problem to the Stride hybrid solver using a list variable\n")
"""Read in the solution returned using `.state(0)` and display the solution."""

#TODO: Return the best solution for the list variable symbol and store it in `order_state`.


#TODO: Return the objective value of the best solution and store it in `objective_value`.


# Print the best solution
print(f"For state {0}, order={order_state} results in the objective value of {objective_value}")
