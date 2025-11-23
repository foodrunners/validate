# Validate Repository Overview

You asked: *"What is this tool? Can I tweak it?"*

## 1. What is this tool?
The `validate` repository is a full-stack **Web Application** designed to check "Industry Foundation Classes" (IFC) files—the standard format for BIM data.

Think of it as a **Quality Control Platform** for building models.

### Core Functionality
1.  **Upload**: Users upload `.ifc` files via a Web UI or API.
2.  **Process**: The system runs a series of checks (Syntax, Schema, and "Gherkin" rules).
3.  **Report**: It generates a detailed report showing which parts of the model passed or failed.

### Architecture (The "Stack")
It is built with standard, popular web technologies:
*   **Backend (The Brain)**: Written in **Python** using the **Django** framework. This handles the database, API, and file processing.
*   **Frontend (The Face)**: Written in **JavaScript** using **React**. This is the website you see in the browser.
*   **Worker (The Muscle)**: Uses **Celery** to process large files in the background so the website doesn't freeze.
*   **Validation Engine**: Uses **IfcOpenShell** (a powerful Python library) to read IFC files and **Gherkin** (a language for writing human-readable rules) to validate them.

## 2. Can you tweak it?
**Yes, absolutely.** Since you have the source code, you can modify every aspect of it. Here are the common ways you might want to tweak it:

### A. Tweak the Rules (The most common use case)
The tool validates files based on "rules". You can add your own!
*   **Location**: `backend/apps/ifc_validation/checks/ifc_gherkin_rules/`
*   **How**: You write "Feature files" in plain English (e.g., "Every Wall must have a FireRating") and then write a small snippet of Python code to check that rule.
*   **Why**: To enforce your specific company standards or project requirements.

### B. Tweak the Backend Logic
*   **Location**: `backend/apps/ifc_validation/`
*   **How**: Modify the Python code in Django.
*   **Why**: To change how files are stored, add new API endpoints, or integrate with other systems (like sending an email when validation fails).

### C. Tweak the UI
*   **Location**: `frontend/`
*   **How**: Modify the React components.
*   **Why**: To change the branding (logo, colors), simplify the dashboard, or show different data in the reports.

## 3. Summary
You don't *have* to build a separate app on top of it. You can treat this repository as your **base product** and customize it to fit your needs.

*   **If you want a custom dashboard**: Modify the `frontend`.
*   **If you want custom checks**: Add rules to the `backend`.
*   **If you want to automate it**: Use the API (as we explored briefly).
