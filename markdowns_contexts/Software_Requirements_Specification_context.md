# Work Product Description
## Purpose
### Purpose in ISO26262
The Software Requirements Specification (SRS) in ISO 26262 serves as a critical document that defines the software safety requirements necessary to achieve the overall functional safety objectives of the system. It ensures that all safety-related aspects are considered and addressed in the software design and implementation phases. The SRS is integral to the safety lifecycle, providing traceability from the safety goals and technical safety requirements to the software level. It supports compliance with ISO 26262 by ensuring that the software development process systematically addresses potential hazards and mitigates risks to an acceptable level.
### Purpose in Automotive SPICE
In ASPICE, the Software Requirements Specification (SRS) is essential for supporting process improvement and quality assurance within the software development lifecycle. It provides a detailed description of the software requirements, ensuring that they are complete, consistent, and verifiable. The SRS is closely linked to ASPICE's engineering processes, particularly in the areas of requirements elicitation, analysis, and management. It facilitates effective communication among stakeholders and serves as a foundation for subsequent design, implementation, and testing activities, thereby enhancing the overall quality and reliability of the software product.
## Content
**Software Requirements Specification: Compliance with ISO 26262 and ASPICE**

The Software Requirements Specification (SRS) is a critical work product in the development of automotive systems, ensuring that both functional and non-functional requirements are clearly defined and aligned with safety and quality standards. To achieve compliance with ISO 26262 and ASPICE, the SRS must encompass the following elements:

### 1. **Identification and Documentation of Requirements**
- **Functional and Non-Functional Requirements**: The SRS should comprehensively document both functional and non-functional requirements derived from system requirements and architecture. This includes detailing the software's intended behavior and performance characteristics.
- **Characteristics of Requirements**: Requirements must be verifiable, unambiguous, comprehensible, free from design and implementation constraints, and non-contradictory. These characteristics ensure clarity and facilitate effective communication among stakeholders.

### 2. **Software Safety Requirements**
- **Derivation from Safety Goals**: The SRS must include software safety requirements derived from technical safety requirements. These should address safety-related functionalities and properties that, if unmet, could compromise safety.
- **Consideration of Safety Analyses**: Safety-oriented analyses should be used to identify additional safety requirements and provide evidence of their fulfillment.

### 3. **Structuring and Prioritization**
- **Organizational Structure**: Requirements should be structured hierarchically and organized according to a logical grouping scheme, such as by functionality or product variants. This aids in managing complexity and ensuring completeness.
- **Prioritization**: Requirements should be prioritized based on project or stakeholder needs, which can guide release planning and resource allocation.

### 4. **Specification and Management of Safety Requirements**
- **Attributes of Safety Requirements**: Each safety requirement must have a unique identification, status, and assigned ASIL (Automotive Safety Integrity Level). This ensures traceability and clarity throughout the safety lifecycle.
- **Characteristics of Safety Requirements**: Safety requirements should be unambiguous, comprehensible, atomic, consistent, feasible, verifiable, necessary, implementation-free, complete, and conforming to relevant standards.

### 5. **Interface and Configuration Considerations**
- **Hardware-Software Interface (HSI)**: The SRS should detail the HSI, ensuring that software requirements align with hardware specifications and configurations.
- **External Interfaces and Operating Modes**: Requirements must account for external interfaces and various operating modes, including transitions between modes, to ensure robust system behavior.

### 6. **Maintainability and Consistency**
- **Maintainability**: The SRS should be structured to allow for easy modification and extension, supporting the introduction of new requirements or versions.
- **Consistency**: Both internal and external consistency must be maintained, ensuring that requirements do not contradict themselves or each other.

### 7. **Verification and Validation**
- **Verifiability**: The SRS must include criteria for verifying each requirement, ensuring that they can be tested and validated effectively.
- **Compliance with Standards**: The SRS should conform to applicable automotive industry standards, ensuring that all requirements meet regulatory and safety expectations.

By incorporating these elements, the Software Requirements Specification will meet the compliance and quality expectations set forth by ISO 26262 and ASPICE, ensuring a robust foundation for the development of safe and reliable automotive systems.
## Input
To ensure compliance with ISO 26262 and ASPICE standards for the work product '**Software Requirements Specification**', the following necessary inputs should be considered:

