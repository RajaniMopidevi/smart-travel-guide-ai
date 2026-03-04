# Smart Travel Guide using Multi-Agent System

## Overview

The **Smart Travel Guide** is a Python-based travel planning assistant that uses a **multi-agent architecture** to automate itinerary creation.
Instead of manually searching multiple websites for destinations, costs, and activities, the system intelligently generates a **structured travel plan** based on user inputs such as destination, trip duration, budget, and preferences.

The system demonstrates how **AI-inspired multi-agent systems** can simplify real-world tasks like travel planning by delegating responsibilities across specialized agents.

---

## Problem Statement

Planning a trip usually requires gathering information from multiple sources such as travel blogs, booking platforms, maps, and forums. Travelers must compare destinations, estimate budgets, and design itineraries manually.

This process is often:

* Time-consuming
* Confusing for first-time travelers
* Dependent on multiple scattered resources
* Difficult to personalize based on budget or interests

This project addresses these challenges by creating a **Smart Travel Guide that automates travel planning using multiple collaborating agents.**

---

## Solution

The Smart Travel Guide introduces a **multi-agent system** where each agent performs a specialized task.

The system:

* Accepts user inputs such as destination, days, budget, and preferences
* Retrieves structured destination data when available
* Uses fallback logic to generate information for unknown destinations
* Calculates estimated travel budgets
* Generates personalized day-by-day itineraries

This modular architecture ensures the system remains **scalable, flexible, and easy to extend**.

---

## System Architecture

The system follows a **multi-agent workflow**:

User Input
↓
Travel Advisor (Orchestrator Agent)
↓
Destination Agent → Retrieves or generates destination information
↓
Budget Agent → Calculates estimated trip cost
↓
Itinerary Agent → Generates personalized day-by-day travel plan
↓
Final Travel Plan Output

---

## Agents in the System

### Destination Agent

* Retrieves destination information from a predefined dataset
* Generates fallback highlights for unknown destinations
* Ensures the system works for **any city entered by the user**

### Budget Agent

* Calculates estimated travel cost based on:

  * number of travel days
  * typical cost per day
  * estimated flight expenses
* Returns a detailed budget breakdown

### Itinerary Agent

* Generates a **multi-day itinerary**
* Uses destination highlights and user preferences
* Produces personalized travel recommendations

### Travel Advisor (Orchestrator)

* Coordinates all agents
* Manages workflow and decision-making
* Combines outputs into the final travel plan

---

## Key Features

* Multi-agent system design
* Modular and extensible architecture
* Session memory for tracking interactions
* Budget estimation tool
* Dynamic itinerary generation
* Fallback logic for unknown destinations
* Works for **any city entered by the user**

---

## Project Structure

```
smart-travel-guide-ai
│
├── main.py          # Entry point for running the travel planner
├── agents.py        # Multi-agent logic
├── tools.py         # Utility functions (destination lookup, budget)
├── data.py          # Destination dataset
├── memory.py        # Session memory handling
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

---

## Example Usage

Run the program:

```
python main.py
```

Example input:

```
Enter destination: Paris
Enter number of days: 4
Enter travel preference: museums and cafes
Enter your budget (INR): 90000
```

Example output:

```
------ Travel Plan ------

Destination: Paris
Country: Unknown

Estimated Budget:
20000 INR

Itinerary:

Day 1: Visit Paris Central Market and enjoy museums and cafes.
Day 2: Visit Paris Old Town and enjoy museums and cafes.
Day 3: Visit Paris Cultural District and enjoy museums and cafes.
Day 4: Visit Paris Main Landmark and enjoy museums and cafes.
```

---

## Technologies Used

* Python
* Multi-Agent System Design
* Modular Software Architecture
* Rule-Based Logic
* AI-Inspired Itinerary Generation

---

## Future Enhancements

Possible improvements include:

* Integrating real travel APIs (flight and hotel search)
* Adding a weather recommendation agent
* Integrating large language models for advanced itinerary generation
* Creating a web interface using Streamlit
* Visualizing itineraries using maps and timelines

---

## Learning Outcomes

This project demonstrates practical concepts such as:

* Multi-agent collaboration
* Modular system design
* Agent orchestration
* Tool-based AI workflows
* Context management using session memory

---

## Author

Developed as an AI systems project demonstrating how **multi-agent architectures can automate travel planning and decision support tasks.**
