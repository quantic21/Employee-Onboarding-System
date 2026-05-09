{
  "Comment": "Simple HRMS Workflow",
  "StartAt": "CheckDocuments",
  "States": {
    "CheckDocuments": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-south-1:593814964617:function:get_onboarding_status",
      "Parameters": {
        "employee_id.$": "$.employee_id"
      },
      "ResultPath": "$.doc",
      "Next": "CheckStatus"
    },
    "CheckStatus": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.doc.status",
          "StringEquals": "COMPLETED",
          "Next": "ITProvisioning"
        }
      ],
      "Default": "Wait24Hours"
    },
    "Wait24Hours": {
      "Type": "Wait",
      "Seconds": 86400,
      "Next": "ReminderCheck"
    },
    "ReminderCheck": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-south-1:593814964617:function:reminder_check_lambda",
      "Parameters": {
        "employee_id.$": "$.employee_id"
      },
      "Next": "CheckDocuments"
    },
    "ITProvisioning": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-south-1:593814964617:function:it_provisioning_lambda",
      "Parameters": {
        "employee_id.$": "$.employee_id"
      },
      "Next": "PolicySignOff"
    },
    "PolicySignOff": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-south-1:593814964617:function:policy_signoff_lambda",
      "Parameters": {
        "employee_id.$": "$.employee_id"
      },
      "Next": "ManagerIntro"
    },
    "ManagerIntro": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-south-1:593814964617:function:manager_intro_lambda",
      "Parameters": {
        "employee_id.$": "$.employee_id"
      },
      "End": true
    }
  }
}
