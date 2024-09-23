Welcome to the DLG Enablement project! This project has examples for running experiments, using model registry and publishing models as APIs.


### Perform your first experiment

The `domino_experiments_example_workbook.ipynb` Jupyter notebook shows an example of how you can use the Experiments feature to train and compare models.

Run it inside the workspace, and then compare the runs in the Experiment tab.

![Jupyter](raw/latest/jupyter.svg?inline=true) ![R](raw/latest/r.svg?inline=true) ![VScode](raw/latest/vscode.svg?inline=true)

[![Run Notebook](raw/latest/run-notebook.svg)](/workspace/:ownerName/:projectName?showWorkspaceLauncher=True)

#### Example from the Experiments tab after running the `experiment.ipynb` notebook code

![Example Experiment Run Comparison](raw/latest/experiment-example-run-comparison.png)

---

### Publish a Model as an API
Domino models are REST API endpoints that run your Domino code. We’ve created a sample model for you. Check out these quick instructions and publish your sample model in no time!

[![Publish Model](raw/latest/publish-model.svg)](/models/getBasicInfo?name=Sample-model&file=model.py&function=my_model&projectId=:projectId)

Enter `model.py` or `model.R` in the file field. Enter `my_model` in the function field, and hit ‘Create Model’.

![How to start a Model!](raw/latest/how-to-start-a-model.png)

---

