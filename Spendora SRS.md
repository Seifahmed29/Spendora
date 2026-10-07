# Spendora

## Software Requirements Specification (SRS)

| | |
|---|---|
| **Project Type** | Personal Finance Management & Expense Tracking System |
| **Platform** | Cross-platform Mobile Application |
| **Primary Client** | Flutter Mobile Application |
| **Backend** | Python + FastAPI |
| **Database** | PostgreSQL |
| **Cloud Database** | Supabase PostgreSQL |
| **Document Version** | 1.0 |
| **Status** | Baseline Specification |

---

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional, non-functional, technical, security, data, integration, and operational requirements of Spendora, a personal finance management and expense tracking application.

The purpose of this document is to provide a single, unambiguous reference for:

- Project stakeholders
- UI/UX designers
- Flutter developers
- Backend developers
- Database developers
- QA/test engineers
- DevOps engineers
- Project supervisors
- Documentation and graduation-project reviewers

The SRS defines what Spendora must do, while the implementation roadmap defines how and in what order the team will build it.

---

## 2. Product Overview

### 2.1 Product Definition

Spendora is a personal finance management application that enables users to manage their financial information, record income and expenses, organize transactions, manage multiple financial accounts, create budgets and financial goals, monitor subscriptions, and understand their financial behavior through analytics and reports.

The application is designed to provide users with a centralized view of their personal finances through an easy-to-use mobile interface.

---

## 3. Problem Statement

Managing personal finances manually can make it difficult for users to:

- Track daily expenses
- Understand where their money is going
- Manage multiple financial accounts
- Control spending against a budget
- Monitor financial goals
- Track recurring subscriptions
- Identify spending patterns
- Understand monthly financial performance

Spendora addresses these problems by providing an integrated personal finance management system that organizes financial information and presents meaningful summaries and analytics.

---

## 4. Objectives

Spendora shall:

1. Allow users to securely create and manage accounts.
2. Allow users to authenticate securely.
3. Allow users to manage multiple financial accounts.
4. Allow users to organize transactions into categories.
5. Allow users to record income and expenses.
6. Allow users to search and filter transactions.
7. Allow users to create and monitor budgets.
8. Provide financial analytics and spending trends.
9. Allow users to create financial goals.
10. Allow users to track subscriptions.
11. Provide relevant financial notifications.
12. Generate financial reports.
13. Provide a centralized financial dashboard.
14. Protect user financial data through authentication and authorization.
15. Provide a scalable architecture that can be extended in the future.

---

## 5. Scope

### 5.1 In Scope

The initial Spendora system shall include:

- User registration
- User login
- Authentication
- JWT-based authorization
- User profile
- Financial accounts
- Categories
- Income
- Expenses
- Transactions
- Dashboard
- Budgets
- Analytics
- Financial goals
- Subscriptions
- Notifications
- Reports
- Settings
- Security controls
- Testing
- Monitoring
- Deployment
- Basic local caching/offline support if schedule permits

These features correspond to the project's defined MVP scope.

---

## 6. Out of Scope

The following shall not be required for the initial version:

1. Direct bank API integration
2. Investment portfolio management
3. Cryptocurrency management
4. Complex household/family financial management
5. Artificial intelligence features
6. Microservices architecture
7. Advanced offline synchronization
8. Complex banking operations
9. Real-money transfers
10. Direct interaction with banking infrastructure

These items may be considered future enhancements.

---

## 7. Target Users

### 7.1 Registered User

The primary system actor is the registered user.

A registered user can:

- Log in
- Manage their profile
- Manage accounts
- Manage categories
- Create transactions
- Manage budgets
- View analytics
- Manage goals
- Manage subscriptions
- Receive notifications
- Generate reports
- Manage application settings

---

## 8. System Actors

| Actor | Description |
|---|---|
| User | Primary person using Spendora |
| Authentication System | Handles identity verification and authorization |
| Backend API | Provides business logic and data services |
| PostgreSQL Database | Stores persistent application data |
| Firebase FCM | Delivers push notifications |
| Monitoring Services | Monitor backend and mobile application behavior |

There is no administrative actor required for the core MVP unless an administrative dashboard is added later.

---

## 9. High-Level System Architecture

Spendora shall follow a client-server architecture.

```text
┌──────────────────────────┐
│      Flutter Mobile      │
│                          │
│ UI                       │
│ Riverpod                 │
│ Use Cases                │
│ Repositories             │
│ Dio                      │
└────────────┬─────────────┘
             │ HTTPS / REST
             ▼
┌──────────────────────────┐
│       FastAPI API        │
│                          │
│ Routers                  │
│ Services                 │
│ Repositories             │
│ Authentication           │
│ Validation               │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      SQLAlchemy ORM      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    PostgreSQL Database   │
│       / Supabase         │
└──────────────────────────┘
```

The mobile application shall not communicate directly with PostgreSQL.

All protected data access shall pass through the backend API.

---

## 10. Technology Requirements

### 10.1 Frontend

The mobile application shall use:

- Flutter
- Dart
- Riverpod
- GoRouter
- Dio
- Freezed
- JSON serialization
- Flutter Secure Storage
- fl_chart

