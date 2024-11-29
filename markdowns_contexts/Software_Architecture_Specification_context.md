# Work Product Description
## Purpose
### Purpose in ISO26262
The Software Architecture Specification in ISO 26262 serves to define the software components and their interactions within the system, ensuring that safety requirements are met. It provides a structured framework to identify potential hazards and implement safety mechanisms, supporting the overall safety case for the system.
### Purpose in Automotive SPICE
In ASPICE, the Software Architecture Specification outlines the high-level design of the software, detailing the structure and interaction of software components. It ensures that the software design aligns with the system requirements and supports traceability, verification, and validation activities, contributing to the overall quality and reliability of the software product.
## Content
To comply with ISO 26262 and ASPICE standards, the 'Software Architecture Specification' should include the following key content:

1. **Static Aspects**: Document the static aspects of the software architecture, including the software structure, hierarchical levels, data types, external interfaces, global variables, and constraints. This should align with both functional and non-functional requirements.

2. **Dynamic Aspects**: Specify the dynamic aspects, such as the behavior of software components, their interactions in different modes, control flow, concurrency, and data flow through interfaces. Use appropriate notations like SysML or UML for clarity.

3. **Architectural Characteristics**: Ensure the architecture is comprehensible, consistent, simple, verifiable, modular, abstract, encapsulated, and maintainable. These characteristics help avoid systematic faults and support future development activities.

4. **Safety Mechanisms**: Incorporate safety mechanisms for error detection and handling, such as range checks, plausibility checks, monitoring of program execution, and redundancy. These mechanisms should be reviewed at the system level for consistency with safety requirements.

5. **Resource Estimation**: Provide an upper estimation of required resources, including execution time, storage space (RAM and ROM), and communication resources.

6. **Partitioning and ASIL Considerations**: If the software includes components of different ASILs or both safety-related and non-safety-related components, treat all software according to the highest ASIL unless criteria for coexistence are met. Ensure freedom from interference through software partitioning, supported by hardware features if necessary.

7. **Traceability and Testability**: Ensure bi-directional traceability between the software architecture and safety requirements. The architecture should be testable during integration testing and maintainable for future updates.

8. **Software Units Identification**: Develop the architecture down to the level where software units are clearly identified, ensuring clarity and precision in the design.

By addressing these elements, the 'Software Architecture Specification' will align with the requirements of ISO 26262 and ASPICE, ensuring a robust and compliant software development process.
## Input
To ensure compliance of the 'Software Architecture Specification' with ISO 26262 and ASPICE standards, the following key requirements and necessary inputs should be addressed:

1. **Static and Dynamic Aspects**:
   - Document both static and dynamic aspects of the software architecture. This includes defining software components, their interfaces, relationships, and behavior in different modes. Ensure that concurrency aspects like interrupt handling and multi-threading are considered.

2. **Characteristics of Software Architecture**:
   - Ensure the architecture is comprehensible, consistent, simple, verifiable, modular, abstract, encapsulated, and maintainable. Use hierarchical structures and grouping schemes to support abstraction.

3. **Safety Mechanisms**:
   - Implement safety mechanisms for error detection and handling, such as range checks, plausibility checks, and monitoring of program execution. Consider mechanisms like deactivation, recovery, and redundancy to maintain safety.

4. **Resource Estimation**:
   - Provide an upper estimation of required resources, including execution time, storage space (RAM, ROM), and communication resources.

5. **Traceability and Testability**:
   - Ensure bi-directional traceability between the software architecture and safety requirements. The architecture should be testable during integration testing and maintainable.

6. **Software Units Identification**:
   - Develop the architecture down to the level where software units are identified, ensuring clarity in the software structure and data types.

7. **Partitioning and ASIL Compliance**:
   - If different ASILs or safety-related and non-safety-related components coexist, treat all software according to the highest ASIL unless criteria for coexistence are met. Ensure freedom from interference through software partitioning, supported by hardware features if necessary.

8. **Inputs for Specification**:
   - Inputs should include functional and non-functional requirements, safety analyses results, resource constraints, and system-level requirements. Ensure that the architecture aligns with these inputs to support the overall system design and safety goals.

By addressing these requirements and inputs, the 'Software Architecture Specification' will align with ISO 26262 and ASPICE standards, ensuring a robust and compliant software development process.
## Uses
The 'Software Architecture Specification' is a critical work product in both ISO 26262 and ASPICE frameworks, serving several key use cases in the development of automotive systems:

1. **Static and Dynamic Aspects Documentation**: It specifies and documents both the static and dynamic aspects of the software architecture. This includes defining software components, their interfaces, relationships, and behavior in different modes, which is essential for understanding how the software will function and interact with other system components.

