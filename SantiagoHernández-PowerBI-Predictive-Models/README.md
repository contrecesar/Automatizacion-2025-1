# Predictive Models in Power BI: Python and R Integration Examples

This repository contains example scripts in **Python** and **R** that demonstrate how to integrate advanced predictive modeling capabilities directly within **Microsoft Power BI Desktop** via the **Power Query Editor**. These examples complement Section "IV. Beyond Dashboards: Predictive Models, Cloud Data & Advanced Power BI Techniques" of our university article.

## Repository Contents

* `sales_forecast_python.py`: A Python script that implements a simple linear regression model to forecast sales based on advertising spend. Designed to be executed in Power Query Editor.

* `sales_forecast_R.R`: An R script that implements the same simple linear regression model for sales forecasting. Also designed to be executed in Power Query Editor.

## Prerequisites

To run these scripts with Power BI Desktop, you'll need the following:

1. **Microsoft Power BI Desktop:** Ensure you have the latest version installed.

2. **Python Installation:**

   * A Python 3.x installation on your system.

   * The `pandas` and `scikit-learn` libraries installed. You can install them via pip:

     ```bash
     pip install pandas scikit-learn
     ```

3. **R Installation:**

   * An R installation on your system.

   * The `dplyr` and `caret` libraries installed. You can install them in your R console:

     ```R
     install.packages(c("dplyr", "caret"))
     ```

4. **Power BI Desktop Configuration:**

   * In Power BI Desktop, go to `File > Options and settings > Options`.

   * In the `Global` section, select `Python scripting` (or `R scripting`).

   * Ensure Power BI detects your Python/R installation and that the path is correct.

## Test Data (Structure)

Both scripts expect a data table with the following minimum structure in Power BI:

| **Column** | **Data Type** | **Description** |
| :--------- | :------------ | :-------------- |
| `Date` | Date | The date of the sales observation. |
| `Sales` | Numeric | The actual sales for that date. |
| `Advertising_Spend` | Numeric | The advertising spend for that date (predictor variable). |

## How to Use the Scripts with Power BI Desktop

Follow these steps to integrate and run the scripts in your Power BI reports:

1. **Load Data into Power BI Desktop:**

   * Open Power BI Desktop.

   * Click `Get data` and load your historical sales data table (ensuring it has the `Date`, `Sales`, and `Advertising_Spend` columns). You can use a CSV file, a database, etc.

2. **Open Power Query Editor:**

   * Once the data is loaded in Power BI, click `Transform data` on the `Home` tab to open the Power Query Editor.

   * Select the table containing your sales data.

3. **Run the Script (Python or R):**

   * In the `Transform` tab of Power Query Editor, click `Run Python script` or `Run R script` (depending on which script you want to use).

   * A script window will open. Copy and paste the entire content of `sales_forecast_python.py` or `sales_forecast_R.R` into this window.

   * Click `OK`.

   * Power Query will execute the script, passing your data table as a `DataFrame` (Python) or `data.frame` (R) named `dataset`. The script will process the data, generate predictions, and return a table named `output_table`.

4. **Load Results into Power BI Model:**

   * After the script executes, you'll see a new table in Power Query Editor (usually named `output_table` or similar). Click `Table` next to the table name to expand it if necessary.

   * Click `Close & Apply` on the `Home` tab of Power Query Editor.

   * The table with the predicted sales (`Predicted_Sales`) will be loaded into your Power BI data model, ready for use in your reports and visualizations.
