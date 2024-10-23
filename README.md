# MultiQC GC Content Calculator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Description

The **MultiQC GC Content Calculator** is a Python script designed to parse HTML reports generated by the MultiQC package. It extracts and calculates the average GC (Guanine-Cytosine) content from a specific table in the report. This tool is particularly useful for bioinformaticians and researchers analyzing genomic data from sequencing experiments.

## Features

- Parses HTML reports generated by MultiQC using BeautifulSoup.
- Calculates the average GC content from a specified table in the report.

## Installation

To use this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/a-lamloum/MultiQC-GC-Content-Average-Calculator.git
cd MultiQC-GC-Content-Average-Calculator
```

## Usage 
Run the script from the command line, providing the path to the MultiQC HTML report as an argument:
```
python script.py <html_file>.html
```

## Example 
```
python script.py multiqc_report.html
```
