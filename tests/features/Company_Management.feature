Feature: Company_Management
  As a user, I want to manage companies in the real estate app
  so that I can organize properties under their respective owners.

  Background:
    Given the user is in the companies page

  Scenario: Listing existing companies
    Then the following companies are listed:
      | Acme Real Estate     | Real Estate   | contact@acmereal.com   |
      | Sunrise Builders     | Construction | info@sunrisebuild.com  |
      | Blue Horizon Brokers | Broker       | support@bluehorizon.co |

  Scenario: Successfully create a new company with all fields
    When the user clicks on + Create Company
    And the user enters 'Innovate Real Estate' as Company Name
    And the user selects 'Real Estate' as Company Type
    And the user enters 'contact@innovatere.com' as Email
    And the user clicks on Create Company
    Then the user is in the companies page
    And the following companies are listed:
      | Innovate Real Estate | Real Estate | contact@innovatere.com |