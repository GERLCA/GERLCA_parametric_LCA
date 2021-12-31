# GERLCA_parametric_LCA
Python codes for performing life cycle assessment (LCA) scenario analyses, sensitivity analyses, and Monte Carlo analyses, using systems of equations and variable input parameters

## Parametric LCA description

Parametric LCA aims to maintain the relationships between different parameters along the life cycle of a system or product, modeling the system with variables and equations that depict these interconnections. This practice also accommodates for sensitivity analysis and Monte Carlo analysis while minimizing the likelihood of modeling impossible cases, as interdependent parameters change in value automatically when a parameter is varied.

## Input parameters

Input parameters are the variables that are independently set in the LCA model and that do not themselves depend on other parameter values.

These codes work with an input parameter text file, saved with a .txt extension and set up with comma-delimited columns and a header. The columns should contain, in this order:
>Parameter name, Minimum value, Baseline value, Maximum value

For Monte Carlo analysis, the input parameter text file should have an additional "column" for the probability distribution type:
>Parameter name, Minimum value, Baseline value, Maximum value, Probability distribution type

Additionally, the values shown may need to be changed from their true minimum and maximum values, depending on the probability distribution type (please see Monte Carlo analysis code directions below for more details).

There should be zero empty lines in the parameter text file, including at the very end, or the code will show an error.

### How to set up a line in the input parameter text file for Monte Carlo analysis, by distribution type:

**Uniform distribution:** 
>Parameter name, Minimum value, Baseline value, Maximum value,**uniform**

**Normal distribution:** 
>Parameter name, Minimum value, Baseline value, Baseline + 2 standard deviations,**normal**

**Lognormal distribution:** 
>Parameter name, Minimum value, Location, Scale,**lognormal**

The lognormal distribution needs a location and scale to be defined.

**Triangular distribution:**
>Parameter name, Minimum value, Baseline value, Maximum value,**triangular**

**Weibull distriution:**
>Parameter name, Minimum value, Scale or alpha value, Shape or beta value,**Weibull**

**Distribution from a weighed dataset:**
>Parameter name, Minimum value, Baseline value, Maximum value,**weighed**

This needs an external text file for the dataset of weighed probabilities for the input parameter, named exactly like the name of the parameter and saved to the same folder as the input parameter text file. There should be no spaces and no header in this text file.
Two "columns" are separated by commas, with the possible value for the parameter first, followed by the probability of that value occurring second.

**Distribution informed from raw data:**
>Parameter name, Minimum value, Baseline value, Maximum value,**rawdata**

This will only pick values from your raw dataset and nothing in between values.
This needs an external text file for the dataset of possible values for the input parameter, named exactly like the name of the parameter and saved to the same folder as the input parameter text file. There should be no spaces and no header in this text file.

It is recommended that, for Monte Carlo analysis, the impact values from characterized life cycle inventories (LCIs) be removed from the equations and that individual "rawdata" text files be created for the possible impact values of each LCI, which can be extracted from running an uncertainty analysis on a unit process LCI in SimaPro.

## LCA model (system of equations)

For the codes to run, equations must be developed and added to the codes themselves where indicated with comments.

These equations include:
-Equations that describe the relationships between independent parameters and additional parameters that can be calculated from the independent and/or other parameters
-Equations that set steady values, such as conversion factors and impacts from characterized life cycle inventories
-Equations that determine the impacts by process along the life cycle and that sum up to the total impact scaled to the functional unit ("Process_" equations)

The system of equations requires the values for characterized impacts from relevant life cycle inventories (LCIs), which can be exported from other softwares like SimaPro and Gabi. The codes are designed to handle and provide results for one impact category at a time. Thus, the system of equations should include LCI impacts for one impact category only.

Each equation starting with "Process_" is recognized by the codes to contribute to the sum total of the life cycle impact of the studied system. No "Process_" equation should duplicate or include other "Process_" impacts in order to avoid double-counting impacts. All "Process_" equations should be scaled to the functional unit and based on the relevant indicator units for the target impact category (for example, kg CO2eq/functional unit).

## Results

The results of each run are saved as a text file in the same folder that the input parameter text file is saved.

The results of the **baseline LCA scenario analysis** will show the impact by "Process_" equation and the total impact.

The results of the **sensitivity analysis** will show:
>Parameter name, total LCA result when the parameter is changed to its minimum value, baseline LCA scenario analysis result, total LCA result when the parameter is changed to its maximum value

The results of the **Monte Carlo analysis** will show a column of total LCA results (one on each line) for the number of simulations requested.

The results of the **Monte Carlo analysis with parameter values by simulation** will show a header labeling each comma-delimited "column." The first column shows the total LCA result of the simulation (one simulation per line), followed by the value of each parameter used in that simulation. This can help identify the combination of parameter values that led to outliers or extreme values in order to inform either revised iterations of the LCA model or recommendations to the audience for the LCA.

## License

Licensed under GNU General Public License v3.0: "Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights." 

Please cite this GitHub package when using it in a study for publication.

## Questions

Please read the comments at the top of each code and the comments within the codes for additional notes on how to proceed appropriately with the analyses.

Please email mfortier2@ucmerced.edu if you have questions about the codes, notice an issue that we should patch up, or have a request for an update or modification of the codes.
