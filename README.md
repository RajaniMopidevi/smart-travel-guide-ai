# Smart Travel Guide – AI Powered Multi-Agent System

## Overview

The **Smart Travel Guide** is an AI-powered travel planning system built using a **multi-agent architecture**.
It automatically generates **detailed, personalized travel itineraries** including places to visit, food recommendations, and daily plans.

Unlike traditional travel planners, this system combines:

*  Structured data (for known destinations)
*  AI generation (for dynamic planning)

to deliver a **complete travel experience in seconds**.

---

## Problem

Planning a trip is often:

* Time-consuming ⏳
* Scattered across multiple websites 🌐
* Difficult to personalize 🎯
* Confusing for beginners 😵

Users must manually:

* Research destinations
* Estimate budgets
* Plan day-by-day itineraries

---

## Solution

This project solves the problem using a **Multi-Agent AI System**.

The system:

* Accepts user inputs (destination, days, budget, preferences)
* Fetches real destination data (if available)
* Uses AI (Ollama) to generate:

  * Real places
  *  Food recommendations
  *  Detailed day-wise itinerary
  * Calculates budget automatically

---

## System Architecture

```
User Input
   ↓
Travel Advisor (Main Controller)
   ↓
Destination Agent → Gets or generates destination data
   ↓
Budget Agent → Calculates trip cost
   ↓
Itinerary Agent → AI generates full travel plan
   ↓
Final Output (Detailed Travel Plan)
```

---

##  Agents Explained

### 🔹 Destination Agent

* Fetches destination from dataset (`data.py`)
* Uses AI fallback for unknown locations
* Ensures system works for **ANY destination worldwide**

---

### 🔹 Budget Agent

* Calculates:

  * Cost per day
  * Total trip cost
  * Flight estimates
  * Returns structured budget breakdown

---

### 🔹 Itinerary Agent (Core AI)

* Uses **Ollama (LLM)** to generate:

  * Full day-wise plans
  * Morning / Afternoon / Evening schedule
  * Food & local experiences
  * Produces **realistic travel plans**

---

### 🔹 Travel Advisor (Orchestrator)

* Coordinates all agents
* Combines outputs into final result

---

##  Key Features

* Multi-Agent System Design
* AI-Powered Itinerary Generation (Ollama)
* Works for ANY destination
* Includes food & local experiences
* Budget estimation system
* Modular & scalable architecture
* Hybrid system (data + AI)

---

## Project Structure

```
main.py      → Entry point  
agents.py    → Multi-agent logic  
tools.py     → Utilities (budget, data access)  
data.py      → Destination dataset  
memory.py    → Session handling  

```

---

## How to Run

### 1️ Install dependencies

```
pip install -r requirements.txt
```

### 2️ Install Ollama

Download from: https://ollama.com

### 3️ Pull model

```
ollama pull gemma3:4b
```

### 4️ Run project

```
python main.py
```

---

## Example Input

```
Enter destination: Mumbai
Enter number of days: 5
Enter travel preference: food, beach, popular markets etc
Enter your budget (INR): 60000
```

---

## 🎯 Example Output

* Destination: Mumbai
* Country: India
* Budget: {'approx_total_inr': 25500, 'breakdown': {'days_cost': 17500, 'flights_estimate': 8000}}
* Itinerary:

