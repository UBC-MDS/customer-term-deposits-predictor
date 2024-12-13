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
- **Commit Message:** [Link to commit updating license](#)

---

### 4. Address Data Leakage in EDA
**Feedback Description:**  
Milestone 1 feedback highlighted a violation of the "golden rule" by performing EDA before splitting the dataset, potentially causing data leakage.

**Changes Made:**  
Refactored the workflow to ensure EDA is performed only on the training dataset after the data split.

**Evidence:**  
- **Commit Message:** [Refactored EDA to prevent data leakage](https://github.com/your-username/your-repository/commit/commit-hash)

---

### 5. Add Code of Conduct
**Feedback Description:**  
The email address under the "Enforcement" section of the Code of Conduct should be tied to the team.

**Changes Made:**  
Updated the Code of Conduct to include a team email under the "Enforcement" section.

**Evidence:**  
- **Commit Message:** [Add Code of Conduct](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/3f7673399b4a743e368c79830bf890664c9d409c)

---

### 6. Fix `download_customer_data.py` Script
**Feedback Description:**  
The script attribute naming convention in `download_customer_data.py` was not descriptive enough. Attribute names only listed different paths, which lacked clarity. Milestone 1 feedback suggested improving the naming of attributes passed to the script with more descriptive names.

**Changes Made:**  
Updated the `download_customer_data.py` script to include clear and descriptive path names for attributes. Added detailed documentation to the script for better usability and clarity.

**Evidence:**  
- **Commit Message:** [Improved attribute naming and added documentation](https://github.com/UBC-MDS/customer-term-deposits-predictor/commit/fa8277624052bf961079ae27e1818e323ca72932)  

---

## Summary of Improvements

1. Updated README file with a direct link to the analysis results.
2. Deleted unnecessary `doc` folder after configuring GitHub Pages to serve from the "root."
3. Added a Creative Commons License to the repository.
4. Addressed data leakage by performing EDA only on training data post-split.
5. Updated the Code of Conduct to include a team email under the "Enforcement" section.
6. Improved the `download_customer_data.py` script by making attribute names more descriptive and adding documentation.

---

## Additional Notes

If any feedback was partially addressed or pending, please indicate the status and next steps here.