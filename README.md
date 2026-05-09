# Employee-Onboarding-System
A fully automated digital onboarding platform that streamlines the entire employee joining process — from offer-letter acceptance to Day 1 readiness — including account provisioning, document collection, equipment allocation, and automated welcome communications.


# 🚀 HRMS Employee Onboarding System (Serverless)

A fully automated, production-style HR onboarding system built using AWS serverless architecture.  
This system handles employee creation, document collection, workflow automation, and notifications from Day 0 to Day 1 readiness.

---

## 📌 Overview

This project implements an end-to-end onboarding pipeline where:

- HR creates a new employee
- System provisions user access (Cognito)
- Employee uploads required documents
- Automated reminders are sent for pending tasks
- Workflow progresses through multiple stages
- Notifications are triggered on completion

---

## 🏗️ Architecture

**Core AWS Services Used:**

- **API Gateway** – REST API layer
- **AWS Lambda** – Backend logic
- **DynamoDB** – Employee data storage
- **Amazon S3** – Document storage
- **AWS Step Functions** – Workflow orchestration
- **Amazon SES** – Email notifications (welcome + reminders)
- **Amazon SNS** – Completion notifications
- **Amazon Cognito** – Authentication & authorization
- **CloudFront + S3** – Frontend hosting

---

## 🔄 Workflow

Create Employee → Cognito User Created → Welcome Email Sent
↓
Step Function Triggered
↓
Document Collection (S3 Upload)
↓
Reminder (SES Email if pending)
↓
All Documents Uploaded
↓
Status Updated → SNS Notification Sent
↓
IT Provisioning → Policy Sign-off → Manager Intro


---

## 👥 User Roles

### 🧑‍💼 HR
- Create employees
- View onboarding status of all employees

### 👨‍💻 Employee
- Login via Cognito
- Upload required documents
- Track onboarding progress

---

## 📂 Project Structure
/backend
├── EmployeeFunction (Create employee + Cognito + SES)
├── upload_employee_document (S3 upload + Step Function trigger + SNS)
├── get_onboarding_status
├── reminder_check_lambda (SES reminders)
├── it_provisioning_lambda
├── policy_signoff_lambda
├── manager_intro_lambda
├── failure_handler_lambda

/frontend
├── index.html (HR + Employee portal)

/step-function
├── onboarding_workflow.json


---

## 🗄️ DynamoDB Schema (Employee Table)

| Attribute | Description |
|----------|------------|
| employee_id | Unique UUID |
| cognito_sub | Cognito user ID |
| email | Employee email |
| department | Department |
| role | Job role |
| manager_id | Manager reference |
| joining_date | Joining date |
| employment_type | Full-time / Intern / Contract |
| documents | Document status map |
| onboarding_status | Stage-wise progress |
| overall_status | IN_PROGRESS / COMPLETED |
| created_at | Timestamp |

---

## 📤 Document Upload

Employees upload:

- ID Proof
- Degree Certificate
- Signed Offer Letter

Stored securely in S3 with structured path: employee_id/document_type/file_name


---

## 🔔 Notifications

### 📧 Amazon SES
- Welcome email (on employee creation)
- Reminder emails (if documents pending)

### 📢 Amazon SNS
- Triggered when onboarding is completed

---

## 🔐 Authentication

- Managed using Amazon Cognito
- Role-based access using Cognito Groups:
  - `HR`
  - `EMPLOYEE`

---

## 🌐 Frontend

- Hosted on S3 + CloudFront
- Simple UI with:
  - HR dashboard
  - Employee upload portal
- JWT-based authentication using Cognito

---

## ⚙️ Setup Instructions



1. Configure Environment Variables (Lambda)
Set for relevant functions:
TABLE_NAME
BUCKET_NAME
STATE_MACHINE_ARN
FROM_EMAIL
SNS_TOPIC_ARN
USER_POOL_ID

2. Deploy Services
Create DynamoDB table
Create S3 bucket
Deploy Lambda functions
Configure API Gateway routes
Deploy Step Function
Configure SES (verify emails or move out of sandbox)
Configure SNS topic

3. Frontend
Upload index.html to S3
Enable static hosting
(Optional) Add CloudFront
🧪 Demo Flow
HR logs in
Create employee
Cognito user + welcome email sent
Step Function starts
Employee uploads documents
Reminder email (if pending)
All docs completed → SNS triggered
Workflow completes
💰 Cost Estimate

Estimated cost for ~50 onboarding/month:

Lambda: negligible
DynamoDB: low usage
S3: minimal storage
SES/SNS: very low

👉 Approx: ~$5–10/month

🚀 Key Features
Serverless architecture
Event-driven workflow
Automated reminders
Role-based access control
Real-time status tracking
Scalable and cost-efficient
