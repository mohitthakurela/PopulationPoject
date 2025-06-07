# Country Population Analyzer 🌍

## Overview
This project fetches data about countries using the **RestCountries API** and processes it to determine population statistics. It outputs a ranked list of the top 5 most populous countries and saves the results to a CSV file.

## Features
- Retrieves country data including **name, capital, and population**.
- Sorts countries by population in descending order.
- Provides summary statistics (total countries, total population, average population).
- Saves the **top 5 most populous countries** to a CSV file.

## Dependencies
Ensure you have **Python 3.x** installed along with:
- `requests` (for making API calls)
- `csv` (for handling CSV output)

To install missing dependencies, run:
```bash
pip install requests