The roadmap specifies these technologies for the Flutter foundation.

### 10.2 Backend

The backend shall use:

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- psycopg
- Pydantic
- pydantic-settings
- Alembic
- JWT
- Argon2 or bcrypt

The defined backend foundation includes these technologies.

### 10.3 Database

The system shall use:

- PostgreSQL
- Supabase PostgreSQL for hosted database infrastructure
- SQLAlchemy ORM
- Alembic migrations

The database design shall use primary keys, foreign keys, uniqueness constraints, NOT NULL constraints, CHECK constraints, and appropriate indexes.

---

## 11. Functional Requirements

Functional requirements define the behavior that Spendora shall provide.

### FR-01 Authentication

#### FR-01.1 Registration

The system shall allow a new user to create an account.

The registration process shall collect the required user information.

The system shall:

1. Validate submitted information.
2. Verify that the account does not already exist.
3. Hash the password.
4. Store the user.
5. Return an appropriate response.

#### FR-01.2 Password Security

Passwords shall never be stored in plaintext.

The backend shall use a secure password hashing algorithm such as:

- Argon2
- bcrypt

The roadmap explicitly specifies Argon2/bcrypt.

#### FR-01.3 Login

The system shall provide a login mechanism.

The login process shall:

1. Receive user credentials.
2. Locate the user.
3. Verify the password.
4. Generate authentication tokens.
5. Return the required authentication information.

#### FR-01.4 JWT Authentication

The backend shall generate:

- Access token
- Refresh token

Protected endpoints shall require valid authentication.

The authentication flow shall associate the authenticated request with the corresponding user ID.

#### FR-01.5 Current User

The system shall provide an endpoint for retrieving the currently authenticated user.

Example:

```http
GET /api/v1/users/me
```

#### FR-01.6 Logout

The application shall provide logout functionality.

Logout shall clear locally stored authentication credentials and invalidate refresh credentials where applicable.

#### FR-01.7 Authentication State

Flutter shall maintain authentication state using Riverpod.

The application shall distinguish between:

- Unauthenticated
- Authenticating
- Authenticated
- Authentication failure

#### FR-01.8 Protected Navigation

GoRouter shall enforce authentication redirects.

Example:

```text
Unauthenticated
      ↓
   /login

Authenticated
      ↓
    /app
```

The project architecture explicitly requires authentication-based routing.

---

### FR-02 User Profile

The system shall allow users to view and manage their profile.

Profile functionality shall include:

- View profile
- Update profile information
- Change password where supported
- Manage application preferences
- Logout

A user's profile information shall belong exclusively to that user.

---

### FR-03 Financial Accounts

#### FR-03.1 Account Creation

Users shall be able to create financial accounts.

Supported account types shall include:

- Cash
- Bank
- Credit Card
- Debit Card
- E-Wallet
- Savings

These account types are defined in the project roadmap.

#### FR-03.2 Account Operations

Users shall be able to:

- Create an account
- View accounts
- View account details
- Edit an account
- Delete an account

Example API:

```http
POST   /api/v1/accounts
GET    /api/v1/accounts
GET    /api/v1/accounts/{id}
PUT    /api/v1/accounts/{id}
DELETE /api/v1/accounts/{id}
```

#### FR-03.3 Account Ownership

Users shall only be able to access accounts belonging to themselves.

A user shall never be able to access another user's account by modifying an account ID.

---

### FR-04 Categories

#### FR-04.1 Default Categories

The system shall provide default categories including:

- Food
- Transport
- Shopping
- Bills
- Entertainment
- Health
- Education
- Travel
- Other

These are the baseline categories defined for Spendora.

#### FR-04.2 Custom Categories

If included in the final MVP, users shall be able to create and manage custom categories.

Custom categories shall belong to the user who created them.

#### FR-04.3 Category Operations

Users shall be able to:

- View categories
- Create custom categories
- Edit custom categories
- Delete custom categories where permitted

---

### FR-05 Transactions

Transactions represent the core financial records of Spendora.

The roadmap identifies transactions as the core feature of the application.

#### FR-05.1 Transaction Types

The system shall support:

```text
INCOME
EXPENSE
```

#### FR-05.2 Transaction Data

A transaction shall contain, at minimum:

- ID
- User
- Amount
- Transaction type
- Account
- Category
- Description
- Date
- Creation timestamp
- Update timestamp

The roadmap explicitly identifies amount, type, category, account, description, and date as transaction data.

#### FR-05.3 Create Transaction

Users shall be able to create:

- Income transactions
- Expense transactions

The system shall validate:

- Amount
- Transaction type
- Account
- Category
- Date
- User ownership

#### FR-05.4 Edit Transaction

Users shall be able to edit their transactions.

#### FR-05.5 Delete Transaction

Users shall be able to delete their transactions.

#### FR-05.6 Transaction Search

Users shall be able to search transactions.

#### FR-05.7 Transaction Filtering

The system shall support filtering by:

- Date
- Category
- Account
- Income/Expense type
- Amount

These filters are explicitly specified in the project roadmap.

---

### FR-06 Dashboard

The dashboard shall provide a centralized overview of the user's financial state.

