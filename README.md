## Project name:
Laptop search

### Short description:
In this application, a user can input a specific laptop or brand to check what website, compared between 3 different sites, has the best price available. The user is also given a list of laptops near the searched laptop's price range. The laptop is searched using BeautifulSoup, and the list of alternative laptops is found by clustering of CSV data. This means, that the results will be the closest in price, in the same cluster.

### List of used technologies:
* matplotlib
* pandas
* numpy
* sklearn
* beautifulsoup
* csv
* re(regular expression)
* flask

### Installation guide:
The code is meant to be run in the docker environment given by Thomas Hartmann(https://github.com/Hartmannsolution/docker_notebooks). We recommend using Visual Studio Code to run the project, as this is what the project is developed and tested with.

### User guide:
1. Open a terminal in the project directory
2. In the terminal, type 'FLASK_APP="server.py"'
3. In the terminal, type 'flask run --host=0.0.0.0'
4. In a browser, open the IP: http://127.0.0.1:5000/, or click the link if using Visual Studio Code.

### Status:
Everything we planned to do is done, as listed in the general tasks.

### List of Challenges:
* Webscraping
* Clustering with meanshift
* Handling DataFrames with Pandas
* Make an interface using Flask

### General tasks:
Part 1 (webscraping, regex)
* 1.1 Webscrape a specific laptop or brand from different websites
* 1.2 Use regex to format information on the cheapest one found.

Part 2 - Main challenge - (csv with pandas, clustering with meanshift)
* 2.1 Generate a CSV file with laptop data, and save to a DataFrame.
* 2.2 Show a graph of the connection between brand and price of laptops
* 2.3 Prepare the data for clustering purposes.
* 2.4 Get the different clusters, and save the data in a seperate CSV file.

Part 3
* 3.1 Determine which cluster, the laptop found in part 1 belongs to.
* 3.2 Present top 5 laptops, sorted by closest price, in the same cluster.

Part 4(Flask)
* 4.1 Use Flask to make an interface, where the user can search a laptop, and get the top 5 results laptops in the same cluster/category.


### Made by:
* Sebastian Steen Lundby Hansen (cph-sh499) 
* Sebastian James Bentley (cph-sb287)
* Michael Christian Ibsen(cph-mi93)
* Rasmus Grønbek (cph-rg86)
