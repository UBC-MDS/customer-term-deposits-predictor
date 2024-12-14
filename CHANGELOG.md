# CHANGELOG

This document outlines the improvements made to the project based on feedback received, including references to specific evidence such as commits, pull requests, or lines of code. Each section includes narration to help identify how the changes address the feedback.

---

## Feedback Summary

### 1. Update README File
**Feedback Description:**  
No link was provided in the README file to the analysis results.

**Changes Made:**  
Updated the README file to include a link to the analysis HTML file hosted on GitHub Pages:  
[https://ubc-mds.github.io/customer-term-deposits-predictor/analysis/customer-term-deposits-predictor.html](https://ubc-mds.github.io/customer-term-deposits-predictor/analysis/customer-term-deposits-predictor.html).  
Changed the GitHub Pages settings to "root" to directly specify the HTML file in the analysis folder.

**Evidence:**  
- **Commit Message:** [Link added](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/54bd749420578e68e0895d2d7a14037ceabb23d3#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5)

---

### 2. Delete `doc` Folder
**Feedback Description:**  
The `doc` folder was unnecessary after updating GitHub Pages to serve from the "root."

**Changes Made:**  
Deleted the `doc` folder from the repository.

**Evidence:**  
- **Commit Message:** [Removed the doc folder](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/54bd749420578e68e0895d2d7a14037ceabb23d3)

---

### 3. Update License File
**Feedback Description:**  
No Creative Commons License was specified for the project report, as noted in the Milestone 1 feedback.

**Changes Made:**  
Added a Creative Commons License to the project repository. Followed an example license from Tiffany's GitHub repository.

**Evidence:**  
- **Commit Message:** [Link to commit updating license](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/84c1048184c11ff7f5c084b89f6d3e33cb0917ae)

---

### 4. Address Data Leakage in EDA
**Feedback Description:**  
Milestone 1 feedback highlighted a violation of the "golden rule" by performing EDA before splitting the dataset, potentially causing data leakage.

**Changes Made:**  
Refactored the workflow to ensure EDA is performed only on the training dataset after the data split.

**Evidence:**  
- **Commit Message:** [Refactored EDA to prevent data leakage](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/d71cc1993e3edaa7fd324956cb3fc4b33fb06a01)

---

### 5. Add Code of Conduct
**Feedback Description:**  
The email address under the "Enforcement" section of the Code of Conduct should be tied to the team.

**Changes Made:**  
Updated the Code of Conduct to include a team email under the "Enforcement" section.

**Evidence:**  
- **Commit Message:** [Add Code of Conduct](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/54bd749420578e68e0895d2d7a14037ceabb23d3#diff-ffdbe3a1e7ee93cacfc080b6c635ccf3a8f6b0f00f2fb884f78c6b5f9dac8fd2)

---

### 6. Fix `download_customer_data.py` Script
**Feedback Description:**  
The script attribute naming convention in `download_customer_data.py` was not descriptive enough. Attribute names only listed different paths, which lacked clarity. Milestone 1 feedback suggested improving the naming of attributes passed to the script with more descriptive names.

**Changes Made:**  
Updated the `download_customer_data.py` script to include clear and descriptive path names for attributes. Added detailed documentation to the script for better usability and clarity.

**Evidence:**  
- **Commit Message:** [Improved attribute naming and added documentation](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/fa8277624052bf961079ae27e1818e323ca72932)  

---

### 7. Fix Environment Configuration
**Feedback Description:**  
1. **Pinned package versions missing:** Almost none of the packages in `environment.yml` were pinned with specific versions.  
2. **Platform-specific lockfile:** The lockfile was created for `osx-arm64` and wasn't compatible with other platforms.

**Changes Made:**  
- Added version pinning to all packages in `environment.yml` to ensure consistent environments across different setups.  
- Updated the lockfile to support multiple platforms (e.g., Linux, Windows, and macOS).  

**Evidence:**  
- **Commit Message:** [Pinned package versions and updated lockfile](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/d3b461f162439fc1aaae14b7b5921ccf8effa1c5)

---

### 8. Categorize `bank-full.csv` into Processed or Raw Folder
**Feedback Description:**  
The file `bank-full.csv` was standalone and not categorized into either the `processed` or `raw` folder.

**Changes Made:**  
Moved `bank-full.csv` into the `raw` folder, as it represents raw input data.

**Evidence:**  
- **Commit Message:** [Moved bank-full.csv](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/af40dd843cbc4677f906d29194a12fabf263551a)

---

### 8. Add function docstring
**Feedback Description:**  
Adding docstrings for each function would make the code easier to understand and use.

**Evidence:**
- **src folder link:** [link to src folder with all functions and their docstrings](https://github.com/UBC-MDS/customer-term-deposits-predictor/tree/main/src) 

---

### 9. Error handling
**Feedback Description:**
Consider adding checks for common issues in scripts, such as missing input files or directories.

**Changes Made:**
This was completed as part of the Milestone 4 requirements. Tests were added to a tests file for all functions.

**Evidence:**
- **test folder link:** [link to test folder](https://github.com/UBC-MDS/customer-term-deposits-predictor/tree/main/tests)

---

### 10. Validation script
**Feedback Description:**
README instructions doesn't run validate.py. A person who is trying to reproduce this analysis should run the same validation to ensure input data is correct.

**Changes Made:**
The validation script was changed into a function and incorporated into the preprocessed script for better code flow

**Evidence:**
- **Commit message:** [Validate function called in preprocessed script](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/fbf47bdc8eb4c30a280f12f786d278fdf930ae10)

---

### 11. Quarto Render issues in Docker
**Feedback Description:**
Wasn't able to render to report using the container environment.

**Changes Made:**
The README file was updated to provide more specific details to run the environment in the docker container.

**Evidence:**
- **Commit message:** [README file instructions updated](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/85170d44971649c322cb430dadbc5749abd369a3#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5)

---

## Summary of Improvements

1. Updated README file with a direct link to the analysis results.
2. Deleted unnecessary `doc` folder after configuring GitHub Pages to serve from the "root."
3. Added a Creative Commons License to the repository.
4. Addressed data leakage by performing EDA only on training data post-split.
5. Updated the Code of Conduct to include a team email under the "Enforcement" section.
6. Improved the `download_customer_data.py` script by making attribute names more descriptive and adding documentation.
7. Fixed environment configuration by pinning package versions and creating a platform-compatible lockfile.
8. Categorized `bank-full.csv` into the `raw` folder and updated scripts and documentation accordingly.

---

## Additional Notes

If any feedback was partially addressed or pending, please indicate the status and next steps here.