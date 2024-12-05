# Work Product Description
## Purpose
### Purpose in ISO26262
The Software Architecture Specification in ISO 26262 serves as a critical document to ensure that the software design meets the functional safety requirements. It provides a detailed description of the software components, their interactions, and interfaces, ensuring traceability to safety requirements. This work product is essential for achieving functional safety objectives as it helps in identifying potential safety risks and implementing necessary safety mechanisms. It aligns with ISO 26262 processes by supporting the verification and validation of the software design against safety goals, thus ensuring compliance with the standard's guidelines for developing safety-critical automotive systems.
### Purpose in Automotive SPICE
In ASPICE, the Software Architecture Specification is a key work product that supports process improvement and quality assurance in software development. It defines the structure of the software system, detailing components, interfaces, and their interactions, which is crucial for systematic software engineering. This specification aids in ensuring that the software architecture is robust, maintainable, and scalable, aligning with ASPICE's engineering processes. It also facilitates effective communication among stakeholders and supports the management processes by providing a clear blueprint for software development, thus enhancing overall project quality and efficiency.
## Content
**Software Architecture Specification: Compliance with ISO 26262 and ASPICE**

The Software Architecture Specification is a critical work product in the development of automotive systems, ensuring that both functional and non-functional requirements are met while adhering to safety and quality standards. To achieve compliance with ISO 26262 and ASPICE, the specification must encompass several key elements and characteristics, as outlined below:

1. **Static Aspects of Software Architecture:**
   - **Software Structure:** Clearly define the hierarchical levels of the software, including the organization of software components and their interfaces. This should include data types, global variables, and external dependencies.
   - **External Interfaces:** Document the interfaces of software components and the embedded software, ensuring clarity in communication with external systems.
   - **Constraints:** Identify any constraints related to the architecture, such as scope limitations and dependencies.

2. **Dynamic Aspects of Software Architecture:**
   - **Behavioral Description:** Provide a detailed description of the software components' behavior, including functional chains of events, logical data processing sequences, and control flow.
   - **Concurrency and Interaction:** Address concurrency aspects such as interrupt handling, multi-threading, and the interaction of software components in various modes.
   - **Temporal Constraints:** Specify temporal constraints, including timing requirements for tasks, time slices, and interrupts.

3. **Architectural Characteristics:**
   - **Comprehensibility and Consistency:** Ensure the architecture is easily understandable and consistent across all components and interfaces.
   - **Simplicity and Modularity:** Design the architecture to be simple and modular, facilitating easier maintenance and updates.
   - **Verifiability and Testability:** The architecture should be verifiable and testable, with bi-directional traceability to software safety requirements.
   - **Encapsulation and Abstraction:** Use encapsulation to protect data and abstraction to manage complexity, employing hierarchical structures and views.

4. **Safety Mechanisms:**
   - **Error Detection and Handling:** Implement safety mechanisms for error detection, such as range checks and plausibility checks, and error handling strategies like deactivation and recovery mechanisms.
   - **Resource Estimation:** Provide an upper estimation of required resources, including execution time, storage space, and communication resources.

5. **Partitioning and ASIL Considerations:**
   - **Software Partitioning:** If applicable, ensure freedom from interference between software components through effective partitioning, supported by hardware features or equivalent means.
   - **ASIL Compliance:** Treat all embedded software according to the highest ASIL level unless criteria for coexistence are met.

6. **Maintainability and Configurability:**
   - **Maintainability:** Design the architecture to be maintainable, allowing for future modifications and enhancements.
   - **Configurable Software:** Consider the suitability of the architecture for configurable software, ensuring flexibility in design and implementation.

By incorporating these elements into the Software Architecture Specification, the work product will align with the requirements of ISO 26262 and ASPICE, ensuring a robust, safe, and high-quality automotive system. This comprehensive approach not only addresses safety and compliance but also supports the overall development process by providing a clear and structured architectural framework.
## Input
To ensure compliance with ISO 26262 and ASPICE standards for the work product '**Software Architecture Specification**', the following inputs are necessary:

1. **Functional and Non-Functional Requirements**: 
   - Inputs should include detailed functional and non-functional requirements to ensure that the software architecture addresses all necessary aspects, such as performance, reliability, and safety. This aligns with ASPICE's emphasis on documenting both static and dynamic aspects of the architecture.

