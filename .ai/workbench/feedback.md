- We need a new way of id-ing the phases, tasks and adrs, to avoid collision when working with concurrent teams, maybe add some sort of timestamp:
  - The id will have the following format:
    - Minutes elapsed since a custom epoch defined in the workflow in a contant file.
    - 4 random numbers.
    - The format of the phases, tasks and decicions name will be "{p/t/d}{id}-{name}" for the Phases, Tasks and Decisions (adrs).
    - The format of the id will be: {minutes-elapsed}{random-numbers}
  - Create a python script to generate 1 or N ids ordered. Only the ID will be returned, not the name for the phase, task or decision.

- When asking the model to create the phases.md file, it starts planning all the phases files.

- Tasks folder is becoming crowded too fast, maybe we could have folders with the phases names and inside it the tasks. It somehow conflicts with what we already decided before as to flat the task folder, but now I think that it is a good tradeoff:
  - Lets make the phases a folder with a phase.md (this will replace the phase file).
  - Inside this folder, there will be the phase.md file and the tasks files for that phase.
  - With this, the tasks folder will now have only orphan tasks.

- The agent is still trying to commit the ignored files. We need to be more enfatic in this.

- We need to make the agent create the task table when defining the phase, instead of waiting for the first task.
