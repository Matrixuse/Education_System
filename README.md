# Multi-Agent Education System (AAI-04)

---

## Project Overview
The Multi-Agent Education System is an AI-powered educational application designed to generate structured learning content through collaboration between multiple intelligent agents.

The system uses specialized agents such as a Researcher Agent to collect study material and a Writer Agent to transform that information into well-structured educational content using a Large Language Model (LLM).

This project focuses on building a smart, modular, and scalable learning system that improves content quality through agent collaboration and task specialization.

---

## Problem Statement
Develop an AI-driven multi-agent educational system that:

1. Collects relevant study resources automatically  
2. Processes and structures information intelligently  
3. Uses multiple agents with defined roles  
4. Enables communication between agents  
5. Generates high-quality educational outputs  

---

## Features
1. Multi-Agent Collaboration – Multiple agents working together  
2. Research-Based Content Generation – Information collected from sources  
3. Structured Output – Clean and organized educational content  
4. Task Delegation – Orchestrator assigns tasks to agents  
5. Shared Memory System – Enables agent communication  
6. Scalable Architecture – Easy to extend with more agents  

---

## Tech Stack

1. Programming Language:
   - Python  

2. Frameworks:
   - LangChain / CrewAI  

3. LLM API:
   - Groq API  

4. Model:
   - LLaMA 3.1 – 8B Instant  

5. Architecture Type:
   - Multi-Agent System 

---

## System Architecture (High-Level)
1. User interacts with the system  
2. Orchestrator Agent processes the request  
3. Researcher Agent collects data  
4. Data stored in shared memory  
5. Writer Agent formats and structures content  
6. System generates final output  
7. Learning/content generation loop continues  

---

## Project Structure

```bash
Education_System/
│── main.py
│
├── agents/
│   ├── researcher.py
│   └── writer.py
│
├── orchestrator/
│   └── controller.py
│
├── memory/
│   └── shared_state.py
│
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone Repository
git clone https://github.com/Matrixuse/Education_System.git

cd Education_System

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Add API Key
OPENAI_API_KEY="your_api_key_here

### 4. Run Application
python main.py

---

## Usage
1. Run the application  
2. Provide an educational topic or query  

The system will:  
3. Research the topic  
4. Process the information  
5. Generate structured content  

Example:  
Input: "Explain Artificial Intelligence"  
Output: Detailed structured explanation  

---

## Future Enhancements
1. Add Reviewer Agent for quality checking  
2. Integrate real-time data sources  
3. Build interactive UI  
4. Add personalized learning features  
5. Improve agent communication  

---

## Team Members

| No. | Name | Enrollment No |
|-----|------|--------------|
| 1 | JAYENDRA VERMA | EN22IT301043 |
| 2 | HANSRAJ SINGH RAJPUT | EN24CA5030055 |
| 3 | ASHISH NAGDA | EN24CA5030026 |
| 4 | NAMAN SHARMA | EN22IT301058 |
| 5 | ATUL MANDLOI | EN24CA5030031 |
| 6 | HITENDRA SAMEDIYA | EN24CA5030067 |

---

## Subject
Agentic AI

---

## GitHub Repository
https://github.com/Matrixuse/Education_System.git

---

## Conclusion
The Multi-Agent Education System demonstrates how Agentic AI can enhance educational content generation through collaboration between specialized agents.

By combining task delegation, shared memory, and intelligent orchestration, the system provides a strong foundation for scalable AI-powered learning platforms.