2. **Hardware-Software Interface (HSI) Definition**:
   - A clear definition of the HSI is crucial to contextualize the software architecture within the system design. This input ensures that the architecture is compatible with the hardware, as required by ASPICE.

3. **Safety Requirements and Analysis Results**:
   - Safety requirements derived from ISO 26262 should be included to guide the architectural design in implementing necessary safety mechanisms. Results from safety-oriented analyses should inform the architecture to incorporate error detection and handling mechanisms.

4. **Resource Estimations**:
   - Inputs should include estimations of required resources such as execution time, storage space, and communication resources. This ensures that the architecture is feasible and efficient, as mandated by ISO 26262.

5. **Traceability Information**:
   - Bi-directional traceability between software architecture and safety requirements is essential. This input supports verifiability and maintainability, ensuring that all safety requirements are addressed in the architecture.

6. **Modularity and Encapsulation Guidelines**:
   - Inputs should provide guidelines on modularity and encapsulation to ensure the architecture is comprehensible, consistent, and maintainable. This aligns with ISO 26262's emphasis on these characteristics to avoid systematic faults.

7. **Partitioning and ASIL Considerations**:
   - If applicable, inputs should include partitioning strategies and ASIL considerations to ensure freedom from interference and appropriate handling of mixed ASIL components. This is crucial for maintaining safety integrity levels as per ISO 26262.

8. **Dynamic Behavior and Concurrency Aspects**:
   - Inputs should describe the expected dynamic behavior and concurrency aspects, such as interrupt handling and multi-threading. This ensures that the architecture can handle different software modes and interactions effectively, as required by ASPICE.

9. **Verification and Testability Criteria**:
   - Inputs should include criteria for verifying the architecture and ensuring its testability during integration testing. This supports the ISO 26262 requirement for verifiability and ASPICE's focus on dynamic aspects.

By incorporating these inputs, the Software Architecture Specification will be well-positioned to meet the compliance requirements of both ISO 26262 and ASPICE, ensuring a robust and safe software design.
## Uses
The **Software Architecture Specification** is a critical work product in the context of ISO 26262 and ASPICE standards, serving multiple use cases that ensure compliance and facilitate documentation in automotive software development.

### Primary Use Cases:

1. **Static and Dynamic Design Documentation:**
   - The specification documents both static and dynamic aspects of the software architecture. This includes defining software components, their interfaces, and relationships, as well as the behavior and interaction of these components in various modes. This comprehensive documentation supports ASPICE requirements for specifying software architecture.

2. **Safety and Error Handling:**
   - It addresses safety mechanisms for error detection and handling, which are crucial for ISO 26262 compliance. This includes implementing range checks, plausibility checks, and monitoring mechanisms to ensure the software can handle errors effectively and maintain safety.

3. **Resource Estimation:**
   - The specification provides an upper estimation of required resources such as execution time, storage space, and communication resources. This is essential for planning and ensuring that the software can operate within the constraints of the embedded system, aligning with ISO 26262 requirements.

4. **Modularity and Maintainability:**
   - By emphasizing modularity, encapsulation, and maintainability, the specification ensures that the software architecture is comprehensible, consistent, and simple. These characteristics are vital for avoiding systematic faults and are mandated by ISO 26262.

5. **Partitioning and ASIL Management:**
   - The specification supports the implementation of software partitioning to ensure freedom from interference between components of different ASILs. This is crucial for managing safety-related and non-safety-related components within the same system, as required by ISO 26262.

### Support for Documentation and Compliance:

- **Traceability and Verifiability:**
  - The specification ensures bi-directional traceability between software architecture and safety requirements, facilitating verifiability and testability during integration testing. This traceability is a key aspect of both ISO 26262 and ASPICE compliance.

- **Comprehensive Design Characteristics:**
  - It addresses essential design characteristics such as comprehensibility, consistency, simplicity, and abstraction, which are necessary for a robust architectural design. These characteristics support the ISO 26262 goal of avoiding systematic faults.

- **Integration with System Design:**
  - The specification includes the hardware-software interface (HSI) definition, which integrates with system design activities. This alignment with system-level design is crucial for ASPICE compliance and ensures that software architecture is developed in context with the overall system.

