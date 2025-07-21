Feature: Company_Management
  As a user, I want to manage companies in the real estate app
  so that I can organize properties under their respective owners.

  Background:
    Given the user is in the companies page

  Scenario: Listing existing companies
    Then the following companies are listed:
      | Acme Real Estate     | Real Estate  | contact@acmereal.com   |
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

  Scenario: Attempt to create a company with an invalid email
    When the user clicks on + Create Company
    And the user enters 'Innovate Real Estate' as Company Name
    And the user selects 'Real Estate' as Company Type
    And the user enters 'no email' as Email
    And the user clicks on Create Company
    Then the user remains in the Create Company Page
    And the user clicks on Back to List button
    And the following companies are not listed
      | Innovate Real Estate | Real Estate | no email |

  Scenario: Successfully delete a company
    When the user clicks on delete the company 'Acme Real Estate'
    Then company successfully deleted alert is displayed
    And the following companies are not listed
      | Acme Real Estate | Real Estate | contact@acmereal.com |

  Scenario: Successfully create and delete the same company
    When the user clicks on + Create Company
    And the user enters 'Innovate Real Estate' as Company Name
    And the user selects 'Real Estate' as Company Type
    And the user enters 'contact@innovatere.com' as Email
    And the user clicks on Create Company
    Then the user is in the companies page
    And the user clicks on delete the company 'Innovate Real Estate'
    And company successfully deleted alert is displayed
    And the following companies are not listed
      | Innovate Real Estate | Real Estate | contact@innovatere.com |

  Scenario: Successfully create a company and its property
    When the user clicks on + Create Company
    * the user enters 'Prestige Properties' as Company Name
    * the user selects 'Broker' as Company Type
    * the user enters 'info@prestigep.com' as Email
    * the user clicks on Create Company
    * the user clicks on Properties
    * the user clicks on +Create Property
    * the user enters 'Ocean View Villa' as Property Name
    * the user enters '123 Seaside Ave' as Address
    * the user enters '1500000' as Price
    * the user enters '200 sqm' as Size
    * the user selects 'Prestige Properties' as Company
    * the user clicks on Create Property
    Then the user is in the Properies Page
    And the following properties are listed:
      | Ocean View Villa | 123 Seaside Ave | $1500000.00 | 200 sqm | Prestige Properties |
