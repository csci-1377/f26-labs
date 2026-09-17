# Lab 1: Modeling Pointing Time

This lab uses **Jupyter Notebook** for interactive coding and exploration.  
You will run everything **locally** on your machine.

## 1. Install `uv`

We will use [`uv`](https://github.com/astral-sh/uv) to install and run Python tools for this assignment.

### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```
irm https://astral.sh/uv/install.ps1 | iex
```

## 2. Launch Jupyter Notebook
From the root of the repository, run:
```bash
uv run --locked jupyter notebook lab1-student.ipynb
```
A browser window should open automatically- this is where you will be working.
If it doesn’t pop up, copy the URL printed in the terminal into your browser.


## 3. Troubleshooting

If `uv` reports a workspace error involving a parent directory, and this lab
should run independently, add the lab folder to `exclude` in the parent
workspace's `pyproject.toml`:

```toml
[tool.uv.workspace]
exclude = ["path/to/lab1"]
```

Use the path relative to the parent `pyproject.toml`. Keep existing workspace
settings and append to any existing `exclude` list. Then rerun the launch
command from the lab folder.