In summary, the **Software Architecture Specification** is a foundational document that supports compliance with ISO 26262 and ASPICE by providing detailed documentation of software architecture, ensuring safety and error handling, managing resources, and maintaining modularity and traceability. Its role is pivotal in achieving a safe, reliable, and maintainable automotive software system.

# Concepts
## Terminology (ISO)
- **architecture:** representation of the structure of the item (3.84) or element (3.41) that allows identification of building blocks, their boundaries and interfaces, and includes the allocation of requirements to these building blocks
- **baseline:** version of the approved set of one or more work products (3.185), items (3.84) or elements (3.41) that serves as a basis for change. A baseline is typically placed under configuration management and is used as a basis for further development through the change management process during the lifecycle (3.86).
- **component:** non-system level element (3.41) that is logically or technically separable and is comprised of more than one hardware part (3.71) or one or more software units (3.159) EXAMPLE A microcontroller. Note 1 to entry: A component is a part of a system (3.163).
- **configuration data:** data that is assigned during element build and that controls the element build process EXAMPLE 1 Pre-processor variable settings which are used to derive compile time variants from the source code. EXAMPLE 2 XML files to control the build tools or toolchain. Note 1 to entry: Configuration data controls the software build. Configuration data is used to select code from existing code variants already defined in the code base. The functionality of selected code variant will be included in the executable code. Note 2 to entry: Since configuration data is only used to select code variants, configuration data does not include code that is executed or interpreted during the use of the item (3.84).
- **element:** system (3.163), components (3.21) (hardware or software), hardware parts (3.71), or software units (3.159)
Note 1 to entry: When “software element” or “hardware element” is used, this phrase denotes an element of
software only or an element of hardware only, respectively.
Note 2 to entry: An element may also be a SEooC (3.138).
- **embedded software:** fully-integrated software to be executed on a processing element (3.113)
- **functional safety concept:** specification of the functional safety requirements (3.69), with associated information, their allocation to elements (3.41) within the architecture (3.1), and their interaction necessary to achieve the safety goals (3.139)
- **functional safety requirement:** specification of implementation-independent safety (3.132) behaviour or implementation-independent safety measure (3.141) including its safety-related attributes Note 1 to entry: A functional safety requirement can be a safety (3.132) requirement implemented by a safety-related E/E system (3.40), or by a safety-related system (3.163) of other technologies (3.105), in order to achieve or maintain a safe state (3.131) for the item (3.84) taking into account a determined hazardous event (3.77). Note 2 to entry: The functional safety requirements might be specified independently of the technology used in the concept phase (3.110) of product development. Note 3 to entry: Safety-related attributes include information about the ASIL (3.6).
- **inspection:** examination of work products, following a formal procedure, in order to detect safety anomalies. Note: Inspection is a means of verification and differs from testing in that it does not normally involve the operation of the associated item or element. A formal procedure normally includes a previously defined procedure, checklist, moderator and review of the results.
- **review:** examination of a work product (3.185), for achievement of its intended work product (3.185) goal, according to the purpose of the review Note 1 to entry: From a development phase (3.110) perspective, verification review (3.181) and confirmation review (3.24).
- **safety architecture:** set of elements (3.41) and their interaction to fulfil the safety (3.132) requirements
- **software component:** one or more software units (3.159)
- **software unit:** atomic level software component (3.157) of the software architecture (3.1) that can be subjected to stand-alone testing (3.169)
- **verification:** determination whether or not an examined object meets its specified requirements EXAMPLE The typical verification activities can be classified as follows: — verification review (3.181), walk-through (3.182), inspection (3.82); — verification testing (3.169); — simulation; — prototyping; and — analysis (safety (3.132) analysis, control flow analysis, data flow analysis, etc.).
- **verification review:** verification (3.180) activity to ensure that the result of a development activity fulfils the project requirements, or technical requirements, or both Note 1 to entry: Individual requirements on verification reviews are given in specific clauses of individual parts of the ISO 26262 series of standards. Note 2 to entry: The goal of verification reviews is technical correctness and completeness of the item (3.84) or element (3.41). EXAMPLE Verification review types can be technical review (3.127), walk-through (3.182) or inspection (3.82).
- **walk-through:** systematic examination of work products (3.185) in order to detect safety anomalies (3.134) Note 1 to entry: Walk-through is a means of verification (3.180). Note 2 to entry: Walk-through differs from testing (3.169) in that it does not normally involve the operation of the associated item (3.84) or element (3.41). Note 3 to entry: Any anomalies that are detected are usually addressed by rework, followed by a walk-through of the reworked work products (3.185). EXAMPLE During a walk-through, the developer explains the work product (3.185) step-by-step to one or more reviewers. The objective is to create a common understanding of the work product (3.185) and to identify any safety anomalies (3.134) within the work product (3.185). Both inspections (3.82) and walk-throughs are types of peer review (3.127), where a walk-through is a less stringent form of peer review (3.127) than an inspection (3.82).
- **work product:** documentation resulting from one or more associated requirements of ISO 26262 Note 1 to entry: The documentation can be in the form of a single document containing the complete information for the work product or a set of documents that together contain the complete information for the work product.