2. **Safety and Error Handling**: The specification addresses safety mechanisms for error detection and handling, ensuring that potential faults are managed effectively. This includes implementing range checks, plausibility checks, and monitoring program execution, which are crucial for maintaining system safety and reliability.

3. **Resource Estimation**: It provides an upper estimation of required resources such as execution time, storage space, and communication resources. This helps in planning and optimizing the use of system resources, ensuring that the software can operate efficiently within the hardware constraints.

4. **Architectural Characteristics**: The specification ensures that the software architecture exhibits characteristics like comprehensibility, consistency, simplicity, verifiability, modularity, encapsulation, and maintainability. These characteristics help in avoiding systematic faults and facilitate easier maintenance and updates.

5. **Partitioning and ASIL Management**: It addresses the implementation of software components with different Automotive Safety Integrity Levels (ASILs) and ensures freedom from interference through software partitioning. This is vital for managing safety-related and non-safety-related components within the same system.

6. **Traceability and Testability**: The specification emphasizes the importance of traceability between the software architecture and safety requirements, as well as the testability of the architecture during integration testing. This ensures that all safety requirements are met and that the architecture can be effectively tested for compliance.

Overall, the 'Software Architecture Specification' aids in comprehensive documentation, ensuring that all aspects of the software architecture are well-defined, safe, and aligned with both functional and non-functional requirements. This documentation is crucial for achieving compliance with ISO 26262 and ASPICE standards, ultimately contributing to the development of safe and reliable automotive systems.

# Concepts
## Terminology (ISO)
- **architecture:** representation of the structure of the item or element that allows identification of building blocks, their boundaries and interfaces, and includes the allocation of requirements to these building blocks
- **baseline:** version of the approved set of one or more work products, items or elements that serves as a basis for change. A baseline is typically placed under configuration management. A baseline is used as a basis for further development through the change management process during the lifecycle.
- **component:** non-system level element that is logically or technically separable and is comprised of more than one hardware part or one or more software units. EXAMPLE A microcontroller. Note: A component is a part of a system.
- **confirmation review:** confirmation that a work product provides sufficient and convincing evidence of their contribution to the achievement of functional safety considering the corresponding objectives and requirements of ISO 26262. Note: The goal of confirmation reviews is to ensure compliance with the ISO 26262 series of standards.
- **element:** system (3.163), components (3.21) (hardware or software), hardware parts (3.71), or software units (3.159) Note 1 to entry: When “software element” or “hardware element” is used, this phrase denotes an element of software only or an element of hardware only, respectively. Note 2 to entry: An element may also be a SEooC (3.138).
- **embedded software:** fully-integrated software to be executed on a processing element (3.113)
- **functional safety concept:** specification of the functional safety requirements, with associated information, their allocation to elements within the architecture, and their interaction necessary to achieve the safety goals.
- **inspection:** examination of work products, following a formal procedure, in order to detect safety anomalies. Inspection is a means of verification. Inspection differs from testing in that it does not normally involve the operation of the associated item or element. A formal procedure normally includes a previously defined procedure, checklist, moderator and review of the results.
- **review:** examination of a work product, for achievement of its intended work product goal, according to the purpose of the review Note 1 to entry: From a development phase perspective, verification review and confirmation review.
- **safety architecture:** set of elements and their interaction to fulfil the safety requirements
- **software component:** one or more software units (3.159)
- **software unit:** atomic level software component of the software architecture that can be subjected to stand-alone testing
- **work product:** documentation resulting from one or more associated requirements of ISO 26262 Note 1 to entry: The documentation can be in the form of a single document containing the complete information for the work product or a set of documents that together contain the complete information for the work product.

## Abbreviations
- **ALU:** Arithmetic Logic Unit
- **ASIC:** Application-Specific Integrated Circuit
- **ASIL:** Automotive Safety Integrity Level
- **CAN:** Controller Area Network
- **COTS:** Commercial Off The Shelf
- **CPU:** Central Processing Unit
- **CRC:** Cyclic Redundancy Check
- **DMA:** Direct Memory Access
- **DSP:** Digital Signal Processor
- **ECC:** Error Correction Code
- **ECU:** Electronic Control Unit
- **EDC:** Error Detection Code
- **E/E:** system Electrical and/or Electronic system
- **EMC:** ElectroMagnetic Compatibility
- **EMI:** ElectroMagnetic Interference
- **ESD:** ElectroStatic Discharge
- **ETA:** Event Tree Analysis
- **EVR:** Embedded Voltage Regulator
- **FET:** Field Effect Transistor
- **FMEA:** Failure Mode and Effects Analysis
- **FPGA:** Field Programmable Gate Array
- **FTA:** Fault Tree Analysis
- **GPU:** Graphics Processing Unit
- **HSI:** Hardware-Software Interface
- **ISA:** Instruction Set Architecture
- **MBD:** Model Based Development
- **MC/DC:** Modified Condition/Decision Coverage
- **MMU:** Memory Management Unit
- **MPU:** Memory Protection Unit
- **OS:** Operating System
- **PAL:** Programmable Array Logic
- **PE:** Processing Element
- **PLD:** Programmable Logic Device
- **PLL:** Phase Locked Loop
- **RAM:** Random Access Memory
- **ROM:** Read Only Memory
- **RTL:** Register Transfer Level
- **SoC:** System on Chip
- **SPI:** Serial Peripheral Interface
- **SW:** SoftWare
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

