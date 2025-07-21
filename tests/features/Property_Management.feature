Feature: Property_Management
  As a user, I want to manage properties in the real estate app
  so that I can track all assets associated with companies.

  Background:
    Given the user is in the Properies Page

  Scenario: Listing existing properties
    Then the following properties are listed:
      | Ocean View Apartment | 123 Beach Ave   | $250000.00 | 120 sqm | Acme Real Estate |
      | Downtown Loft        | 456 City Center | $320000.00 | 95 sqm  | Acme Real Estate |
      | Modern Duplex        | 333 Oak Lane    | $370000.00 | 140 sqm | Sunrise Builders |

  Scenario: Successfully create a new property linked to a company
    When the user clicks on +Create Property
    And the user enters 'Ocean View Villa' as Property Name
    And the user enters '123 Seaside Ave' as Address
    And the user enters '1500000' as Price
    And the user enters '200 sqm' as Size
    And the user selects 'Sunrise Builders' as Company
    And the user clicks on Create Property
    Then the user is in the Properies Page
    Then the following properties are listed:
      | Ocean View Villa | 123 Seaside Ave | $1500000.00 | 200 sqm | Sunrise Builders |

  Scenario: Attempt to create a property with required fields left blank
    When the user clicks on +Create Property
    And the user enters ' ' as Property Name
    And the user enters ' ' as Address
    And the user enters ' ' as Price
    And the user enters '200 sqm' as Size
    And the user clicks on Create Property
    Then the user remains in the Create Property Page
    And the user clicks on Back to List button
    And the following properties are not listed
      |  |  | 200 sqm |  |
