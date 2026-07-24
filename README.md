# 🌱 AI Crop Advisory System

AI Crop Advisory System is an AI-powered agricultural advisory platform that assists farmers in making informed decisions using Machine Learning, Deep Learning, Large Language Models (LLMs), and real-time weather information.

<Br/>

<a id="deployment"></a>

# 🚀 Deployment

This project is deployed on **[AUP Cloud](https://dub.aupcloud.io/)** (AMD University Program), running on a Linux node powered by an **AMD RYZEN AI MAX+ PRO 395 w/ Radeon 8060S**. The `ollama-agent:latest` environment is spawned through the AUP Cloud Server Options dashboard to host the LLM-powered chatbot component.

<img width="1440" alt="AUP Cloud Server Options" src="screenshots/AUP_cloud.png">

<Br/>

# Table of Contents

- [Deployment](#deployment)
- [Problem Statement](#ps)
- [Inspiration](#inspiration)
- [Solution](#solution)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#structure)
- [System Workflow](#workflow)
- [Machine Learning Models](#ml-models)
- [Project Setup Guide](#setup)
- [Example Usage](#example-usage)
- [Datasets Used](#datasets)
- [Future Enhancements](#future)
- [Working Model Screenshots](#working-model-ss)

<a id="ps"></a>

# Problem Statement

Agriculture is one of the most important sectors for food production, but farmers often face challenges in selecting suitable crops, identifying plant diseases, managing irrigation, and accessing reliable agricultural guidance. Can we build a single AI-powered system that analyzes soil information and real-time weather conditions to guide farmers through these decisions, instead of relying on scattered, generic, or hard-to-access advice?

<a id="inspiration"></a>

# Inspiration

As we all know, farming decisions directly affect a farmer's yield and livelihood, yet the tools available to make these decisions are often fragmented. The following are the drawbacks of the existing approach:

1. Farmers often lack easy access to data-driven crop recommendations tailored to their soil and local weather conditions.
2. Plant diseases are frequently identified too late, or misdiagnosed, leading to crop loss and unnecessary pesticide/fertilizer use.
3. Irrigation decisions are often made on habit or guesswork rather than actual temperature, humidity, and rainfall data.
4. Reliable, on-demand agricultural guidance is not always available when farmers need it most.

We decided to work on this problem to bring Machine Learning, Deep Learning, and LLMs together into one accessible advisory system for farmers.

<a id="solution"></a>

# Solution

The AI Crop Advisory System combines Machine Learning, Deep Learning, and Artificial Intelligence into a single interactive application to overcome these drawbacks:

1. A trained Machine Learning model combined with live weather data recommends the most suitable crop for a farmer's soil and location.
2. A Deep Learning model detects plant diseases directly from leaf images and provides actionable treatment guidance.
3. Real-time weather data drives irrigation recommendations, removing the guesswork from watering decisions.
4. A locally-running LLM-powered chatbot answers agricultural questions on demand, without needing an internet-dependent third-party service.

<a id="features"></a>

# Features

- Unified command-line application combining crop recommendation, disease detection, irrigation advice, and an AI chatbot.

- ## 🌾 Crop Recommendation

  - Recommends the most suitable crop based on Soil Type, Nitrogen (N), Phosphorus (P), Potassium (K), Soil pH, Live Temperature, Live Humidity, and Live Rainfall.
  - Uses a trained Machine Learning model together with live weather data retrieved through the OpenWeatherMap API.

- ## 🍃 Disease Detection

  - Detects plant diseases from uploaded leaf images using a Deep Learning model based on **MobileNetV2**.
  - Returns Disease Name, Prediction Confidence, Symptoms, Cause, Treatment, and Recommended Fertilizer.
  - Supported diseases: Tomato Early Blight, Tomato Late Blight, Potato Early Blight, Potato Late Blight, Rice Bacterial Leaf Blight, Rice Brown Spot, Rice Leaf Smut.

- ## 💧 Irrigation Recommendation

  - Uses Temperature, Humidity, and Rainfall to advise whether irrigation is required based on current environmental conditions.

- ## 🤖 Agricultural Chatbot

  - An AI-powered chatbot built using **Qwen 3.5 (2B)** running locally through **Ollama**.
  - Answers questions on crop cultivation, fertilizer usage, pest management, organic farming, seasonal farming, and general agricultural practices.

- ## 🌦 Live Weather Integration

  - Fetches real-time Temperature, Humidity, Rainfall, Weather Condition, and Wind Speed using the OpenWeatherMap API.

<a id="tech-stack"></a>

# Tech Stack

- Python
- Scikit-learn
- Random Forest Classifier
- PyTorch
- TorchVision
- MobileNetV2
- Ollama
- Qwen 3.5 (2B)
- Pandas
- NumPy
- Pillow
- Requests
- Joblib
- OpenWeatherMap API

<a id="structure"></a>

# Project Structure

```
CropAdvisor/
│
├── agent.py                  # Main application
├── router.py                 # AI query routing
├── chatbot.py                # Agricultural chatbot
├── tools.py                  # Tool management
│
├── crop.py                   # Crop prediction model
├── crop_agent.py             # Crop recommendation workflow
├── disease.py                # Disease information
├── image_classifier.py       # Leaf disease prediction
├── irrigation.py             # Irrigation recommendation
├── soil.py                   # Soil information
├── weather.py                # Live weather API
│
├── train_disease_model.py    # Model training script
│
├── models/
│   ├── crop_model.pkl
│   ├── disease_model.pth
│   └── class_names.pth
│
├── images/
├── training_dataset/
│
├── README.md
└── requirements.txt
```

<a id="workflow"></a>

# System Workflow

```
                 Farmer
                    │
                    ▼
         AI Crop Advisory System
                    │
     ┌──────────────┼──────────────┬──────────────┐
     ▼              ▼              ▼              ▼
 Crop            Disease       Irrigation      Chatbot
Recommendation   Detection     Recommendation
     │              │              │
     ▼              ▼              ▼
Weather API    Leaf Image      Weather Data
     │              │
     ▼              ▼
 Soil Data     MobileNetV2
     │              │
     ▼              ▼
Random Forest   Disease Details
     │
     ▼
Recommended Crop
```

<a id="ml-models"></a>

# Machine Learning Models

## Crop Recommendation

**Algorithm:** Random Forest Classifier

**Input Features:** Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall

**Output:** Recommended Crop

## Leaf Disease Detection

**Architecture:** MobileNetV2

**Framework:** PyTorch

**Input:** Leaf Image (224 × 224 pixels)

**Output:** Disease Name, Prediction Confidence

<a id="setup"></a>

# Project Setup Guide

1. Clone the repository

   ```sh
   git clone <https://github.com/PATHIPATIMOHITHA18/CropAdvisor>
   cd CropAdvisor
   ```

2. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

3. Start Ollama

   ```sh
   ollama serve
   ```

4. Run the application

   ```sh
   python agent.py
   ```

<a id="example-usage"></a>

# Example Usage

## Crop Recommendation

**Input**

```
City : Hyderabad
Soil : Black Soil
```

**Output**

```
Location : Hyderabad
Temperature : 29°C
Humidity : 72%
Rainfall : 5 mm

Recommended Crop
Rice
```

<br />

## Disease Detection

**Input**

```
Leaf Image
```

**Output**

```
Disease
Tomato Early Blight

Confidence
98.64%

Symptoms
Brown circular spots on older leaves.

Cause
Alternaria fungus

Treatment
Spray Mancozeb fungicide.

Recommended Fertilizer
NPK 10-10-20
```

<br />

## Irrigation Recommendation

**Input**

```
City : Chittoor
```

**Output**

```
Temperature : 33°C
Humidity : 62%
Rainfall : 4 mm
Moderate irrigation is recommended based on the current weather conditions.
```

<br />

## Agricultural Chatbot

**Example Question**

```
How can I improve rice yield?
```

The chatbot provides practical agricultural guidance using the locally running Qwen 3.5 language model.

<a id="datasets"></a>

# Datasets Used

- Crop Recommendation Dataset (Kaggle)
- PlantVillage Dataset
- Rice Leaf Disease Dataset

<a id="future"></a>

# Future Enhancements

- Fertilizer Recommendation using Machine Learning
- Pest Detection using Deep Learning
- Multi-language Support
- Voice-based Farmer Assistant
- Mobile Application
- Yield Prediction
- Farmer Profile Management
- Satellite Weather Integration
- GPS-based Soil Information

<a id="working-model-ss"></a>

# Working Model Screenshots

![image](screenshots/crop_recommendation.png)

<br />

![image](screenshots/Disease_detection.png)

<br />

![image](screenshots/Irrigation.png)

<br />

![image](screenshots/chatbot.png)

<br />

# 👨‍💻 Author

Developed as an AI-powered agricultural advisory system using Machine Learning, Deep Learning, Large Language Models, and real-time weather integration to support farmers in making informed agricultural decisions.

<br />

# 👥 Team Details

**Team Name:** Data Dynamos

**Team Leader:** Pathipati Mohitha

**Team Members:**

1. Modharapalem Chandana
2. Nalabolu Sreeja
3. Maddina Gowthami
4. M Hemanth
