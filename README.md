#PSIT Project #2 (IT KMITL)

##Overview
![Poker](http://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Holdem.jpg/320px-Holdem.jpg) ![poker.py code](https://dl.dropboxusercontent.com/u/371276/poker_code.png)

Ps. Thanks the first photo from [Wikipedia](http://en.wikipedia.org/wiki/Poker)

Our project was created for Problem Solving of Information Technology (PSIT) subject. It was powered by Python---High-level programming. The name of project is "Poker" program.

Our project has 3 files which include:
* `poker.py` --- THE PROGRAM OF OUR PROJECT.
* `poker_test.py` --- program for testing: it uses unitest module in python.
* `README.md` --- describe about details of our project.

##How to use poker.py
You can run `poker.py` from Python IDLE for help your poker game. You can input card names that you want. Then, it will result the status which you get.

###Arrangement:
- A is Ace, K is the King, Q is the Queen, J is Jack and T is 10.
- Spades are S, Hearts are H, Diamonds are D and Clubs are C.
- The card ranks in poker to sort to descending is A K Q J T 9 8 7 6 5 4 3 2.
- **Ex:** If you want a card "Jack of Hearts", **you MUST type 'JH'** into the list.

###Let's Start !!
You can run "Poker" function by open Python IDLE, open file `poker.py` and type this....
```python
>>> hand1 = ['TS', 'JS', ...]	### Create a variable to List type!
>>> hand2 = ['5H', '4S', ...]   ### In the list, you MUST add your hand to string type!
>>> hand3 = ['7H', '7S', ...]   ### In the list, each strings CAN NOT be same!
    .
    .
    .
>>> poker([hand1, hand2, ...])	### Then enter for see the result
```

Then, it shows the result...
```python
The Winner is ['TS', 'JS', ...] Rank:........
```

***I hope that it helps you to decide on the game!*** **;)**

##Members
* Mr.Chisanupong Srisaide (Student ID: 56070029)
* Mr.Jenpasit Puprasert   (Student ID: 56070022)
* Mr.Kanit Proaresai      (Student ID: 56070010)

##About Poker
* You can see at https://github.com/mekzcnt/poker/wiki/About-Poker
