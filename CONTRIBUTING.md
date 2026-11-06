# Contributing

Corrections, clearer explanations and new recipes are welcome.

## Report an error or suggest a topic

Open an [issue](https://github.com/retomarek/edap/issues/new/choose): the forms ask for the book page, what went wrong or what you would like to see. Questions go to [Q&A](https://github.com/retomarek/edap/discussions/categories/q-a). Bugs in a pyedautils function itself belong to [pyedautils](https://github.com/retomarek/pyedautils/issues/new/choose).

## Change the book

1. Fork the repository, clone it and create a branch.
2. Install the dependencies and build the book locally, as described under *Local development* in the [README](README.md):

   ```bash
   pip install -r requirements.txt
   jupyter-book build edap
   ```

3. Edit the Markdown pages and notebooks in `edap/`. Recipes in Part III follow the same layout: Goal, Data Basis, Data Preparation, Visualization and an optional Customization dropdown. Load data from a URL or from the data bundled with pyedautils, and commit notebooks without outputs (the book executes them).
4. New pages go into `edap/_toc.yml`, new packages into `requirements.txt`.
5. Check that the build runs without errors and without new warnings, then open a pull request.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CONDUCT.md). By contributing to this project you agree to abide by its terms.
