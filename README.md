# script
Build a monitoring tool in the form of a Python script in order to check the proper functioning of a system or service.
The objective is to carry out a supervision (monitoring of computer systems) to automatically send alerts to administrators.

We want to query the metrics available on the supervised system at regular intervals in order to know the occupancy status of storage spaces, CPU utilization rate, memory utilization rate and network interface utilization rate.

The script will send this data to a database (temporal data base) in our case, InfluxDB.

The stored data will be used in dashboards built with a tool specialized in the presentation of data, in our case Grafana.

Getting Started:
  - Clone the project: https://github.com/tcardo06/script.git
  - Install Python, Grafana, InfluxDB and Psutil according to your operating system.
  - Open the project and write in the terminal of your directory project the following commande: 
      `python3 administration.py -i 4` (python or python3 depending on your installed version)
      -i being the interval of seconds at which the data is sent to your database (here 4 for exemple)
  - You can visualize your data on Grafana in the form of a graph (see images in exemple).

Trello link:
https://trello.com/b/6QMdi7Dn/scripting-admin

Grafana screenshot:

<img width="1717" alt="Capture d’écran 2022-07-01 à 14 12 53" src="https://user-images.githubusercontent.com/72390135/176893235-cde12e1a-07b1-4481-ab50-edfeeb9a0b4b.png">

InfluxDB screenshot:

<img width="1717" alt="Capture d’écran 2022-07-01 à 14 13 20" src="https://user-images.githubusercontent.com/72390135/176893255-0406eea2-83e3-418c-814c-ff005dc83f1c.png">
