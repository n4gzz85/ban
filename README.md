# Bandit Security Scan GitHub Action

## Overview

The Bandit Security Scan GitHub Action is designed to automate the process of checking for security vulnerabilities in Python code. It uses **Bandit**, a security linter for Python code, to identify potential vulnerabilities and block the merging of Pull Requests (PRs) if any high-severity vulnerabilities are detected.

This action runs on every pull request to ensure that new code does not introduce security risks. If a high-severity vulnerability is found, the PR is blocked, and a comment is posted. If no high-severity vulnerabilities are found, a success message is posted, and the PR is automatically merged.

Note: If the codebase already contains high-severity vulnerabilities and a pull request is submitted with new files, the scanner will evaluate all files in the PR. As a result, the merge may be blocked even if the new files do not contain high-severity vulnerabilities. We refer to "high" severity here, as Bandit does not use the "Critical" label for its findings. In Bandit, "high" represents the most severe vulnerabilities.

## Workflow Breakdown

The workflow consists of two main jobs:

### 1. Security Scan

- Installs and runs **Bandit** on the codebase.
- Checks for vulnerabilities with a focus on high-severity issues.
- Posts a comment and blocks the PR if any high vulnerabilities are found.

### 2. Auto Merge

- If the security scan job is successful (i.e., no high vulnerabilities are found), the PR is automatically merged.

## Workflow Triggers

The workflow is triggered by a **pull request** event. Specifically, it runs on every pull request made to the repository.

## Jobs

### Security Scan

This job is responsible for performing the security scan using **Bandit**. It:

- Installs Bandit and runs it on the codebase.
- Filters out vulnerabilities with a severity of "high."
- Posts a comment to block the PR if high vulnerabilities are found.

### Auto Merge

If the **Security Scan** job is successful (i.e., no high vulnerabilities are found), the PR is automatically merged. This step ensures that once the code is confirmed secure, it will be merged without further intervention.

## Permissions

The action defines specific permissions for the GitHub runner to ensure proper access levels for the necessary API calls:

- **pull-requests:** write
- **contents:** read
- **issues:** write

## Requirements

- The repository should be set up to support GitHub Actions.
- Ensure that the PR contains Python code that can be analyzed by Bandit.

## Conclusion

This GitHub Action automates the security scan process for Python code, ensuring that high-severity vulnerabilities are flagged and blocked before any code is merged into the repository. It adds an additional layer of security to your CI/CD pipeline by leveraging Bandit and GitHub Actions to enforce secure coding practices.