1. **System Requirements and System Architecture**: These serve as the foundational inputs for identifying and documenting both functional and non-functional software requirements. They ensure that the software requirements align with the overall system objectives and architecture, providing a clear context for software development.

2. **Technical Safety Requirements**: Derived from the system's safety goals, these requirements are crucial for identifying software safety requirements. They ensure that the software can handle safety-related functionalities and properties, preventing violations of technical safety requirements.

3. **Hardware-Software Interface (HSI) Specification**: This input is essential for understanding the interaction between hardware and software components. It provides necessary details for defining software requirements that are dependent on hardware interfaces.

4. **Stakeholder Requirements**: These inputs are vital for capturing the needs and expectations of stakeholders, which can influence the prioritization and structuring of software requirements. They ensure that the software meets user and business needs.

5. **Safety-Oriented Analyses**: These analyses help identify additional software safety requirements and provide evidence for their achievement. They ensure that the software requirements address potential safety risks and are robust against failures.

6. **Configuration Parameters and Timing Constraints**: Inputs such as system and hardware configurations, and timing constraints (e.g., execution or reaction times), are necessary for specifying precise software requirements. They ensure that the software operates correctly within defined parameters and timeframes.

7. **External Interfaces and Operating Modes**: Understanding external interfaces (e.g., communication and user interfaces) and operating modes (e.g., normal, degraded, testing) is crucial for defining comprehensive software requirements. These inputs ensure that the software can interact effectively with external systems and adapt to different operational states.

8. **ASIL Decomposition**: If applicable, this input is necessary for managing the allocation of safety integrity levels across software components. It ensures that the software requirements maintain the appropriate safety levels as derived from higher-level safety goals.

9. **Quality Management System Specifications**: For functions beyond those with specified safety requirements, inputs from the quality management system ensure that all software functions are documented and meet quality standards.

These inputs collectively contribute to the compliance of the Software Requirements Specification with ISO 26262 and ASPICE standards by ensuring that the requirements are comprehensive, safety-oriented, and aligned with system-level objectives and constraints.
## Uses
**Use Cases of the Software Requirements Specification (SRS) in ISO 26262 and ASPICE Context**

The Software Requirements Specification (SRS) is a critical work product in the development of automotive systems, serving as a foundational document that outlines the functional and non-functional requirements of the software. Its use cases within the context of ISO 26262 and ASPICE standards are pivotal for ensuring compliance and facilitating effective documentation.

1. **Identification and Documentation of Requirements:**
   - The SRS is used to identify and document both functional and non-functional requirements derived from system requirements and architecture. This aligns with ASPICE's emphasis on using defined characteristics for requirements, such as verifiability, unambiguity, and freedom from design constraints. In ISO 26262, the SRS is crucial for deriving software safety requirements from technical safety requirements, ensuring that safety-related functionalities and properties are adequately captured.

2. **Structuring and Prioritization:**
   - The SRS provides a structured approach to organizing software requirements, which can be grouped by functionality or product variants. Prioritization is also addressed, allowing requirements to be aligned with project or stakeholder needs. This structured approach supports ASPICE's process of managing requirements effectively and ensures that critical safety requirements are prioritized in accordance with ISO 26262.

3. **Specification of Safety Requirements:**
   - In ISO 26262, the SRS is instrumental in specifying software safety requirements, considering factors such as hardware-software interfaces, timing constraints, and operating modes. The document ensures that safety requirements are unambiguously identifiable, inherit the appropriate ASIL (Automotive Safety Integrity Level), and possess characteristics such as feasibility, verifiability, and completeness.

4. **Support for ASIL Decomposition:**
   - The SRS supports the application of ASIL decomposition, as outlined in ISO 26262, by ensuring that safety requirements are appropriately decomposed and managed. This involves maintaining a hierarchical structure and ensuring external consistency and maintainability of the requirements.