The dashboard shall display:

- Total balance
- Total income
- Total expenses
- Savings
- Recent transactions
- Spending breakdown
- Budget progress

The dashboard depends on accounts, transactions, categories, and analytics.

#### FR-06.1 Balance

The system shall calculate the user's current financial balance based on the supported financial records.

#### FR-06.2 Recent Transactions

The dashboard shall display recent financial transactions.

#### FR-06.3 Spending Summary

The dashboard shall provide a summary of spending by relevant categories.

---

### FR-07 Budgets

#### FR-07.1 Budget Creation

Users shall be able to create budgets.

A budget shall define a spending limit associated with a category or applicable budgeting scope.

#### FR-07.2 Budget Operations

Users shall be able to:

- Create budgets
- View budgets
- Edit budgets
- Delete budgets

Example API:

```http
POST   /api/v1/budgets
GET    /api/v1/budgets
PUT    /api/v1/budgets/{id}
DELETE /api/v1/budgets/{id}
```

#### FR-07.3 Budget Calculation

The system shall calculate:

```text
Budget Limit
      ↓
Transactions
      ↓
Category Filter
      ↓
Spent
      ↓
Remaining
      ↓
Utilization %
```

This calculation model is defined in the roadmap.

#### FR-07.4 Budget Status

The system shall identify at least:

- Normal spending
- Approaching budget limit
- Exceeded budget

---

### FR-08 Analytics

The analytics system shall provide users with meaningful summaries of their financial activity.

The backend shall calculate:

- Total income
- Total expenses
- Net savings
- Savings rate
- Category distribution
- Monthly spending
- Weekly spending
- Budget utilization

These analytics requirements are defined in the project roadmap.

#### FR-08.1 Analytics APIs

The system shall provide analytics endpoints such as:

```http
GET /api/v1/analytics/overview
GET /api/v1/analytics/monthly
GET /api/v1/analytics/categories
GET /api/v1/analytics/accounts
```

#### FR-08.2 Charts

The Flutter application shall visualize analytics using charts.

The project specifies fl_chart.

Supported visualizations may include:

- Pie/donut charts
- Bar charts
- Line charts
- Spending trends

#### FR-08.3 Savings Rate

The system shall calculate a savings rate based on income and expenses.

The exact mathematical behavior shall be documented in the implementation/API contract, especially for zero-income cases.

---

### FR-09 Financial Goals

Users shall be able to create financial goals.

#### FR-09.1 Goal Data

A goal shall include:

- Goal name
- Target amount
- Current amount
- Remaining amount
- Progress
- Relevant dates where applicable

#### FR-09.2 Goal Operations

Users shall be able to:

- Create goals
- View goals
- Edit goals
- Delete goals
- Add contributions

Example API:

```http
POST   /api/v1/goals
GET    /api/v1/goals
PUT    /api/v1/goals/{id}
DELETE /api/v1/goals/{id}
```

#### FR-09.3 Goal Calculations

The system shall calculate:

```text
remaining = target - current
progress = current / target × 100
```

The roadmap defines these calculations.

---

### FR-10 Subscriptions

Users shall be able to track recurring subscriptions.

#### FR-10.1 Subscription Data

A subscription shall contain:

- Name
- Amount
- Billing cycle
- Next payment date
- Category
- Account

These fields are defined in the roadmap.

#### FR-10.2 Subscription Operations

Users shall be able to:

- Create subscriptions
- View subscriptions
- Edit subscriptions
- Delete subscriptions

Example API:

```http
POST   /api/v1/subscriptions
GET    /api/v1/subscriptions
PUT    /api/v1/subscriptions/{id}
DELETE /api/v1/subscriptions/{id}
```

#### FR-10.3 Subscription Analytics

The system shall calculate:

- Monthly subscription cost
- Yearly subscription cost
- Upcoming payments

---

### FR-11 Recurring Transactions

Recurring transactions are an optional extension of the core system.

Examples include:

- Salary
- Rent
- Regular bills

The system may support:

- Frequency
- Amount
- Category
- Account
- Next occurrence

A scheduled backend process may:

```text
Check due recurring transaction
          ↓
Create transaction
          ↓
Update next occurrence
```

The roadmap explicitly places recurring transactions after subscriptions and states they may be implemented if time permits.

---

### FR-12 Notifications

The system shall support financial notifications.

Potential notification types include:

- Budget warning
- Subscription reminder
- Goal milestone
- Monthly summary

The planned notification architecture is:

```text
FastAPI
   ↓
Notification Service
   ↓
Firebase FCM
   ↓
Flutter
```

This architecture is specified in the roadmap.

---

### FR-13 Reports

The system shall provide financial reports.

Reports shall include, where implemented:

- Monthly report
- Spending report
- Budget report

Reports may be exported as:

- PDF
- CSV

The roadmap identifies Reports as a later feature and not an MVP blocker if schedule becomes constrained.

---

### FR-14 Local Persistence / Offline Support

The application may provide local persistence for improved usability.

The preferred approach is:

- Drift
- SQLite

The architecture shall separate local and remote data sources:

```text
Repository
   /       \
Remote     Local
  │          │
 Dio        Drift
  │          │
FastAPI    SQLite
```

