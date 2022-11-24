# ST4SD Example: Sum numbers

Toy example demonstrating the most common features of our virtual experiment Domain Specific Language (DSL) `FlowIR`.
We recommend using this source code to follow along with our [sum numbers tutorial](https://st4sd.github.io/overview/tutorial/).

For more information on FlowIR visit our [FlowIR documentation website](https://st4sd.github.io/overview/workflow-specification/).

## Quick links

- [Getting started](#getting-started)
- [Development](#development)
- [Help and Support](#help-and-support)
- [Contributing](#contributing)
- [License](#license)

## Getting started

#### Python

Running and developing this project requires a recent Python version, it is suggested to use Python 3.7 or above. You
can find instructions on how to install Python on the [official website](https://www.python.org/downloads/).

#### Python module st4sd-runtime-core

Create a python 3.7+ and install the python module `st4sd-runtime-core` in it.
For more information, see the installation instructions of [st4sd-runtime-core](https://github.com/st4sd/st4sd-runtime-core).

#### Executing the example

Instructions below assume that your python 3.7 virtual environment is under `${HOME}/venvs/st4sd`

```bash
git clone http://github.com/st4sd/sum-numbers.git
source ${HOME}/venvs/st4sd/bin/activate

# Delete the previous runs if it exists
rm -rf sum-numbers.instance
elaunch.py sum-numbers --nostamp
```

After the virtual experiment terminates, you should have a look inside the `sum-numbers.instance` directory. 
For more information see our [sum-numbers tutorial](https://st4sd.github.io/overview/tutorial/).

## Development

Coming soon.

## Help and Support

Please feel free to reach out to one of the maintainers listed in the [MAINTAINERS.md](MAINTAINERS.md) page.

## Contributing 

We always welcome external contributions. Please see our [guidance](CONTRIBUTING.md) for details on how to do so.

## License

This project is licensed under the Apache 2.0 license. Please [see details here](LICENSE.md).
