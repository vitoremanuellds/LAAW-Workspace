# Feedbacks and new changes

- Make the tasks (tasks with and without subtasks) have the same structure:
  - All the task must now be a folder with the format being: t{ID}-{task-name}/
  - The md file for the task now must not be named the same as the folder, it must be named 'task.md'.
  - The format will now be for a task:
```
t{id}-{task-name}/
  task.md # The actual file that describe the task
  t{id}-{task-name}/ # One subtask for the task. This is only valid if the task has a subtask.
  ...
```
  - Convert the tasks of .ai to this format.
- The description of the define task is broken, it complains about the "{}" and the ":".
- There are some other files on context/ that is not following the id pattern, verify if these files are necessary, if yes convert the files for the new context format, if not, delete them.
- Add instructions to the skills to always use the generate id script to generate any id, including the ones in the subtasks table.
- Files from the LAAW repo must contain a Table of Content after the title of the md file. The ones generated using the workflow as well. The only ones that does not need it are the ones that has only one section.
- All of the changes I'm saying here is to be done in the LAAW repo, not the .ai folder, with exception of the conversions and the contexts problems I asked. Any change to a skill or the workflow files must be done inside the LAAW repo and later propagated to the LAAW-Workspace using the sync tools.