5. **Facilitation of Safety Analyses:**
   - The SRS aids in conducting safety-oriented analyses, providing a basis for identifying additional software safety requirements and offering evidence for their achievement. This aligns with ISO 26262's focus on ensuring that software functions and properties do not lead to violations of technical safety requirements.

**Significance in Compliance and Documentation:**

The SRS plays a vital role in achieving compliance with ISO 26262 and ASPICE by serving as a comprehensive documentation of software requirements. It ensures that all requirements are clearly communicated to stakeholders, facilitating their implementation and verification. The SRS also supports traceability, allowing for the tracking of requirements throughout the development lifecycle, which is essential for both standards.

By adhering to the characteristics and attributes outlined in ISO 26262 and ASPICE, the SRS ensures that software requirements are complete, consistent, and aligned with safety goals. This not only aids in compliance but also enhances the quality and reliability of the automotive system being developed.

# Concepts
## Terminology (ISO)
- **architecture:** representation of the structure of the item (3.84) or element (3.41) that allows identification of building blocks, their boundaries and interfaces, and includes the allocation of requirements to these building blocks
- **baseline:** version of the approved set of one or more work products (3.185), items (3.84) or elements (3.41) that serves as a basis for change Note 1 to entry: See ISO 26262-8:2018, Clause 8. Note 2 to entry: A baseline is typically placed under configuration management. Note 3 to entry: A baseline is used as a basis for further development through the change management process during the lifecycle (3.86).
- **confirmation review:** confirmation that a work product provides sufficient and convincing evidence of their contribution to the achievement of functional safety considering the corresponding objectives and requirements of ISO 26262. Note 1 to entry: A complete list of confirmation reviews is given in ISO 26262-2. Note 2 to entry: The goal of confirmation reviews is to ensure compliance with the ISO 26262 series of standards.
- **element:** system (3.163), components (3.21) (hardware or software), hardware parts (3.71), or software units (3.159)
Note 1 to entry: When “software element” or “hardware element” is used, this phrase denotes an element of
software only or an element of hardware only, respectively.
Note 2 to entry: An element may also be a SEooC (3.138).
- **embedded software:** fully-integrated software to be executed on a processing element (3.113)
- **error:** discrepancy between a computed, observed or measured value or condition, and the true, specified or
theoretically correct value or condition
Note 1 to entry: An error can arise as a result of a fault (3.54) within the system (3.163) or component (3.21) being
considered.
- **functional safety concept:** specification of the functional safety requirements (3.69), with associated information, their allocation to elements (3.41) within the architecture (3.1), and their interaction necessary to achieve the safety goals (3.139)
- **functional safety requirement:** specification of implementation-independent safety (3.132) behaviour or implementation-independent safety measure (3.141) including its safety-related attributes
- **inspection:** examination of work products (3.185), following a formal procedure, in order to detect safety anomalies (3.134). Note 1 to entry: Inspection is a means of verification (3.180). Note 2 to entry: Inspection differs from testing (3.169) in that it does not normally involve the operation of the associated item (3.84) or element (3.41). Note 3 to entry: A formal procedure normally includes a previously defined procedure, checklist, moderator and review (3.127) of the results.
- **review:** examination of a work product (3.185), for achievement of its intended work product (3.185) goal, according to the purpose of the review Note 1 to entry: From a development phase (3.110) perspective, verification review (3.181) and confirmation review (3.24).
- **safety anomaly:** conditions that deviate from expectations and that can lead to harm (3.74) Note 1 to entry: Safety anomalies can be discovered, among other times, during the review (3.127), testing (3.169), analysis, compilation, or use of components (3.21) or applicable documentation. EXAMPLE Deviation can be on requirements, specifications, design documents, user documents, standards, or on experience.
- **safety element out of context:** SEooC safety-related element (3.144) which is not developed in the context of a specific item (3.84) Note 1 to entry: A SEooC can be a system (3.163), a combination of systems (3.163), a software component (3.157), a software unit (3.159), a hardware component (3.21) or a hardware part (3.71). EXAMPLE A generic wiper system (3.163) with assumed safety requirements to be integrated in different OEM systems (3.163).
- **software component:** one or more software units (3.159)
- **software unit:** atomic level software component (3.157) of the software architecture (3.1) that can be subjected to stand-alone testing (3.169)
- **statement coverage:** percentage of statements within the software that have been executed
- **technical safety concept:** specification of the technical safety requirements (3.168) and their allocation to system (3.163) elements (3.41) with associated information providing a rationale for functional safety (3.67) at the system (3.163) level
- **technical safety requirement:** requirement derived for implementation of associated functional safety requirements (3.69) Note 1 to entry: The derived requirement includes requirements for mitigation.
- **verification:** determination whether or not an examined object meets its specified requirements EXAMPLE The typical verification activities can be classified as follows: — verification review (3.181), walk-through (3.182), inspection (3.82); — verification testing (3.169); — simulation; — prototyping; and — analysis (safety (3.132) analysis, control flow analysis, data flow analysis, etc.).
- **verification review:** verification (3.180) activity to ensure that the result of a development activity fulfils the project requirements, or technical requirements, or both Note 1 to entry: Individual requirements on verification reviews are given in specific clauses of individual parts of the ISO 26262 series of standards. Note 2 to entry: The goal of verification reviews is technical correctness and completeness of the item (3.84) or element (3.41). EXAMPLE Verification review types can be technical review (3.127), walk-through (3.182) or inspection (3.82).
- **walk-through:** systematic examination of work products (3.185) in order to detect safety anomalies (3.134) Note 1 to entry: Walk-through is a means of verification (3.180). Note 2 to entry: Walk-through differs from testing (3.169) in that it does not normally involve the operation of the associated item (3.84) or element (3.41). Note 3 to entry: Any anomalies that are detected are usually addressed by rework, followed by a walk-through of the reworked work products (3.185). EXAMPLE During a walk-through, the developer explains the work product (3.185) step-by-step to one or more reviewers. The objective is to create a common understanding of the work product (3.185) and to identify any safety anomalies (3.134) within the work product (3.185). Both inspections (3.82) and walk-throughs are types of peer review (3.127), where a walk-through is a less stringent form of peer review (3.127) than an inspection (3.82).
- **work product:** documentation resulting from one or more associated requirements of ISO 26262 Note 1 to entry: The documentation can be in the form of a single document containing the complete information for the work product or a set of documents that together contain the complete information for the work product.

