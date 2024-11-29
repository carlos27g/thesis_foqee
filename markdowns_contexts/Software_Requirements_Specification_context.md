# Work Product Description
## Purpose
### Purpose in ISO26262
The Software Requirements Specification (SRS) in ISO 26262 serves to ensure that all safety requirements are clearly defined, traceable, and testable. It is a critical document that outlines the software safety requirements derived from the system and hardware requirements, ensuring that the software design and implementation can achieve the necessary safety goals. The SRS helps in identifying potential hazards and mitigating risks through detailed requirements, thus playing a vital role in the safety lifecycle of automotive software development.
### Purpose in Automotive SPICE
In ASPICE, the Software Requirements Specification (SRS) is essential for defining the functional and non-functional requirements of the software product. It ensures that all stakeholder needs are captured and translated into detailed software requirements, which are then used to guide the design, implementation, and testing phases. The SRS is crucial for achieving traceability, consistency, and completeness in the software development process, thereby supporting quality assurance and process improvement in line with ASPICE standards.
## Content
To comply with ISO 26262 and ASPICE standards, the 'Software Requirements Specification' should include the following key content:

1. **Functional and Non-Functional Requirements**: Clearly identify and document both functional and non-functional requirements for the software, ensuring they are derived from system requirements and architecture. These requirements should be verifiable, unambiguous, and free from design and implementation constraints.

2. **Software Safety Requirements**: Derive software safety requirements considering safety-related functionalities and properties that could lead to the violation of technical safety requirements. These should include functions for safe execution, fault detection, and maintaining safe states.

3. **Specification and Management**: Ensure the specification and management of safety requirements consider system and hardware configurations, hardware-software interfaces, timing constraints, external interfaces, and operating modes.

4. **ASIL Considerations**: If ASIL decomposition is applied, ensure compliance with relevant ISO guidelines. Safety requirements should inherit the ASIL from the safety requirements they are derived from unless decomposition is applied.

5. **Characteristics of Safety Requirements**: Safety requirements should be unambiguous, comprehensible, atomic, internally consistent, feasible, verifiable, necessary, implementation-free, complete, and conforming to applicable standards.

6. **Attributes of Safety Requirements**: Each safety requirement should have a unique identification, a status, and an ASIL level.

7. **Hierarchical and Organizational Structure**: Safety requirements should be organized hierarchically and grouped appropriately, ensuring completeness, external consistency, no duplication, and maintainability.

8. **Documentation and Identification**: Safety requirements should be clearly identifiable, possibly listed in a separate document or marked with a special attribute if included with other requirements.

By incorporating these elements, the 'Software Requirements Specification' will align with the necessary standards for safety and quality in automotive software development.
## Input
To ensure compliance of the 'Software Requirements Specification' with ISO 26262 and ASPICE standards, the following key requirements and inputs should be considered:

1. **Identification and Documentation of Requirements:**
   - Use system requirements and architecture to identify and document both functional and non-functional software requirements.
   - Ensure requirements are verifiable, unambiguous, and free from design constraints.

2. **Derivation of Software Safety Requirements:**
   - Derive software safety requirements from technical safety requirements, considering safety-related functionalities and properties.
   - Include functions that ensure safe execution, maintain safe states, and handle fault detection and mitigation.

3. **Specification and Management of Safety Requirements:**
   - Specify safety requirements using a combination of natural language and structured methods.
   - Ensure safety requirements are unambiguously identifiable, inheriting the appropriate ASIL (Automotive Safety Integrity Level).

4. **Characteristics of Safety Requirements:**
   - Ensure safety requirements are unambiguous, comprehensible, atomic, consistent, feasible, verifiable, necessary, implementation-free, complete, and conforming to relevant standards.

5. **Attributes of Safety Requirements:**
   - Assign unique identification, status, and ASIL to each safety requirement, maintaining these attributes throughout the safety lifecycle.

