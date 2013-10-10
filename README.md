#PSIT Project #2 (IT KMITL)

##Overview
Our project was created for Problem Solving of Information Technology (PSIT) subject. It was powered by Python---High-level programming. The name of project is "Poker" program.

Our project has 3 files which include
* `poker.py` --- THE PROGRAM OF OUR PROJECT.
* `poker_test.py` --- program for testing: it uses unitest module in python.
* `README.md` --- describe about details of our project


##How to use poker.py
You can run `poker.py` from Python IDLE for help your poker game. You can input a number of card and card names that you want. It will result the status which you get.

You can run "Poker" function by ....
```python
>>> hand = [.........]	### Create a variable to List type. In the list, you must add your hand.
>>> poker([hand])		### Then enter for see the result
```

Then, it show the result...
```python
The Winner is [............] Rank:........
```

I hope that it help you to decide on the game! ;)

##Members
* Mr.Chisanupong Srisaide (560700xx)
* Mr.Jenpasit Puprasert (56070022)
* Mr.Kanit Proaresai (560700xx)

##About Poker
Poker is a family of card games that the most popular in the world, because It's not complex and using a critical thinking and making a decision. It's a game that using both Lucky, Probability, Psychology and Experience in order to get the profit in the game. In this article, Let's define the following acronyms. (Universal abbreviation of who study and play poker) A is Ace, K is the King, Q is the Queen, J is for Jack, T was 10 and the card ranks in poker to sort to Descending is A K Q J T 9 8 7 6 5 4 3 2.

###How to play Poker
* **Playing 5 Card Draw** (via http://www.wikihow.com/Play-Poker)
	- **Understand the basics of poker.** Poker is usually played with a standard 4-suit 52-card deck. The ace 		normally plays high, but can sometimes play low. A joker or other wild cards may be added. At the showdown, 		those players still remaining compare their hands according to the hand rankings. Suits are not used to break 		ties, nor are cards beyond the fifth; only the best five cards in each hand are used in the comparison. In the 		case of a tie, the pot is split equally among the winning hands.
	- **Become familiar with poker hand variations.** The person who wins is the person with the highest-valued 		hand. You can't win if you don't know which hands will take the pot. If two players have hands with the same 		value (e.g. two full houses) or no one has a winning hand, then the player with the highest value card in their 	hand wins (Ace is highest). Print out a ranking of the poker hands and memorize the hands. 
	- **Chip in.** Place an "ante" (pronounced ant-ee) or "token bet" (pronounced token bet) into the pot (usually a 	spot at the center of the table, although you can use a pot if you wish). Every player places an equal amount of 	whatever your currency (poker chips, nickels, bills, car keys...). Whoever wins takes it all.
	- **Deal or be dealt with.** After shuffling (showing off) the dealer distributes the cards face down starting 		with the player to his or her immediate left and continuing clockwise, one card at a time, until everyone has 		five cards. The deck is placed in the middle of the table.
	- **Look at your cards while everyone else looks at theirs.** This is the time to evaluate how strong your hand 	is. Beginner players usually end up showing how strong their hand is with what is known as a tell. Some tells 		include; shallow breathing, lack of or too much eye contact, facial muscle flexes, etc. Trying to reduce these 		tells will give you a better chance. Keep your "poker face".
	- **Take turns.** The first person to make a call is usually the player on the dealer's left (who was dealt the 	first card). That player can open (place the first bet) or check (pass the decision onto the next player). Once 	the pot is opened, meaning that a player bets a certain amount (e.g. places a nickel in the pot), all of the 		people who already had their turns have two options:
		- See or call - Stay in the game by putting the equivalent amount in the pot.
		- Fold - Quit the game by putting your cards face down on the table; whatever you put in the pot stays 			in the pot.
		- After they've made their choices, everyone who still has a turn will have those options, plus an 			additional one:
		- Raise - Stay in the game by putting more than the last person put in the pot.
		- If someone raises, then everyone who already had a turn must see or fold again. Then the next person 			has their turn.
	- **Draw.** Once everyone has had a turn (even if everyone checked) get rid of up to three cards you don't want 	and have them replaced. This is done in turns, again beginning with the player on the dealer's left and going 		clockwise. Choose the cards that you don't think will help you gain a winning hand. You might get rid of three 		cards, or you might keep them all. If you do get rid of cards, put them face down on the table so no one sees 		what you had.
	- **Go through another round of betting.** As before, the first player can either open or check, and the 		checking can continue until someone opens, after which players can see, raise or fold. More people will start to 	fold once they realize their weak hand isn't worth the bet.
	- **Expose your cards.** Everyone turns their cards over to see who has the winning hand. Winner takes all
 
* **Hand Ranks** (via "Think Python" book on page 177)
	- Pair : two cards with the same rank
	- Two pair : two pairs of cards with the same rank
	- Three of a kind : three cards with the same rank
	- Flush : five cards with the same suit
	- Full house : three cards with one rank, two cards with another
	- Four of a kind : four cards with the same rank
	- Straight : five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
	- Straight flush : five cards in sequence (as defined above) and with the same suit
