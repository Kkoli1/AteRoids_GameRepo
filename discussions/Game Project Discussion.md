## Game Project Discussion

- Presentation will start on March 17
- Project deadline is on April 1



Objectives

- [x] Design Pattern
- [x] Code Conventions and Best practices 
- [x] Documentation 
- [x] Exception Handling 



Framework 

- PyGame



Language 

- Python



### Game Entities

- Ship (Factory Pattern)
  - Contains Bullet Object: relationship is composition 
  - 3 Kinds of ship
- Asteroid (Inheritance)
  - Main Asteroid*
  - Small Asteroid 



### Program Entities

| Entity             | Responsibility                                               |
| ------------------ | ------------------------------------------------------------ |
| Logger (Singleton) | Keeps score of the game and stores it on disk when the program end |
| MetaData*          | Keeps the state of the game and triggered by the end of the  |
| MainClass          | Runs the game component and generate the entire gameplay     |
| WindowObject       | Responsible for all action triggered by the user             |
| FileHandler        | Responsible for making transactions with external files such as updating files |



### Information Requirement

```
source {
	babyroid_count: int,
	score:int,
	username:str,
}

highscore_table {
	list_of_score:List[int]
}
```



### Feature List

- Game is not endless; environment and obstacles are scripted 
- Different game levels alter the following variables
  - Number of opponents 
  - Environment 
  - Pace of bullets and kinds of bullets 
- Should save and load file
- Should contain a file that keeps top 10 highscore of the game
- Game will end when AteRoid reaches the end line 



### Action Plan and Distribution of Task 

- Window Screen 
  - Menu 
    - Events that are associated with Menu
- Documentation and Design Layout 
- Game Elements
- File handling, error handling and implementation of design pattern



### Recommendations

- PEP 8 Compliance
  - PEP 8 Standards https://peps.python.org/pep-0008/
  - [Importing library guidelines](https://dev.to/iamdeb25/guidelines-on-importing-modules-in-python-2lp)
- Type Annotations
  - Tool: http://mypy-lang.org/
- Google format Docstring
  - Tool: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