6. **Structuring and Prioritization:**
   - Structure software requirements by grouping and prioritizing them according to project or stakeholder needs.

7. **Consideration of Interfaces and Configurations:**
   - Account for hardware-software interfaces, system and hardware configurations, timing constraints, and external interfaces in the specification of software safety requirements.

8. **Hierarchical and Organizational Structure:**
   - Organize safety requirements hierarchically and ensure they are complete, externally consistent, and maintainable without duplication.

9. **Maintainability and Completeness:**
   - Ensure the set of requirements can be modified or extended, maintaining completeness and consistency across all levels.

Inputs for the 'Software Requirements Specification' should include:
- System requirements and architecture.
- Technical safety requirements and safety goals.
- Hardware-software interface specifications.
- Timing constraints and external interface details.
- Configuration parameters and operating modes.

By adhering to these requirements and inputs, the 'Software Requirements Specification' will align with ISO 26262 and ASPICE standards, ensuring a robust and compliant development process.
## Uses
The 'Software Requirements Specification' (SRS) is a critical work product in both ISO 26262 and ASPICE frameworks, serving as a comprehensive document that outlines the functional and non-functional requirements for software development in automotive systems. Here are the key use cases and how it aids in documentation:

1. **Requirement Identification and Documentation**: The SRS uses system requirements and architecture to identify and document software requirements. This includes both functional and non-functional aspects, ensuring that all necessary capabilities and constraints are captured.

2. **Safety Requirements Derivation**: In ISO 26262, the SRS is essential for deriving software safety requirements. It considers safety-related functionalities and properties that, if failed, could violate technical safety requirements. This ensures that safety is integrated into the software from the outset.

3. **Structuring and Prioritization**: The SRS helps in structuring and prioritizing requirements, which can be organized by functionality or project needs. This organization aids in managing complexity and aligning development efforts with stakeholder priorities.

4. **Specification of Safety Requirements**: The SRS specifies safety requirements using a combination of natural language and formal methods. This ensures that safety requirements are clear, unambiguous, and verifiable, facilitating communication among stakeholders.

5. **Attributes and Characteristics**: The SRS ensures that safety requirements have essential attributes such as unique identification, status, and ASIL (Automotive Safety Integrity Level). It also ensures that requirements are unambiguous, comprehensible, feasible, verifiable, and implementation-free.

6. **Hierarchical and Organizational Structure**: The SRS organizes safety requirements hierarchically and by appropriate grouping schemes. This structure ensures completeness, consistency, and maintainability, making it easier to manage and update requirements over time.

7. **Interface and Configuration Considerations**: The SRS takes into account hardware-software interfaces, system configurations, and external interfaces, ensuring that all interactions and dependencies are well-documented and understood.

Overall, the SRS is a foundational document that supports the development of safe, reliable, and compliant automotive software by providing a clear, structured, and comprehensive set of requirements. It facilitates communication, ensures alignment with safety standards, and aids in the verification and validation processes.

