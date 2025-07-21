# Defect Report

---

## Defect: Company Deletion - "Page Not Found" Error

* **ID:** DR-001
* **Date Reported:** 7/20/2025
* **Reported By:** JF
* **Module:** Company Management
* **Severity:** High (Application crash, core functionality failing)
* **Priority:** High
* **Status:** Open

### Description

When a user attempts to delete a company that has just been created, the application crashes and displays a "Page Not Found" error. This prevents the successful deletion of companies, impacting essential data management functionality.
### Steps to Reproduce

1. **Given** the user is in the companies page
2. **When** the user clicks on + Create Company
3. **And** the user enters 'Innovate Real Estate' as Company Name
4. **And** the user selects 'Real Estate' as Company Type
5. **And** the user enters 'contact@innovatere.com' as Email
6. **And** the user clicks on Create Company
7. **Then** the user is in the companies page
8. **And** the user clicks on delete the company 'Innovate Real Estate'

### Expected Result

The company "Innovate Real Estate" should be successfully deleted from the list, and the user should remain on the company listing page without any errors.
### Actual Result

The application crashes, and a "Page Not Found" error is displayed in the browser. The company remains in the list.
### Environment

* **Operating System:** Windows
* **Browser:** Chrome


---

## Defect Report: Property Deletion - "Page Not Found" Error

* **ID:** DR-002
* **Date Reported:** 7/20/2025
* **Reported By:** JF
* **Module:** Property Management
* **Severity:** High (Application crash, core functionality failing)
* **Priority:** High
* **Status:** Open

### Description

When a user attempts to delete a property that has just been created, the application crashes and displays a "Page Not Found" error. This prevents the successful deletion of properties, impacting essential data management functionality
### Steps to Reproduce

1. **Given** the user is in the Properties Page
2. **When** the user clicks on +Create Property
3. **And** the user enters 'Ocean View Villa' as Property Name
4. **And** the user enters '123 Seaside Ave' as Address
5. **And** the user enters '1500000' as Price
6. **And** the user enters '200 sqm' as Size
7. **And** the user selects 'Sunrise Builders' as Company
8. **And** the user clicks on Create Property
9. **Then** the user is in the Properties Page
10. **And** the user clicks on delete the property 'Ocean View Villa'

### Expected Result

The property "Ocean View Villa" should be successfully deleted from the list, and the user should remain on the property listing page without any errors.
### Actual Result

The application crashes, and a "Ocean View Villa" error is displayed in the browser. The property remains in the list.
### Environment

* **Operating System:** Windows
* **Browser:** Chrome


---

## Defect Report: Orphaned Properties After Company Deletion

* **ID:** DR-003
* **Date Reported:** 7/20/2025
* **Reported By:** JF
* **Module:** Company Management, Property Management
* **Severity:** Medium (Data inconsistency, functional flaw)
* **Priority:** Medium
* **Status:** Open

### Description

When a company is deleted from the application, its associated properties are not automatically removed from the property list. This leads to orphaned properties being displayed, creating data inconsistency and an inaccurate representation of active properties.
### Steps to Reproduce

1. **Given** the user is in the companies page
2. **When** the user clicks on delete the company 'Sunrise Builders'
3. **And** the user clicks on Properties
9. **Then** the following properties are not listed:
* | Mountain Cabin | 111 Pine Hill | $180000.00 | 80 sqm  | Sunrise Builders |
* | Lakeside Villa | 222 Lake Road | $450000.00 | 200 sqm | Sunrise Builders |
* | Modern Duplex  | 333 Oak Lane  | $370000.00 | 140 sqm | Sunrise Builders |


### Expected Result

After "Sunrise Builders" is deleted, "Sunrise Builders" (and any other properties associated with "Sunrise Builders") should no longer be listed in the properties section. Properties associated with a deleted company should also be removed.
### Actual Result

Despite "Sunrise Builders" being deleted, any properties associated with "Sunrise Builders" remain listed in the properties section. This creates "orphaned" properties without an existing parent company.
### Environment

* **Operating System:** Windows
* **Browser:** Chrome

---