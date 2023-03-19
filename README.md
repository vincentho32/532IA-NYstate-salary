# 532IA-NYstate-salary

## Motivation and purpose

The purpose of this dashboard is to provide users insights and information needed to succeed in their careers. Specifically, users can visualize data related to job numbers and salaries in different industries and geographic regions. By analyzing the data, hopefully user can make informed decisions about their career paths, negotiate better salaries, and achieve their professional goals.

For more details, please click this link to [my proposal](https://github.com/vincentho32/532IA-NYstate-salary/blob/main/proposal.md)


## Usage section

The dashboard features a box plot that displays numerical data, such as employment numbers and wages across different areas. Additionally, there is a histogram that illustrates the distribution of various columns in the dataset. Users can choose which data they wish to visualize by selecting options from the respective dropdown menu.


## Installation


To install `NYstate-salary` locally, you can:

1. To replicate the analysis, first clone this GitHub repository. Then, install nb_conda_kernels in your base environment. Now, install the dependencies listed in the nystatewage.yaml file below as an Anaconda environment, using:

```{r}
conda install -c conda-forge nb_conda_kernels
conda env create -f nystatewage.yaml
conda activate nystatewage
```

2. Then run this command in src/ folder:

```{r}
python app.py
```
3. Copy the address and paste it to the browser to visualize the dashboard page.


## Dataset Reference

The dataset is from [Data.gov](https://catalog.data.gov/dataset/occupational-employment-statistics)


## Contributing

Feedback and suggestions are always welcome! 

Please read [the contributing guidelines](https://github.com/vincentho32/532IA-NYstate-salary/blob/main/CONTRIBUTING.md)
to get started.
## Code of conduct

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation. Detailed descriptions
of these points can be found in [`CODE_OF_CONDUCT.md`](https://github.com/vincentho32/532IA-NYstate-salary/blob/main/CODE_OF_CONDUCT.md).

## License
The NYstate-salary Dashboard is licensed under the terms of the MIT license.