**Process control**
- **Definition:** process element
- **Purpose:** providing a measurement to what degree process objectives are achieved
- **Examples:** Number of elements from higher level architectural design (e.g., ECU variants, SOCs, sensors) with software portions for which no software architectural design is available yet (should be 0).
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Metrics
- **Terminology (ASPICE):** Metrics

**Baseline**
- **Definition:** work product
- **Purpose:** freezing all development artefacts at a given moment in time in order to be able to re-establish this state of development in the future
- **Examples:** -
- **Elements:** All workproducts which are subject to beaselining
- **Example Elements:** Test reports, software architecture specification, software requirements specification, source code, product quality report
- **Terminology (ISO 26262):** Baseline
- **Terminology (ASPICE):** Baseline

**Configuration data specification**
- **Definition:** work product
- **Purpose:** providing the basis for introducing required variability before the software has been built.
- **Examples:** precompiler directives
- **Elements:** Configuration data
- **Example Elements:** Compiler switches controlling for which vehicle configuration the software is built
- **Terminology (ISO 26262):** Configuration data
- **Terminology (ASPICE):** NA

**Quality measure**
- **Definition:** process element
- **Purpose:** providing quality indicators for the product or the applied processes.
- **Examples:** Process audit, work product review, test report, confirmation measure
- **Elements:** NA
- **Example Elements:** NA
- **Terminology (ISO 26262):** Confirmation measure
- **Terminology (ASPICE):** NA

**Process audit**
- **Definition:** process element
- **Purpose:** providing quality indicators for the applied processes.
- **Examples:** safety audit, configuration management audit, software testing audit
- **Elements:** NA
- **Example Elements:** NA
- **Terminology (ISO 26262):** Safety audit
- **Terminology (ASPICE):** Assessment; internal audit

**Work product review**
- **Definition:** process element
- **Purpose:** providing quality indicators for the product.
- **Examples:** document reviews, specification reviews, code reviews
- **Elements:** NA
- **Example Elements:** NA
- **Terminology (ISO 26262):** Safety assessment; software verification report; confirmation review
- **Terminology (ASPICE):** Verification results

**Review checklist**
- **Definition:** process element
- **Purpose:** providing a list of pre-defined quality criteria for work product reviews.
- **Examples:** configuration management plan review checklist, pull request review checklist, code inspection checklist, requirements review checklist
- **Elements:** quality criteria
- **Example Elements:** NA
- **Terminology (ISO 26262):** NA
- **Terminology (ASPICE):** NA

**Review report**
- **Definition:** work product
- **Purpose:** determining the quality status of a work product based on a review checklist
- **Examples:** configuration management plan review report, pull request review report, code inspection report, requirements review report
- **Elements:** Assessed quality criteria for the work product under review (=answered checklist questions)
- **Example Elements:** nan
- **Terminology (ISO 26262):** Confirmation measure results (excluding safety audit results)
- **Terminology (ASPICE):** Review evidence

**Work product defect**
- **Definition:** process element
- **Purpose:** describing violations to quality criteria from review checklists
- **Examples:** -
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Safety anomalies
- **Terminology (ASPICE):** Review evidence

**Problem record**
- **Definition:** work product
- **Purpose:** describing violation of requirements or other specifications in the software under development.
- **Examples:** -
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Error, failure, fault
- **Terminology (ASPICE):** Problem

**Development interface agreement**
- **Definition:** work product
- **Purpose:** specifying responsibility and separation of tasks between development partners.
- **Examples:** -
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Development interface agreement
- **Terminology (ASPICE):** Commitment/agreement

**Functional safety concept**
- **Definition:** work product
- **Purpose:** specifying the functional safety requirements with associated information, their allocation to design elements and their interaction necessary to achieve the safety goals
- **Examples:** -
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Functional safety concept
- **Terminology (ASPICE):** -

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
- **Terminology (ISO 26262):** NA
- **Terminology (ASPICE):** Review method

**Risk and opportunity overview**
- **Definition:** work product
- **Purpose:** providing a basis for mitigating known risks and facilitating known opportunities.
- **Examples:** -
- **Elements:** risks, opportunities
- **Example Elements:** -
- **Terminology (ISO 26262):** Risk
- **Terminology (ASPICE):** Improvement opportunity; risk
