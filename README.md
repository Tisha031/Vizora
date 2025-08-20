# Vizora
Vizora is a Django-based web application that provides automated Excel and CSV file processing, data analysis, and report generation capabilities.

# Core Functionality
1) File Upload & Processing
   
        Accepts Excel (.xlsx) and CSV files
   
        Automatically processes uploaded data using pandas
   
        Handles data cleaning (removes null values)
   
        Groups and aggregates data by the first column
   
3) Data Analysis & Visualization
   
        Generates bar charts using matplotlib
    
        Provides data summaries and insights

   
4) Report Export
   
        Exports processed data to CSV format & Excel format
   
        Maintains data integrity during export
5) Report History
   
       Tracks all uploaded files with timestamps
   
       Records processing status
   
       Provides access to historical reports

# Key Features

    User-friendly Interface: Clean, modern UI with Tailwind CSS styling
    
    Multi-format Support: Handles both Excel and CSV files
    
    Automatic Data Processing: Intelligent grouping and aggregation
    
    Visual Data Representation: Charts and tables for better data understanding
    
    Export Capabilities: Multiple output formats for flexibility
    
    Audit Trail: Complete history of all processed files

# Technical Architecture
    Backend: Django 5.2.3 with Python
    
    Database: SQLite (with Django ORM)
    
    Data Processing: Pandas for data manipulation and analysis
    
    Visualization: Matplotlib for chart generation
    
    Frontend: HTML templates with Tailwind CSS for modern UI
    
    File Handling: OpenPyXL for Excel file operations