## Abbreviations
- **ASIL:** Automotive Safety Integrity Level (see definition 3.6)
- **COTS:** Commercial Off The Shelf
- **CRC:** Cyclic Redundancy Check
- **DFA:** Dependent Failure Analysis
- **DIA:** Development Interface Agreement (see definition 3.32)
- **DMA:** Direct Memory Access
- **ECC:** Error Correction Code
- **ECU:** Electronic Control Unit
- **EDC:** Error Detection Code
- **E/E:** system Electrical and/or Electronic system (see definition 3.40)
- **EMC:** ElectroMagnetic Compatibility
- **EMI:** ElectroMagnetic Interference
- **EOTI:** Emergency Operation Time Interval (see definition 3.44)
- **EOTTI:** Emergency Operation Tolerance Time Interval (see definition 3.45)
- **ESD:** ElectroStatic Discharge
- **ESC:** Electronic Stability Control
- **ETA:** Event Tree Analysis
- **EVR:** Embedded Voltage Regulator
- **FDTI:** Fault Detection Time Interval (see definition 3.55)
- **FET:** Field Effect Transistor
- **FMEA:** Failure Mode and Effects Analysis
- **FTA:** Fault Tree Analysis
- **HARA:** Hazard Analysis and Risk Assessment
- **HSI:** Hardware-Software Interface
- **I/O:** Input – Output
- **MBD:** Model Based Development
- **MC/DC:** Modified Condition/Decision Coverage
- **OEM:** Original Equipment Manufacturer
- **OS:** Operating System
- **QM:** Quality Management
- **RFQ:** Request For Quotation
- **SEooC:** Safety Element out of Context (see definition 3.138)
- **SG:** Safety Goal (see definition 3.139)
- **SW:** SoftWare
- **TCL:** Tool Confidence Level
- **UML:** Unified Modeling Language
- **XML:** eXtensible Markup Language

