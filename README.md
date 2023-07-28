# README #

This README would normally document whatever steps are necessary to get your application up and running.

## Data
https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up

The columns "Global_active_power" and "Global_reactive_power" are two important electrical power consumption measurements in the dataset. Understanding their meaning and relevance is crucial for predicting future values of "Voltage" and gaining insights into the electricity consumption behavior.

1. **Global Active Power (Global_active_power):**
   - Meaning: Global active power represents the actual electrical power consumed by the household's electrical appliances and devices, measured in kilowatts (kW). It includes the power used to perform useful work, such as running appliances, lights, and other electrical devices.
   - Relevance: Global active power is a key indicator of the total power consumption in a household. It reflects the actual energy consumed by the electrical devices and can provide insights into peak usage periods and overall energy demand patterns.

2. **Global Reactive Power (Global_reactive_power):**
   - Meaning: Global reactive power represents the non-working power in the electrical system, measured in kilovolt-amperes reactive (kVAR). It is the power used to establish magnetic fields in inductive devices (e.g., motors, transformers) and is required for their operation but does not perform any useful work.
   - Relevance: While global reactive power doesn't directly contribute to useful work, it is essential for the proper functioning of inductive devices. It is important to monitor reactive power to ensure the efficiency and stability of the electrical system. Excessive reactive power can lead to power losses and decreased system performance.

3. **Voltage (Voltage):**
   - Meaning: Voltage, measured in volts (V), represents the electrical potential difference between two points in an electrical circuit. It is a critical parameter in the electrical system, determining the force with which electricity flows through the circuit.
   - Relevance: Voltage is directly related to electrical energy consumption. Variations in voltage levels can impact the performance and lifespan of electrical appliances and devices. Predicting future values of voltage is valuable for identifying potential voltage fluctuations and voltage-related issues that might affect the electrical system's stability and appliance performance.

The relevance of "Global_active_power" and "Global_reactive_power" to predict future values of "Voltage" lies in the fact that electrical power consumption patterns influence the voltage levels in the electrical system. A sudden increase or decrease in power demand can lead to voltage fluctuations. Understanding the relationship between power consumption and voltage helps in predicting potential voltage variations and ensuring a stable and efficient electrical system.

In time series forecasting, considering these related variables, such as "Global_active_power" and "Global_reactive_power," alongside "Voltage," can lead to more accurate and robust predictions. By analyzing the historical patterns between these variables, a forecasting model can capture dependencies and correlations that allow for more precise predictions of future voltage values based on expected power consumption behaviors.

* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact