Feature: Property_Management
  As a user, I want to manage properties in the real estate app
  so that I can track all assets associated with companies.

  Background:
    Given the user is in the properties page

  Scenario: Listing existing properties
    Then the following properties are listed:
      | Ocean View Apartment | 123 Beach Ave   | $250000.00 | 120 sqm | Acme Real Estate |
      | Downtown Loft        | 456 City Center | $320000.00 | 95 sqm  | Acme Real Estate |
      | Modern Duplex        | 333 Oak Lane    | $370000.00 | 140 sqm | Sunrise Builders |


