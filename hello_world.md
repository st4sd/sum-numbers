# Hello world example

This is the most basic workflow definition.

## Hello world workflow definition using the FlowIR format in YAML

```yaml
components: # Contains a list of component definitions
- name: hi  # A component definition is just a multi-level dictionary
  command:
    executable: echo
    arguments: hello world
```

Here, we define a workflow which contains just 1 component that has 2 top-level keys a `name` and a `command` definition. The `command` is just an `executable` and its `arguments`. ST4SD supports grouping components in stages by specifying the component top-level key `stage` (integer). Components with no `stage` key are automatically inserted to stage 0. Here's the same workflow but using an explicit stage index:

```yaml
components:
- name: hi
  stage: 0
  command:
    executable: echo
    arguments: hello world
```

In both examples, the full name of the component is `stage0.hi`. We refer to the full name of a component as the `reference` of the component. You can find more information about workflow definitions and the FlowIR schema in the [README.MD](README.md) file.

>**Note**: _You may also skip the `command.arguments` field of a component altogether. The component will just invoke its executable with no arguments._

>**Note**: _For more information on FlowIR visit our [FlowIR documentation website](https://st4sd.github.io/overview/workflow-specification)._

## Executing the hello world example

This section assumes that you've already installed [st4sd-runtime-core](https://github.com/st4ssd/st4sd-runtime-core). If you've installed `st4sd-runtime-core` in a virtual environment take a moment to load it before continuing.

First, let's create a package for our workflow definition. Workflow packages, in their most basic form, simply contain the workflow definition. But they can also contain binary and data files. For this hello-world example, we'll just create a workflow package with just the workflow definition file.

```bash
cd /tmp
mkdir /tmp/hello-world /tmp/hello-world/conf
cat >/tmp/hello-world/conf/flowir_package.yaml <<EOF
components:
- name: hi
  command:
    executable: echo
    arguments: hello world
EOF
```

>**Note**: _If the `mkdir` commands fail, that means that the `/tmp/hello-world` folder already exists. Try deleting that folder and then rerunning the commands above._

Invoke the `elaunch.py` script of ST4SD to execute the workflow. 

```bash
elaunch.py --nostamp hello-world
# Wait for it to terminate and then view the list of files associated with `hi`
ls -lth hello-world.instance/stages/stage0/hi
# Now look at its stdout
cat hello-world.instance/stages/stage0/hi/out.stdout
```

>**Note**: _If the `elaunch.py` script fails it will also print an error message in its stderr. Given the simplicity of this hello-world workflow, an error likely means that you've already run hello-world before with the `--nostamp` argument. If that's the case, simply delete `/tmp/hello-world.instance` and re-run `elaunch.py`._

>**Note 2**: _The `--nostamp` argument instructs the workflow scheduler to not prefix the name of the workflow instance directory that it generates with a timestamp. This just makes it easier for this guide to tell you where files are. In practice you'd want to include timestamps in your workflow instance directory names._

The `elaunch.py` script will print out a summary of the execution right before it terminates. Expect to see a text similar to the one below in your terminal:

```
INFO      MainThread                     root                          : <module>             2021-02-12 11:42:13,074: Clean-up - Final status was
cost=0
current-stage=stage0
exit-status=Success
experiment-state=finished
stage-progress=1.0
stage-state=finished
stages=['stage0']
total-progress=1.0
updated=2021-02-12 11:42:13.073179
```

The `elaunch.py` script will create the `/tmp/hello-world.instance` folder. If you like, you can take a moment to poke around the folder structure that `elaunch.py` generated. The files associated with your very first `hi` component are stored under `/tmp/hello-world.instance/stages/stage0/hi`.

See the [sum numbers readme file](README.md) for a more advanced, but still toy, workflow description.
