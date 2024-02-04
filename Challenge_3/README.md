**Web Log Analysis**

**Overview**

This repository contains a Python script (filter_logs.py) designed to assist in the analysis of a web log file from a large ecommerce website. The primary goal of the script is to filter out all the requests with a status code of 200, potentially revealing patterns associated with a suspected ongoing system attack. Additionally, the observations and analysis findings have been documented in the analysis.txt file.

**Files**
filter_logs.py: Python script that filters out all requests with a status code of 200 and writes the remaining requests to a dynamically created output file.
analysis.txt: Text file containing observations and analysis findings based on the examination of the web log file.

**Usage**
1. Ensure you have Python installed on your system.
2. Run the filter_logs.py script by providing the path to the input log file and the desired output directory.
        python filter_logs.py path/to/your/input.log path/to/your/output_directory
3. Check the generated output file for non-200 requests.

**Observations and Recommendations**
The analysis findings and top three recommendations for strengthening the website are detailed in the analysis.txt file. Please review the file to gain insights into potential issues and suggested improvements.
