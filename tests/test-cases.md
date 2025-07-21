# Test Suite Description

This document outlines the automated test suite for the Leasey.AI QA Test application.

## Tools and Frameworks

The test suite is built using the following tools and frameworks:

* **Pytest:** As the test runner.
* **Pytest-BDD:** For implementing Behavior-Driven Development (BDD).
* **Selenium:** For browser automation and web element interaction.
* **WebDriver Manager:** To automatically manage the browser drivers.
* **AssertPy:** For fluent assertions.
* **Page Object Model (POM):** The tests are structured using the POM design pattern to enhance maintainability.

## Test Cases

The test suite covers the following scenarios:

### Company Management

* **AC-01:** List existing companies.
* **AC-02:** Successfully create a new company with all fields.
* **AC-03:** Attempt to create a company with an invalid email.
* **AC-04:** Successfully delete a company.
* **AC-05:** Successfully create and delete the same company.
* **AC-06:** Successfully create a company and its property.
* **AC-07:** Validate all properties are deleted when the company is deleted.

### Property Management

* **AP-01:** List existing properties.
* **AP-02:** Successfully create a new property linked to a company.
* **AP-03:** Attempt to create a property with required fields left blank.
* **AP-04:** Attempt to create a property with a negative price.
* **AP-05:** Successfully delete a property.
* **AP-06:** Successfully create and delete the same property.

## How to Run Tests

To run the automated tests, execute the following command from the root of the project:

```bash
make test
```

This will trigger the test suite and generate an HTML report named `report.html` in the root directory.

## Bug Report
Details about the defects can be found [here](https://github.com/JFPedra/qa-testing-page/blob/main/tests/defects-report.md)