Local persistence shall not be implemented before the online system is stable.

Advanced offline synchronization is explicitly outside the initial scope.

---

### FR-15 Settings

The system shall provide application settings.

Settings may include:

- User preferences
- Notification preferences
- Theme preferences
- Security-related settings
- Logout

---

## 12. Data Requirements

### 12.1 Core Entities

The core database shall contain entities for:

```text
User
Account
Category
Transaction
Budget
BudgetCategory
Goal
Subscription
Notification
```

Potential additional entities include:

```text
RefreshToken
RecurringTransaction
Attachment
```

The baseline entity list is derived from the project database design.

---

## 13. Entity Relationships

The primary relationships shall include:

```text
User 1 ───── N Account
User 1 ───── N Category
User 1 ───── N Transaction
Account 1 ── N Transaction
Category 1 ─ N Transaction
User 1 ───── N Budget
User 1 ───── N Goal
User 1 ───── N Subscription
User 1 ───── N Notification
```

The database shall enforce referential integrity using foreign keys.

---

## 14. Database Constraints

The database shall use:

- Primary keys
- Foreign keys
- Unique constraints
- NOT NULL constraints
- CHECK constraints
- Indexes

Financial amounts shall satisfy appropriate positive-value constraints where applicable.

For example:

```text
amount > 0
```

The roadmap explicitly requires these constraint types.

---

## 15. Database Migration Requirements

Alembic shall be used for database migrations.

The migration flow shall be:

```text
SQLAlchemy Models
       ↓
Alembic Migration
       ↓
PostgreSQL
```

Database schema changes shall be version-controlled.

Manual production database modifications should be avoided except when properly documented and controlled.

---

## 16. API Requirements

### 16.1 API Versioning

The backend shall use:

```text
/api/v1
```

The planned modules include:

```text
auth
users
accounts
categories
transactions
budgets
analytics
goals
subscriptions
notifications
```

This module structure is defined in the architecture roadmap.

---

## 17. API Design

The API shall follow REST principles.

Example:

```http
POST   /accounts
GET    /accounts
GET    /accounts/{id}
PUT    /accounts/{id}
DELETE /accounts/{id}
```

The API shall use appropriate HTTP status codes.

Example:

| Status | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 204 | Successful request with no response body |
| 400 | Invalid request |
| 401 | Unauthenticated |
| 403 | Forbidden |
| 404 | Resource not found |
| 409 | Conflict |
| 422 | Validation error |
| 500 | Internal server error |

---

## 18. API Validation

Pydantic shall be used for request and response validation.

The backend shall reject invalid data before it reaches business logic or persistence.

Examples include:

- Invalid amounts
- Invalid dates
- Missing required fields
- Invalid IDs
- Invalid enum values
- Invalid authentication credentials

---

## 19. API Documentation

FastAPI's automatic Swagger/OpenAPI documentation shall be used.

The API shall be tested independently before complete Flutter integration.

The roadmap specifically requires continuous Swagger/OpenAPI usage.

---

## 20. Flutter Architecture Requirements

The Flutter application shall use feature-based architecture.

A baseline structure shall be:

```text
lib/
├── core/
└── features/
    ├── auth/
    ├── dashboard/
    ├── transactions/
    ├── accounts/
    ├── categories/
    ├── budgets/
    ├── analytics/
    ├── goals/
    ├── subscriptions/
    └── profile/
```

This structure follows the project's architecture specification.

---

## 21. Flutter Data Flow

The application shall follow:

```text
Flutter UI
   ↓
Riverpod
   ↓
Use Case
   ↓
Repository
   ↓
Dio
   ↓
FastAPI
   ↓
Service
   ↓
Repository
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

The complete integration chain is defined in the roadmap.

---

## 22. Dio Requirements

A centralized Dio client shall handle:

- Base URL
- Headers
- Authentication
- JWT
- Interceptors
- Error handling
- Refresh-token handling

Individual screens shall not create independent Dio clients.

The roadmap explicitly requires one central API client.

---

## 23. Freezed Requirements

Freezed shall be used for typed Flutter models where appropriate.

Models shall support JSON serialization.

Core models shall include:

- User
- Account
- Category
- Transaction
- Budget
- Goal
- Subscription

The intended data flow is:

```text
FastAPI JSON
    ↓
Dio
    ↓
Freezed Model
    ↓
Riverpod
    ↓
Flutter UI
```

---

## 24. Navigation Requirements

GoRouter shall manage navigation.

The navigation system shall support routes such as:

```text
/
├── splash
├── onboarding
├── login
├── register
└── app
    ├── home
    ├── transactions
    ├── budgets
    ├── analytics
    └── profile
```

Authentication redirects shall prevent unauthenticated access to protected application screens.

---

## 25. Security Requirements

Security shall be treated as a continuous requirement, not only a final phase.

### 25.1 Authentication Security

The system shall:

- Hash passwords
- Validate JWTs
- Protect private endpoints
- Use refresh tokens appropriately
- Enforce resource ownership

### 25.2 Authorization

Authentication alone shall not be considered sufficient.

For every protected resource:

```text
JWT
 ↓