# Concepts
## Terminology (ISO)
- **baseline:** version of the approved set of one or more work products, items or elements that serves as a basis for change. A baseline is typically placed under configuration management and is used as a basis for further development through the change management process during the lifecycle.
- **confirmation review:** confirmation that a work product provides sufficient and convincing evidence of their contribution to the achievement of functional safety considering the corresponding objectives and requirements of ISO 26262. The goal of confirmation reviews is to ensure compliance with the ISO 26262 series of standards.
- **development interface agreement:** agreement between customer and supplier in which the responsibilities for activities to be performed, evidence to be reviewed, or work products to be exchanged by each party related to the development of items or elements are specified
- **element:** system, components (hardware or software), hardware parts, or software units
- **embedded software:** fully-integrated software to be executed on a processing element
- **functional safety concept:** specification of the functional safety requirements, with associated information, their allocation to elements within the architecture, and their interaction necessary to achieve the safety goals
- **functional safety requirement:** specification of implementation-independent safety behaviour or implementation-independent safety measure including its safety-related attributes
- **inspection:** examination of work products, following a formal procedure, in order to detect safety anomalies. Inspection is a means of verification. Inspection differs from testing in that it does not normally involve the operation of the associated item or element. A formal procedure normally includes a previously defined procedure, checklist, moderator and review of the results.
- **review:** examination of a work product, for achievement of its intended work product goal, according to the purpose of the review.
- **safety anomaly:** conditions that deviate from expectations and that can lead to harm. Safety anomalies can be discovered, among other times, during the review, testing, analysis, compilation, or use of components or applicable documentation. EXAMPLE Deviation can be on requirements, specifications, design documents, user documents, standards, or on experience.
- **software component:** one or more software units (3.159)
- **software tool:** computer program used in the development of an item (3.84) or element (3.41)
- **verification:** determination whether or not an examined object meets its specified requirements EXAMPLE The typical verification activities can be classified as follows: — verification review, walk-through, inspection; — verification testing; — simulation; — prototyping; and — analysis (safety analysis, control flow analysis, data flow analysis, etc.).
- **verification review:** verification activity to ensure that the result of a development activity fulfils the project requirements, or technical requirements, or both. The goal of verification reviews is technical correctness and completeness of the item or element. EXAMPLE Verification review types can be technical review, walk-through or inspection.
- **walk-through:** systematic examination of work products in order to detect safety anomalies. Walk-through is a means of verification. Any anomalies that are detected are usually addressed by rework, followed by a walk-through of the reworked work products. EXAMPLE During a walk-through, the developer explains the work product step-by-step to one or more reviewers. The objective is to create a common understanding of the work product and to identify any safety anomalies within the work product.
- **work product:** documentation resulting from one or more associated requirements of ISO 26262. The documentation can be in the form of a single document containing the complete information for the work product or a set of documents that together contain the complete information for the work product.

## Abbreviations
- **ASIL:** Automotive Safety Integrity Level
- **COTS:** Commercial Off The Shelf
- **CRC:** Cyclic Redundancy Check
- **DIA:** Development Interface Agreement
- **DMA:** Direct Memory Access
- **ECC:** Error Correction Code
- **EDC:** Error Detection Code
- **ETA:** Event Tree Analysis
- **FMEA:** Failure Mode and Effects Analysis
- **FTA:** Fault Tree Analysis
- **HARA:** Hazard Analysis and Risk Assessment
- **HSI:** Hardware-Software Interface
- **I/O:** Input – Output
- **MBD:** Model Based Development
- **MC/DC:** Modified Condition/Decision Coverage
- **OEM:** Original Equipment Manufacturer
- **QM:** Quality Management
- **RFQ:** Request For Quotation
- **SEooC:** Safety Element out of Context
- **SW:** SoftWare
- **SOP:** Start Of Production
- **SG:** Safety Goal
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

**Process control**
- **Definition:** process element
- **Purpose:** providing a measurement to what degree process objectives are achieved
- **Examples:** Number of elements from higher level architectural design (e.g., ECU variants, SOCs, sensors) with software portions for which no software architectural design is available yet (should be 0).
- **Elements:** -
- **Example Elements:** -
- **Terminology (ISO 26262):** Metrics
- **Terminology (ASPICE):** Metrics

**Measurement**
- **Definition:** process element
- **Purpose:** contributing detailed product quality data for process controls
- **Examples:** requirements coverage by test cases, structural code coverage (e.g., branch coverage), code complexity
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

**Calibration data specification**
- **Definition:** work product
- **Purpose:** providing the basis for introducing required variability after the software has been built.
- **Examples:** characteristic maps, characteristic line, behaviour switches in the deployed software
- **Elements:** Calibration data
- **Example Elements:** Engine performance curves
- **Terminology (ISO 26262):** Calibration data
- **Terminology (ASPICE):** NA

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
