# Learning Project
Personal Project made to learn.

Developers:

- [Luís Rafael Sena](https://github.com/ifuaslaerl)
- []()

To add docker, follow this commands:

```console
git clone git@github.com:ifuaslaerl/LearningProject.git
cd LearningProject
docker build -t dev-container .
docker run -it --name dev-container -v $(pwd):/workspace dev-container
```

Attach to container in /workspace

```console
conda env create -f env.yml
conda init
source ../opt/miniconda/bin/activate
conda activate PYTHON
git config --global --ad safe.directory /workspace
```

Recomended to download this extentions in VsCode:

- GitLens — Git supercharged
- gitignore
- Path Intellisense
- Prettier - Code formatter
- indent-rainbow
- Python
- isort
- Pylint
- autoDocstring - Python Docstring Generator
- C/C++
- C/C++ Extension Pack
- C/C++ Runner
- Rainbow CSV
