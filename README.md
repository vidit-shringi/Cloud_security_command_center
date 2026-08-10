<div align="center">

<img src="assets/internshield-iam-banner.png" alt="InternShield AI-Powered IAM Security Auditor" width="100%">

# InternShield AI-Powered IAM Privilege Escalation Risk Auditor

### AWS IAM Security Assessment • Policy Analysis • AI-Assisted Troubleshooting

**Identify • Analyze • Understand • Secure**

[![AWS](https://img.shields.io/badge/AWS-IAM-orange?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/iam/)
[![Bash](https://img.shields.io/badge/Bash-Linux-black?style=for-the-badge&logo=gnubash)](https://www.gnu.org/software/bash/)
[![AWS CLI](https://img.shields.io/badge/AWS%20CLI-Security-blue?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/cli/)
[![AI](https://img.shields.io/badge/AI-Shell--GPT-purple?style=for-the-badge)](#ai-assisted-analysis)
[![Security](https://img.shields.io/badge/Focus-IAM%20Security-red?style=for-the-badge)](#security-model)

**Developed by Vidit Shringi | InternShield**

</div>

---

## About

**InternShield AI-Powered IAM Privilege Escalation Risk Auditor** is a
Linux-based security assessment utility designed to analyze AWS IAM
configurations and identify potentially dangerous permission patterns.

The tool combines traditional AWS security analysis with
AI-assisted troubleshooting to help security learners,
cloud engineers, and security professionals understand IAM
configuration risks.

```text
                 AWS ACCOUNT
                     │
                     ▼
              ┌──────────────┐
              │ AWS Identity  │
              │ Verification  │
              └───────┬──────┘
                      │
                      ▼
              ┌──────────────┐
              │ IAM Users    │
              │ Enumeration  │
              └───────┬──────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
      Managed Policies    Inline Policies
             │                 │
             └────────┬────────┘
                      ▼
              ┌──────────────┐
              │ Risk Pattern │
              │   Analysis   │
              └───────┬──────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
        Security Finding   Shell-GPT
                              │
                              ▼
                       AI Explanation
                              │
                              ▼
                    Analyst Verification