user_id
 ↓
resource ownership
```

A user must only access resources belonging to them.

### 25.3 Sensitive Data

The system shall not:

- Store plaintext passwords
- Expose secrets in source code
- Log passwords
- Expose authentication secrets
- Commit `.env` files containing secrets

The roadmap explicitly requires `.env` to be excluded from Git.

### 25.4 Mobile Security

Authentication tokens shall be stored using secure storage.

Flutter Secure Storage shall be used instead of ordinary preferences for authentication tokens.

The application shall not contain backend secrets.

### 25.5 Transport Security

Production API communication shall use HTTPS.

### 25.6 CORS

The backend shall configure CORS appropriately for supported clients.

### 25.7 Rate Limiting

Sensitive endpoints such as authentication endpoints should be protected against excessive requests.

### 25.8 SQL Injection

Database access shall use SQLAlchemy and parameterized queries rather than unsafe string-generated SQL.

---

## 26. Non-Functional Requirements

### NFR-01 Performance

Normal API requests should respond within an acceptable time under expected project load.

Analytics queries shall be optimized to avoid unnecessary database operations.

### NFR-02 Scalability

The architecture shall allow additional features to be added without rewriting the entire system.

The system should support future expansion into:

- Bank integrations
- AI-based financial assistance
- Advanced analytics
- More financial entities

without requiring a complete architectural redesign.

### NFR-03 Availability

The deployed backend should remain available during normal operating periods.

External infrastructure failures shall be handled gracefully.

### NFR-04 Reliability

The system shall prevent invalid financial records.

Financial calculations shall be deterministic and testable.

### NFR-05 Maintainability

The system shall use modular architecture.

Backend functionality shall be organized by modules/features.

Flutter functionality shall be organized by features.

### NFR-06 Usability

The mobile application shall:

- Use clear navigation
- Provide understandable labels
- Provide validation feedback
- Provide loading states
- Provide error states
- Provide empty states
- Minimize unnecessary user steps

### NFR-07 Accessibility

The application should support:

- Readable typography
- Adequate touch targets
- Sufficient contrast
- Meaningful labels
- Accessible interactive elements

### NFR-08 Responsiveness

The UI shall adapt to supported mobile screen sizes.

### NFR-09 Security

Financial information shall only be accessible to authorized users.

Cross-user data access shall be explicitly tested.

### NFR-10 Maintainable API

The backend API shall use consistent:

- Naming
- Validation
- Error handling
- Authentication
- Response structures
- Versioning

---

## 27. Error Handling Requirements

The backend shall return meaningful errors.

Errors shall not expose:

- Passwords
- JWT secrets
- Database credentials
- Internal stack traces
- Sensitive infrastructure information

Flutter shall convert API errors into user-friendly messages.

The application shall distinguish between:

- Validation errors
- Authentication errors
- Authorization errors
- Network errors
- Server errors
- Not-found errors

---

## 28. UI/UX Requirements

The project shall include UI/UX design before serious feature implementation.

The initial design should cover:

1. Splash
2. Onboarding
3. Login
4. Register
5. Home
6. Add expense
7. Add income
8. Transactions
9. Transaction details
10. Accounts
11. Account details
12. Budgets
13. Budget details
14. Analytics
15. Goals
16. Goal details
17. Subscriptions
18. Subscription details
19. Notifications
20. Profile
21. Settings

These screens are identified in the project's UI/UX roadmap.

---

## 29. UI State Requirements

Major screens shall handle:

```text
Loading
Success
Empty
Error
```

For example:

```text
Transactions
     │
     ├── Loading
     ├── Transactions available
     ├── No transactions
     └── Failed to load
```

---

## 30. Notification Requirements

Notifications shall be categorized by event.

Examples:

**Budget**

- Budget approaching limit
- Budget exceeded

**Subscription**

- Subscription payment approaching

**Goal**

- Goal milestone reached
- Goal completed

**Summary**

- Monthly financial summary

---

## 31. Testing Requirements

Testing shall occur throughout development rather than only at the end.

### 31.1 Backend Testing

Pytest shall be used.

Backend tests shall cover:

- Authentication
- Transactions
- Budgets
- Accounts
- Analytics
- Goals
- Subscriptions
- Authorization

### 31.2 Flutter Testing

Flutter tests shall cover:

- Widgets
- Providers
- Use cases
- Repositories
- Navigation

### 31.3 Integration Testing

The complete flow shall be tested:

```text
Flutter
 ↓
Dio
 ↓
FastAPI
 ↓
SQLAlchemy
 ↓
PostgreSQL
```

### 31.4 Authorization Testing

A critical security test shall verify:

```text
User A
   X
   ↓
