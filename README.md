# GERLCA_parametric_LCA
Python codes for performing life cycle assessment (LCA) scenario analyses, sensitivity analyses, and Monte Carlo analyses, using systems of equations and variable input parameters

## Parametric LCA description

Parametric LCA aims to maintain the relationships between different parameters along the life cycle of a system or product, modeling the system with variables and equations that depict these interconnections. This practice also accommodates for sensitivity analysis and Monte Carlo analysis while minimizing the likelihood of modeling impossible cases, as interdependent parameters change in value automatically when a parameter is varied.

## Input parameters

Input parameters are the variables that are independently set in the LCA model and that do not themselves depend on other parameter values.

These codes work with an input parameter text file, saved with a .txt extension and set up with comma-delimited columns and a header. The columns should contain, in this order:
Parameter name, Minimum value, Baseline value, Maximum value

For Monte Carlo analysis, the input parameter text file should have an additional "column" for the probability distribution type:
Parameter name, Minimum value, Baseline value, Maximum value, Probability distribution type
Additionally, the values shown may need to be changed from their true minimum and maximum values, depending on the probability distribution type (please see Monte Carlo analysis code directions for more details).

There should be zero empty lines in the parameter text file, including at the very end, or the code will show an error.

## LCA model (system of equations)

For the codes to run, equations must be developed and added to the codes themselves where indicated with comments.

These equations include:
-Equations that describe the relationships between independent parameters and additional parameters that can be calculated from the independent and/or other parameters
-Equations that set steady values, such as conversion factors and impacts from characterized life cycle inventories
-Equations that determine the impacts by process along the life cycle and that sum up to the total impact scaled to the functional unit ("Process_" equations)

The system of equations requires the values for characterized impacts from relevant life cycle inventories (LCIs), which can be exported from other softwares like SimaPro and Gabi. The codes are designed to handle and provide results for one impact category at a time. Thus, the system of equations should include LCI impacts for one impact category only.

Each equation starting with "Process_" is recognized by the codes to contribute to the sum total of the life cycle impact of the studied system. No "Process_" equation should duplicate or include other "Process_" impacts in order to avoid double-counting impacts. All "Process_" equations should be scaled to the functional unit and based on the relevant indicator units for the target impact category (for example, kg CO2eq/functional unit).

## Questions

Please read the comments at the top of each code and the comments within the codes for additional notes on how to proceed appropriately with the analyses.

Please email mfortier2@ucmerced.edu if you have questions about the codes, notice an issue that we should patch up, or have a request for an update or modification of the codes.