## Abbreviations
- **ASIC:** Application-Specific Integrated Circuit
- **ASIL:** Automotive Safety Integrity Level (see definition 3.6)
- **CAN:** Controller Area Network
- **COTS:** Commercial Off The Shelf
- **CPU:** Central Processing Unit
- **CRC:** Cyclic Redundancy Check
- **DIA:** Development Interface Agreement (see definition 3.32)
- **DMA:** Direct Memory Access
- **DSP:** Digital Signal Processor
- **ECC:** Error Correction Code
- **ECU:** Electronic Control Unit
- **EDC:** Error Detection Code
- **E/E:** system Electrical and/or Electronic system (see definition 3.40)
- **EMC:** ElectroMagnetic Compatibility
- **EMI:** ElectroMagnetic Interference
- **ESD:** ElectroStatic Discharge
- **ETA:** Event Tree Analysis
- **FDTI:** Fault Detection Time Interval (see definition 3.55)
- **FMEA:** Failure Mode and Effects Analysis
- **FTA:** Fault Tree Analysis
- **HARA:** Hazard Analysis and Risk Assessment (see definition 3.76)
- **HSI:** Hardware-Software Interface
- **HW:** HardWare
- **I/O:** Input – Output
- **ISA:** Instruction Set Architecture
- **MBD:** Model Based Development
- **MC/DC:** Modified Condition/Decision Coverage (see definition 3.92)
- **MMU:** Memory Management Unit
- **MPU:** Memory Protection Unit
- **OEM:** Original Equipment Manufacturer
- **OS:** Operating System
- **QM:** Quality Management
- **RAM:** Random Access Memory
- **ROM:** Read Only Memory
- **RTL:** Register Transfer Level
- **SEooC:** Safety Element out of Context (see definition 3.138)
- **SW:** SoftWare
- **SoC:** System on Chip
- **SPI:** Serial Peripheral Interface
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

**Process objective**
- **Definition:** process element
- **Purpose:** providing high-level goals to be achieved in each process area
- **Examples:** to develop a software architectural design which satisfies the software requirements, higher level architectural design (e.g., system level) and which identifies the elements of the software and their interfaces.
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Objective
- **Terminology (ASPICE):** Process outcome

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

**Process audit**
- **Definition:** process element
- **Purpose:** providing quality indicators for the applied processes.
- **Examples:** safety audit, configuration management audit, software testing audit
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Safety audit
- **Terminology (ASPICE):** Assessment; internal audit

**Review report**
- **Definition:** work product
- **Purpose:** determining the quality status of a work product based on a review checklist
- **Examples:** configuration management plan review report, pull request review report, code inspection report, requirements review report
- **Elements:** Assessed quality criteria for the work product under review (=answered checklist questions)
- **Example Elements:** nan
- **Terminology (ISO 26262):** Confirmation measure results (excluding safety audit results)
- **Terminology (ASPICE):** Review evidence

**Audit report**
- **Definition:** work product
- **Purpose:** determining the quality status of process application in a development project based on an audit checklist
- **Examples:** configuration management audit report, software development audit report, software testing audit report
- **Elements:** Assessed quality criteria for process application (=answered checklist questions)
- **Example Elements:** nan
- **Terminology (ISO 26262):** Safety audit results
- **Terminology (ASPICE):** Audit report; assessment report

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