```
Okay, here's a detailed 5-day travel itinerary for Mumbai, focusing on your specified interests (Gateway of India, Elephanta Caves, Marine Drive, Shree Siddhivinayak Temple, Dhobi Ghat) and incorporating food, beach, markets, and a realistic structure:

Day 1: Gateway to Mumbai & Colonial Charm

Morning (9:00 AM - 1:00 PM): Start at the Gateway of India.  Take plenty of photos, explore the surrounding area, and consider a short boat ride around the harbor (various operators available).
Afternoon (1:00 PM - 5:00 PM):Lunch at Cafe Leopold (Fort) - a historic and popular spot for Indian and Western cuisine. Afterward, explore Colaba Causeway Market, browsing for clothes, jewelry, souvenirs, and street food.
Evening (5:00 PM - 9:00 PM):Walk along Marine Drive (the ‘Queen’s Necklace’) – enjoy the sea breeze and city views. Dinner at Trishna (Fort) – known for its delicious seafood, particularly the butter garlic prawns.
Food:Cafe Leopold, Trishna, Street food at Colaba Causeway (try Pav Bhaji, Vada Pav).

Day 2: Island Adventure & Spiritual Significance

Morning (8:00 AM - 1:00 PM): Take the ferry from Gateway of India to Elephanta Caves. Explore the ancient cave temples dedicated to Lord Shiva. Allow 3-4 hours for the visit, including ferry time. (Ferry departs every 30-60 minutes)
Afternoon (1:00 PM - 5:00 PM): Lunch at a restaurant near the ferry terminal in Gateway of India – Anthony’s (Continental/Seafood) offers great views.
Evening (5:00 PM - 9:00 PM): Visit the Shree Siddhivinayak Temple (Prabhadevi) - one of Mumbai's most important Hindu temples.  (Be prepared for crowds). Afterward, explore the nearby Siddhivinayak Temple Market for religious items and snacks.
Food: Anthony's, Street food snacks at Siddhivinayak Temple Market.

Day 3: Markets & Bollywood Buzz

Morning (9:00 AM - 1:00 PM): Immerse yourself in the vibrant chaos of Crawford Market - a wholesale market with a huge variety of goods (fruits, vegetables, spices, textiles).  Be prepared for a sensory overload!
Afternoon (1:00 PM - 5:00 PM): Lunch at Cannon Pav Bhaji (Fort) - known for their authentic and delicious Pav Bhaji. Afterwards, explore Matunga, a local area known for its Irani cafes.
Evening (5:00 PM - 9:00 PM):  Take a Bollywood Studio Tour (book in advance) - get a glimpse into the world of Indian cinema. Dinner at Kyani & Co. (Fort) -  an iconic Irani cafe known for its Berry Punch and savory snacks.
Food: Cannon Pav Bhaji, Kyani & Co., street food at Crawford Market.

Day 4: Beach Relaxation & Artistic Vibes

Morning (9:00 AM - 1:00 PM): Head to Juhu Beach. Relax on the sand, enjoy the sea breeze, and perhaps try some street food (bhel puri, pani puri).
Afternoon (1:00 PM - 5:00 PM): Lunch at Gajalee Seafood Restaurant (Juhu) – Popular for its fresh seafood. Afterward, explore the art galleries along Ashoka Road in Bandra.
Evening (5:00 PM - 9:00 PM): Stroll along Bandra-Worli Sea Link for stunning views, especially at sunset. Dinner at Bajapti Misal (Bandra) - a local favorite for Misal Pav.
Food: Gajalee, Bajapti Misal.


Day 5: Dhobi Ghat & Departure

Morning (9:00 AM - 1:00 PM): Visit the Dhobi Ghat (Perlavala Wadi) - witness the spectacle of laundry being hand-washed and dried along the river. (Respectful photography is key.)
Afternoon (1:00 PM - 4:00 PM):  Lunch at Burger Singh (Various Locations) - a popular burger chain for a casual meal. Afterwards, do some last-minute souvenir shopping in a market of your choice (Colaba or Crawford).
Evening (4:00 PM onwards): Depending on your departure time, relax at a cafe or explore a neighborhood you missed.  Head to the airport for your flight.
Food: Burger Singh, Street Food at your chosen market.


Important Notes:
Transportation: Mumbai has a good local train system, taxis, and auto-rickshaws. Consider using the local trains for shorter distances - it's an experience! Uber/Ola are also readily available.
Traffic: Mumbai traffic can be extremely heavy, so factor in extra travel time.
Weather: Mumbai can be hot and humid, especially during the summer months. Pack light, breathable clothing.
Safety: Be aware of your surroundings and take precautions against petty theft.
Bookings: Book your Bollywood studio tour and any specific restaurant reservations in advance, especially during peak season.
Flexibility: This is a suggested itinerary, feel free to adjust it based on your interests and preferences.

```
---

## 💡 Why This Project Stands Out

- Combines rule-based systems with AI (LLM) for real-world problem solving  
- Uses a multi-agent architecture instead of a monolithic design  
- Generates dynamic travel plans for both known and unknown destinations  
- Produces structured, human-like itineraries including food and experiences  
- Designed to be scalable and extendable with additional agents  

---

##  Technologies Used

* Python
* Multi-Agent System Design
* Ollama (LLM Integration)
* Prompt Engineering
* Modular Architecture

---

##  Future Enhancements

*  Web UI (Streamlit / React)
*  Hotel & flight integration
*  Maps & route visualization
*  Preference-based prioritization
*  Budget optimization AI

---

##  Learning Outcomes

* Multi-agent system design
* AI + rule-based hybrid architecture
* LLM integration (Ollama)
* Prompt engineering
* Modular software design

---

##  Author

Built as an AI project to demonstrate how **multi-agent systems + LLMs can automate real-world decision making**.

---

