# Ubuntu STIG Checker

## Description

Ubuntu STIG Checker is a software tool for automated verification of the Ubuntu operating system for compliance with STIG security requirements (Security Technical Implementation Guide).

The project is implemented in Python and uses an architectural approach based on the principles of the RQCODE framework. The main purpose of the system is to automate the verification of the operating system configuration, identify security violations, and attempt to automatically correct detected inconsistencies.

---

## Main features

* Automatic verification of STIG requirements.
* Automatic correction of supported violations.
* Generating a report on the audit results.
* Support for system expansion by adding new STIG controls.
* Using an object-oriented architecture and reusable validation components.

---

## System architecture

The system is based on the principle:

```text
STIG
  ↓
Verification
  ↓
PASS ? ───────────────► Report
  ↓ NO
Remediation
  ↓
Verification
  ↓
Report
```

Each security control is represented by a separate STIG class.

All STIGs are inherited from specialized verification components that contain common control logic.

---

## Project structure

```text
security_requirements_in_python/

├── main.py
├── report.py
│
├── core/
│   ├── requirement.py
│   ├── result.py
│   ├── registry.py
│   ├── engine.py
│   │
│   └── requirements/
│       ├── file_permission.py
│       ├── file_owner.py
│       ├── file_group.py
│       ├── package_installed.py
│       ├── account_policy.py
│       ├── identity_uniqueness.py
│       └── required_file.py
│
├── stigs/
│   ├── ubtu_22_232030.py
│   ├── ubtu_22_232135.py
│   ├── ubtu_22_232140.py
│   ├── ...
│
└── reports/
```

---

## The principle of operation

### 1. STIG Registration

Each STIG is automatically logged into the system through the decorator:

```python
@register
class UBTU22232030(
    FilePermissionRequirement
):
    ...
```

After launching the application, all registered STIGs are loaded into the execution engine.

---

### 2. Performing verification

The execution engine (`ExecutionEngine`) performs the following actions sequentially:

1. Runs the `verify()` method.
2. If the check is successful:
   * The result is marked as a `PASS'.

3. If the verification is unsuccessful:
   * The `remediate()` method is running.

4. After the correction, `verify()` is executed again.
5. The final result is formed.

---

### 3. Report generation

After the verification is completed, a JSON report is created in the `reports` directory.

Example:

```json
{
    "stig_id": "UBTU-22-232030",
    "status": "PASS",
    "severity": "MEDIUM",
    "remediation_attempted": false,
    "final_result": true
}
```

---

## Basic types of requirements

Reusable requirements components are used to reduce code duplication.

### AccountPolicyRequirement

Checks account settings and password policies.

Used for:

* UBTU-22-411035
* UBTU-22-412015
* UBTU-22-412020
* UBTU-22-412025

---

### FileGroupRequirement

Checks the file group.

Used for:

* UBTU-22-232135
* UBTU-22-232170
* UBTU-22-232185

---

### FileOwnerRequirement

Checks the file owner.

Used for:

* UBTU-22-232140
* UBTU-22-611010
* UBTU-22-611020

---

### FilePermissionRequirement

Checks access rights to the file.

Used for:

* UBTU-22-232030
* UBTU-22-232035
* UBTU-22-612020
* UBTU-22-612010

---

### IdentityUniquenessRequirement

Checks the uniqueness of user and group IDs.

Used for:

* UBTU-22-411015
* UBTU-22-411020
* UBTU-22-411025
* UBTU-22-411030

---

### PackageInstalledRequirement

Checks for the installed software package.

Used for:

* UBTU-22-232150

---

### RequiredFileRequirement

Checks for required configuration files.

Used for:

* UBTU-22-412000
* UBTU-22-412005
* UBTU-22-412010
* UBTU-22-232155
* UBTU-22-232160

---

### TMOUTRequirement

Checks for required configuration files.

Used for:

* UBTU-22-412030

---

## Starting the system

To run the check:

1. If you run it without 'sudo', the check will pass **without corrections in the system**, however, some checks **may return an ERROR message**, since some STIGS also require a certain permission to check.

```bash
python3 main.py
```
2. Checks the system and tries to fix all errors if necessary.

```bash
sudo python3 main.py
```

After the verification is completed, the report will be saved in the directory (An example report is attached to the 'reports' folder):

```text
reports/
```

---

## Sample report

Brief information is displayed in the console:

```text
UBTU-22-232030 -> PASS
UBTU-22-232135 -> PASS
UBTU-22-232140 -> FAIL
UBTU-22-411015 -> ERROR
```

Detailed information is saved in the JSON file of the report to the 'reports' folder.

---

## Used technologies

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* pathlib
* os
* pwd
* grp
