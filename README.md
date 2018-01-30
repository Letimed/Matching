# Project matching EPITECH

This repository contains the code related to the EPITECH matching project.
The goal is to find a maximum matching in a dataset of our choice.

To run the project :
```bash
  python matchmaking.py
```

# Dataset

The dataset represent a set a players separated into 2 distinct teams, the resulting graph is therefore a **bipartite graph.**

To generate a new dataset :
```bash
	python datacreate.py
```
This command outputs a **data.csv** file.

The actual data related to each player are the following :

| Variable      	| Meaning									|
| :---------------- |:------------------------------------------|
| team    			| the team of the player 					| 
| nbWin     		| total number of win    					| 
| nbLose 			| total number of lose   					| 
| nbtotalGame		| total number of games	 					| 
| averageGameTime 	| average game time							| 
| kill 				| average number of kill per game			| 
| death 			| average number of death per game			| 
| assist 			| average number of assist per game			|   
| honor 			| average number of honor per game  		| 
| report 			| average number of report per game 		| 
| Ratevictory 		| win / loose ratio on the last 20 games	|
| Pctafk 			| percentage of afk for the player 			|
| Nationalite 		| Country of the player						|
| Gold 				| Average number of gold earned per game 	| 
| GameCurrency 		| Amount of gold possessed by the player 	|


*All those data aggregated represent the set of player looking for a match at a time "t"*

## Used variables

In order to provide a matching a study of the variables needs to be done to remove the ones that are :
 -	**Irrelevant**
 -	**Correlated with each other**
 -	**Redundant**
 
 The variables that were considered are the following with their respective description and ponderation:
 
 
| Variable      	| Description 				| Ponderation 	| Objective |
|:----------------- |:--------------------------|:--------------|:----------|
| WinRate			| nbWin / nbTotalGame 		| x 1.5			| Favourise matching with similar WinRate |
| Kda    			| (kill + assist) / death 	| x 0.8			| Diminishing the impact of a good or bad long term KDA |
| Afk 				| Pctafk					| x 1.3			| Punish players with a higher afk percentage , matching them with other "bad behaved" players |
| Report			| Report 					| x 1.2 		| Punish players with a higher report percentage , matching them with other "bad behaved" players |
| Honor 			| Honor 					| x 1.2 		| Favourise matching against other "well behaved" opponents |
| RateVictory		| RateVictory 				| x 2 			| Highly Favourise matching with similar short term victory ratio | 

## Building the graph

Each player in the dataset is represented by a  **vertex** in the graph.
Similarly , if a similarity is found between two players it is represented by an **edge** linking the two **vertices**

Computing the similarity is done this way : 

```python
for pt1 in team_1:
    for pt2 in team_2:

        distance = (pt1._Dwinrate - pt2._Dwinrate) ** 2
        distance += (pt1._Dkda - pt2._Dkda) ** 2
        distance += (pt1._Dhonor - pt2._Dhonor) ** 2
        distance += (pt1._Dreport - pt2._Dreport) ** 2
        distance += (pt1._Dafk - pt2._Dafk) ** 2
        distance += (pt1._Dratevictory - pt2._Dratevictory) ** 2

        distance = math.sqrt(distance)

        if distance < 0.8:
            graph.add_edge(graph.find_vertex(pt1._idPlayer), graph.find_vertex(pt2._idPlayer))

```
Computhing a similarity is computing the **euclidian distance** between a player and all the others ( iteratively ) if the distance is less than a certain threshold ( 0.8 ) we consider a similarity between the two players and add an **edge** between them.

This threshold has been chosen in order to provide a high enough level of matching but can be changed easily in matchmaking.py

## Finding a maximum matching

In order to find a maximum matching for our newly created bipartite graph we implemented the **Hopcroft-Karp** algorithm.

The implementation is highly derived from the pseudocode available on the [Hopcroft-Karp wikipedia](https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm)

> U will be used to refer to the first partition of the graph
> V will be used to refer to the second partition of the graph

![sample bipartite graph](https://i.stack.imgur.com/6z72n.png)

The Hopcroft-Karp algorithm finds a maximum matching by running a breath first search starting from all unmatched nodes in U and goes to unmatched nodes in V. During the search the distance from the source of the search to the unmatched node in V is updated.

In a second time , a depth first search in run following the path with distance incrementing by 1. This selects one of the many possible path found by the breadth first search.  When arriving to an unmatched node in V if the distance is at least one more than the current distance for this vertex then the path is crossing more vertices ( since the graph is bipartite the path can only zig zag betwen vertices in U and V ) .

This path is selected and the pairing are updated. 

Repeating this step until the breadth first search can no longer find a path ensures that the algorithm will only stop when a maximum cardinality matching is found.