User B's data
```

User A must never be able to retrieve, modify, or delete User B's resources.

The project roadmap explicitly identifies this as an important backend test.

---

## 32. API Testing

A Postman collection shall be maintained.

The collection shall contain:

```text
Spendora API
├── Auth
├── Users
├── Accounts
├── Categories
├── Transactions
├── Budgets
├── Analytics
├── Goals
└── Subscriptions
```

The roadmap defines this organization for independent backend testing.

---

## 33. DevOps Requirements

### 33.1 Git Repository

The project shall use a single repository.

Suggested structure:

```text
spendora/
├── mobile/
├── backend/
├── docs/
├── docker/
└── .github/
```

This repository structure is defined in the architecture roadmap.

### 33.2 Branching Strategy

The repository shall use:

```text
main
develop
feature/*
```

Development shall occur on feature branches.

The intended flow is:

```text
Feature Branch
      ↓
Pull Request
      ↓
Code Review
      ↓
develop
      ↓
Testing
      ↓
main
```

No developer should directly push to `main`.

---

## 34. CI Requirements

GitHub Actions shall be used for continuous integration.

Pull requests should automatically execute:

```text
Python lint
Pytest
Flutter analyze
Flutter tests
```

The project's roadmap defines this CI workflow.

---

## 35. Docker Requirements

The backend shall be containerizable.

The project shall include, where applicable:

```text
Dockerfile
docker-compose.yml
```

A development environment may contain:

```text
Flutter
   ↓
FastAPI Container
   ↓
PostgreSQL
```

Docker shall be introduced after the backend is functional rather than being a prerequisite for feature development.

---

## 36. Deployment Requirements

The production architecture shall include:

```text
Flutter Mobile App
        │
       HTTPS
        ↓
FastAPI Backend
        │
        ↓
PostgreSQL / Supabase
```

The backend shall be deployed to an appropriate cloud platform such as Render or Railway.

The database shall use Supabase PostgreSQL.

---

## 37. Monitoring Requirements

### Backend

Sentry shall be used for:

- API exceptions
- Backend errors
- Performance monitoring

### Flutter

Firebase Crashlytics shall be used for:

- Application crashes
- Runtime crash diagnostics

The roadmap recommends Sentry for backend/API errors and performance, and Crashlytics for mobile crashes.

---

## 38. Logging Requirements

Logs shall support debugging without exposing sensitive information.

The system shall not log:

- Passwords
- Authentication secrets
- JWT secrets
- Database credentials

---

## 39. Data Ownership

All personal financial records shall belong to the authenticated user who created them.

The following resources shall be user-scoped:

- Accounts
- Categories
- Transactions
- Budgets
- Goals
- Subscriptions
- Notifications
- Profile data

---

## 40. Data Integrity Rules

The system shall ensure:

1. Every transaction belongs to a valid user.
2. Every transaction references a valid account when required.
3. Every transaction references a valid category when required.
4. Users cannot reference resources belonging to other users.
5. Financial amounts cannot contain invalid values.
6. Foreign-key relationships remain consistent.
7. Deleted entities do not leave invalid orphaned records.

---

## 41. Core Business Rules

**BR-01** — Every financial record must belong to an authenticated user.

**BR-02** — A transaction must have a valid transaction type.

Valid types:

```text
INCOME
EXPENSE
```

**BR-03** — Transaction amounts must satisfy the system's positive-value validation.

**BR-04** — A budget's spending amount shall be calculated from relevant transactions.

**BR-05** — Budget utilization shall be calculated based on the budget limit and spending.

**BR-06** — Goal progress shall be calculated from current amount and target amount.

**BR-07** — Subscription summaries shall account for their billing cycles.

**BR-08** — Analytics shall only use financial data belonging to the authenticated user.

---

## 42. API Security Model

The API shall distinguish between:

### Public endpoints

Examples:

```http
POST /api/v1/auth/register
POST /api/v1/auth/login
```

### Protected endpoints

Examples:

```http
GET  /api/v1/users/me
GET  /api/v1/accounts
POST /api/v1/accounts
GET  /api/v1/transactions
POST /api/v1/transactions
GET  /api/v1/budgets
GET  /api/v1/analytics/overview
```

Protected endpoints shall require valid authentication.

---

## 43. Acceptance Criteria

A feature shall be considered complete only when:

1. Its database requirements are implemented.
2. Its backend API is implemented.
3. Its validation is implemented.
4. Its authorization is implemented.
5. Its API has been tested.
6. Its Flutter data layer is implemented.
7. Its UI is implemented.
8. Loading/error/empty states are handled.
9. Integration with the backend works.
10. Relevant automated tests exist.
11. Code passes review.
12. The feature works through the complete application flow.

---

## 44. Feature Completion Definition

For example, Transactions are **not** complete merely because the backend has:

```http
POST /transactions
```

Transactions are complete when:

```text
Database
   ↓
SQLAlchemy
   ↓
Transaction Service
   ↓
Transaction API
   ↓
Swagger/Postman Tests
   ↓
Dio
   ↓
Repository
   ↓
Riverpod
   ↓
Flutter UI
   ↓
Create/Edit/Delete/Search/Filter
   ↓
Error + Loading States
   ↓
Authorization Tests
   ↓
Integration Test
```

This definition shall apply to other major features as well.

---

## 45. Requirements Traceability

Each major requirement should be traceable to:

```text
Requirement
    ↓
Use Case
    ↓
Database Entity
    ↓
Backend API
    ↓
Flutter Feature
    ↓
Test Case
```

Example:

```text
Create Expense
      ↓
UC-Transaction-01
      ↓
Transaction Entity
      ↓
POST /transactions
      ↓
Transaction Feature
      ↓
TC-Transaction-01
```

---

## 46. Use Case Catalogue

### UC-01 Register

**Actor:** User

**Precondition:** User is not registered.

**Main Flow:**

1. User opens registration screen.
2. User enters required information.
3. Application validates input.
4. Application sends registration request.
5. Backend validates request.
6. Password is securely hashed.
7. User is created.
8. System returns success.

**Alternative Flow:**

- Email/account already exists.
- Input is invalid.
- Server/database failure.

### UC-02 Login

**Actor:** User

**Main Flow:**

1. User enters credentials.
2. Flutter sends login request.
3. Backend validates credentials.
4. Backend generates tokens.
5. Flutter securely stores tokens.
6. User is authenticated.
7. User is redirected to the application.

### UC-03 Create Account

1. User opens Accounts.
2. User selects Add Account.
3. User enters account information.
4. Flutter validates input.
5. API request is sent.
6. Backend validates authorization.
7. Account is stored.
8. Updated account list is displayed.

### UC-04 Add Expense

1. User opens Add Transaction.
2. User selects Expense.
3. User enters amount.
4. User selects account.
5. User selects category.
6. User enters optional description.
7. User selects date.
8. User submits transaction.
9. Backend validates request.
10. Transaction is persisted.
11. Dashboard/transactions are updated.

### UC-05 Add Income

Same flow as expense, except:

```text
type = INCOME
```

### UC-06 Create Budget

1. User opens Budgets.
2. User creates a budget.
3. User selects category/scope.
4. User enters spending limit.
5. Backend stores budget.
6. System calculates spending.
7. UI displays budget progress.

### UC-07 View Analytics

1. User opens Analytics.
2. Flutter requests analytics.
3. Backend calculates financial statistics.
4. Backend returns results.
5. Flutter renders charts.

### UC-08 Create Goal

1. User creates a goal.
2. User enters target amount.
3. System stores the goal.
4. User may add contributions.
5. System recalculates progress.

### UC-09 Track Subscription

1. User creates subscription.
2. User enters subscription amount.
3. User selects billing cycle.
4. User selects next payment.
5. User selects category/account.
6. System calculates recurring cost.
7. Upcoming payment can generate a notification.

### UC-10 Receive Notification

1. Financial event occurs.
2. Backend determines whether notification criteria are met.
3. Notification service generates notification.
4. Firebase FCM delivers notification.
5. Flutter displays notification.

---

## 47. Sequence Example — Add Expense

```text
User
 │
 ▼
Flutter UI
 │
 ▼
Riverpod
 │
 ▼
Transaction Use Case
 │
 ▼
Transaction Repository
 │
 ▼
Dio
 │
 ▼
FastAPI
 │
 ▼
JWT Authentication
 │
 ▼
Transaction Service
 │
 ▼
Transaction Repository
 │
 ▼
SQLAlchemy
 │
 ▼
PostgreSQL
 │
 ▼
Response
 │
 ▼
Flutter
 │
 ▼
Updated UI
```

---

## 48. Performance Considerations

The system should:

- Avoid unnecessary API calls.
- Use pagination for large transaction lists where required.
- Use database indexes for frequently queried fields.
- Avoid loading unnecessary historical records.
- Optimize analytics queries.
- Cache appropriate data where local persistence is implemented.

---

## 49. Maintainability Requirements

The codebase shall:

- Follow consistent naming conventions.
- Use modular feature organization.
- Separate presentation from data access.
- Avoid duplicated API clients.
- Avoid duplicated business logic.
- Keep configuration separate from application code.
- Use version-controlled migrations.
- Maintain API documentation.
- Maintain automated tests.

---

## 50. Documentation Requirements

The final project documentation shall include:

1. Requirements
2. Use Case Diagram
3. System Architecture
4. C4 Diagram
5. ERD
6. Class Diagrams
7. Sequence Diagrams
8. API Documentation
9. Testing Documentation
10. Deployment Architecture

These documentation deliverables are explicitly identified in the project roadmap.

---

## 51. MVP Prioritization

### Priority 1 — Core

These features are essential:

- Registration
- Login
- Authentication
- User profile
- Accounts
- Categories
- Income
- Expenses
- Transactions
- Dashboard

### Priority 2 — Financial Management

- Budgets
- Analytics
- Goals
- Subscriptions

### Priority 3 — Supporting Features

- Notifications
- Reports
- Settings
- Monitoring
- Local caching

### Priority 4 — Optional Extensions

- Recurring transactions
- Advanced offline functionality
- Additional reporting
- Future intelligent features

This prioritization preserves the roadmap's distinction between the main MVP and features that can be deferred if schedule constraints occur.

---

## 52. Future Scope

Future versions may introduce:

### Bank Integration

```text
Bank
 ↓
Bank API
 ↓
Spendora
 ↓
Automatic Transactions
```

### AI

Potential future capabilities:

- Expense classification
- Spending recommendations
- Financial insights
- Budget recommendations
- Natural-language financial assistant

### Investments

- Stocks
- Funds
- Portfolio tracking

### Cryptocurrency

- Cryptocurrency accounts
- Portfolio tracking
- Market data

### Family Finance

- Shared accounts
- Household budgets
- Family members
- Permission management

### Advanced Offline Synchronization

- Offline transactions
- Conflict resolution
- Sync queues
- Background synchronization

These are future possibilities and are not required for the initial system.

---

## 53. Project Constraints

The project shall consider:

- Limited graduation-project development time
- Six-person development team
- Mobile-first application
- Academic project requirements
- Limited infrastructure budget
- Need for maintainable architecture
- Need for demonstrable functionality
- Need for complete end-to-end integration

The architecture shall therefore prioritize a modular monolith over unnecessary microservices.

---

## 54. Development Strategy

Development shall be incremental.

The team shall not wait for the entire backend to be completed before beginning Flutter development.

Instead:

```text
Foundation
     ↓
Authentication
     ↓
Accounts + Categories
     ↓
Transactions
     ↓
Dashboard
     ↓
Budgets
     ↓
Analytics
     ↓
Goals + Subscriptions
     ↓
Notifications + Reports
     ↓
Testing + Security
     ↓
Deployment
     ↓
Final Integration
```

Individual backend, database, UI, and Flutter tasks may proceed in parallel when their dependencies are satisfied.

---

## 55. Definition of Done

A feature is considered Done only if:

- Requirements are understood.
- UI/UX is approved.
- Database changes are implemented.
- Alembic migration exists.
- Backend model exists.
- Backend validation exists.
- Backend service exists.
- API endpoint exists.
- Authorization exists.
- Swagger/OpenAPI is updated.
- API has been tested.
- Flutter model exists.
- Repository exists.
- Provider/state management exists.
- UI exists.
- Loading state exists.
- Empty state exists.
- Error state exists.
- Integration works.
- Automated tests exist where applicable.
- Code review is completed.
- No critical bugs remain.

---

## 56. Final System Acceptance Criteria

Spendora shall be considered ready for final demonstration when a new user can successfully complete the following complete scenario:

```text
Register
   ↓
Login
   ↓
Authenticated Session
   ↓
Create Financial Account
   ↓
View Account
   ↓
Create Category / Select Category
   ↓
Add Income
   ↓
Add Expense
   ↓
View Transactions
   ↓
Search / Filter Transactions
   ↓
View Dashboard
   ↓
Create Budget
   ↓
View Budget Utilization
   ↓
View Analytics
   ↓
Create Financial Goal
   ↓
Add Goal Contribution
   ↓
Create Subscription
   ↓
View Upcoming Payment
   ↓
Receive Relevant Notification
   ↓
Generate/View Report
```

The entire flow shall work through the actual production-like architecture:

```text
Flutter
 ↓
Riverpod
 ↓
Use Case
 ↓
Repository
 ↓
Dio
 ↓
HTTPS
 ↓
FastAPI
 ↓
JWT
 ↓
Service Layer
 ↓
Repository Layer
 ↓
SQLAlchemy
 ↓
PostgreSQL
 ↓
Response
 ↓
Flutter UI
```

---

## 57. Final Quality Requirements

Before final submission, the team shall verify:

### Functionality

- Core features work.
- CRUD operations work.
- Calculations are correct.
- Navigation works.
- Authentication works.

### Security

- Passwords are hashed.
- JWT validation works.
- Refresh tokens work where implemented.
- Authorization is enforced.
- Cross-user access is impossible.
- Secrets are not committed.
- HTTPS is used in production.

### Database

- Relationships are correct.
- Constraints are correct.
- Migrations work.
- Indexes exist where needed.
- Data integrity is preserved.

### Backend

- API endpoints work.
- Validation works.
- Errors are handled.
- Swagger is accurate.
- Tests pass.

### Flutter

- UI works.
- State management works.
- API integration works.
- Secure token storage works.
- Loading/error/empty states work.
- Responsive layouts work.

### DevOps

- Repository structure is correct.
- Pull requests are reviewed.
- CI passes.
- Docker works.
- Deployment works.

### Monitoring

- Backend errors are monitored.
- Mobile crashes are monitored.

### Documentation

- SRS is complete.
- ERD is complete.
- Architecture diagrams are complete.
- API documentation is complete.
- Testing documentation is complete.
- Deployment documentation is complete.

---

## 58. Requirements Baseline

This SRS shall be treated as the baseline requirements document for Spendora.

Any major change to the system scope shall be documented and reviewed by the project team before implementation.

Changes shall be classified as:

```text
Required
Optional
Future Scope
Out of Scope
```

This prevents uncontrolled feature expansion during development.

---

## 59. Final Product Definition

Spendora is a secure, modular, mobile-first personal finance management system that enables users to manage accounts, record and organize income and expenses, monitor budgets, analyze financial behavior, track financial goals and subscriptions, receive financial notifications, and generate reports.

The system shall use:

```text
Flutter
    +
FastAPI
    +
SQLAlchemy
    +
PostgreSQL
    +
Supabase
```

with secure authentication, modular architecture, automated testing, CI/CD, deployment, and monitoring.

The architecture shall be designed to support future extensions without requiring fundamental restructuring of the core system.