## Disambiguation
**Software architecture specification**
- **Definition:** work product
- **Purpose:** specifying aspects of architecture for the software
- **Examples:** nan
- **Elements:** Software architectural elements
- **Example Elements:** software system, software sub-system, software composition, software component
- **Terminology (ISO 26262):** Software architecture; safety architecture
- **Terminology (ASPICE):** Software architecture specification

**Software component**
- **Definition:** element
- **Purpose:** determining the leaf elements of the hierarchical decomposition of the software
- **Examples:** nan
- **Elements:** Software detailed design elements
- **Example Elements:** nan
- **Terminology (ISO 26262):** Software unit; atomic software component
- **Terminology (ASPICE):** Software component

**Software detailed design**
- **Definition:** work product
- **Purpose:** specifying aspects of design below the level of abstraction represented by software arcihtectural design
- **Examples:** nan
- **Elements:** Software detailed design specification
- **Example Elements:** nan
- **Terminology (ISO 26262):** Software detailed design
- **Terminology (ASPICE):** Software detailed design

**Baseline**
- **Definition:** work product
- **Purpose:** freezing all development artefacts at a given moment in time in order to be able to re-establish this state of development in the future
- **Examples:** -
- **Elements:** All workproducts which are subject to beaselining
- **Example Elements:** Test reports, software architecture specification, software requirements specification, source code, product quality report
- **Terminology (ISO 26262):** Baseline
- **Terminology (ASPICE):** Baseline

**Work product review**
- **Definition:** process element
- **Purpose:** providing quality indicators for the product.
- **Examples:** document reviews, specification reviews, code reviews
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Safety assessment; software verification report; confirmation review
- **Terminology (ASPICE):** Verification results

**Review checklist**
- **Definition:** process element
- **Purpose:** providing a list of pre-defined quality criteria for work product reviews.
- **Examples:** configuration management plan review checklist, pull request review checklist, code inspection checklist, requirements review checklist
- **Elements:** quality criteria
- **Example Elements:** -
- **Terminology (ISO 26262):** nan
- **Terminology (ASPICE):** nan

**Review report**
- **Definition:** work product
- **Purpose:** determining the quality status of a work product based on a review checklist
- **Examples:** configuration management plan review report, pull request review report, code inspection report, requirements review report
- **Elements:** Assessed quality criteria for the work product under review (=answered checklist questions)
- **Example Elements:** nan
- **Terminology (ISO 26262):** Confirmation measure results (excluding safety audit results)
- **Terminology (ASPICE):** Review evidence

**Corrective action**
- **Definition:** work product
- **Purpose:** orchestrating mitigations to process or product related defects found.
- **Examples:** improvement measures for assessment findings, mitigation measures to safety anomalies
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** nan
- **Terminology (ASPICE):** Corrective action

**Requirements specification**
- **Definition:** work product
- **Purpose:** specifying requirements the software must fulfill.
- **Examples:** Specification books, Lastenheft, Functional Safety Concept, Technical Safety Concept, Requirements clusters, Software features
- **Elements:** requirements
- **Example Elements:** functional safety requirements, software requirements, system requirements, assumptions of use, non-functional requirements, special characteristics
- **Terminology (ISO 26262):** Functional safety requirements
- **Terminology (ASPICE):** System requirements; software requirements

**Software features**
- **Definition:** process element
- **Purpose:** defining clusters of related software requirements whose implementation can be terminated at specific release milestones.
- **Examples:** -
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Feature
- **Terminology (ASPICE):** Feature

**Review method**
- **Definition:** process element
- **Purpose:** defining useful approaches for different types of reviews or review goals.
- **Examples:** walk-through, inspection, peer review, expert review
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** -
- **Terminology (ASPICE):** Review method

**Risk and opportunity overview**
- **Definition:** work product
- **Purpose:** providing a basis for mitigating known risks and facilitating known opportunities.
- **Examples:** -
- **Elements:** risks, opportunities
- **Example Elements:** -
- **Terminology (ISO 26262):** Risk
- **Terminology (ASPICE):** Improvement opportunity; risk
