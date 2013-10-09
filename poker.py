def poker():
    """
    Main Func --> Program won't work if this func is missing
   
    """
    hands = table()
    allmax(hands)

def table():
    """
    num_of_hand -> int
    hand -> str
    return card list of each player
    input specific = 5 card with the space
    between it EX. 9H 10H JH QH KH

    """
    all_hand = []
    num_of_hand = input('How many hands do you want? >>> ')
    for i in range(num_of_hand):
        hand = raw_input('Hand'+str(i+1)+'>>> ')
        hand = hand.split(' ')
        all_hand.append(hand)
    return all_hand


def allmax(hands):
    solve = []
    for hand in hands:
        solve += [tuple(hand)+hand_rank(hand)]
    from operator import itemgetter
    solve = sorted(solve,key=itemgetter(5,6),reverse=True)
    winner = solve[0]
    loser = solve[1:]
    print 'winner is',sortcard(winner[:5]),' rank:',winnerrank(winner[5]),
        ':Maxcard is',rechange(winner[6])
    for i in loser :
        if i[5] == winner[5] and rechange(winner[6]) == rechange(i[6]):
            word = 'winner is '
        else:
            word = 'loser is '
        print word,sortcard(i[:5]),' rank:',winnerrank(i[5]),':Maxcard is',rechange(i[6])
        
   
def hand_rank(hand):
   """
   (hand)-> int
 
   Return the hand rank of a hand
   
   """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
       
    if straight_flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks)
    elif fullhouse(ranks):
        return 6, kind(3, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(hand):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks)
    elif twopair(ranks):
        return 2, twopair(ranks)[0], twopair(ranks)[1], kind(1, ranks)
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks
 
def straight_flush(hand):
    """
   (hand)-> Bool
 
   Return True if hand is straight_flush,
   False otherwise
   
   """
   return straight(hand) and flush(hand)
 
def straight(hand):
   """
   (hand)-> Bool
 
   Return True if hand is straight,
   false otherwise
   
   """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
   
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5
   
 
def flush(hand):
    """
    (hand)-> Bool
 
    Return True if hand is flush, False otherwise.

    """
    suits = [s for r,s in hand]
 
    return len(set(suits)) == 1
 
def fullhouse(ranks):
    """
    (ranks)-> Bool
 
    Return True if hand is fullhouse,
    false otherwise
    
    """
    return True if kind(3, ranks) and kind(2, ranks) else False
 
def kind(n, ranks):
    """
    (ranks)-> int
 
    Return rank if hand is n kind,
    false otherwise

    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return 0
 
def twopair(ranks):
    """
    (ranks)-> tuple
 
    Return tuple of highpair and lowpair if hand is twopair,
    false otherwise
    
    """
    ranks.sort(reverse=True)
    high_pair = kind(2, ranks)
    ranks.sort()
    low_pair = kind(2, ranks)
    ranks.sort(reverse=True)
    
    if high_pair != low_pair:
        return (high_pair, low_pair)
    return ()

def sortcard(card):
    rank = 'AKQJT98765432'
    hand = sorted(card,key=compare)

def winnerrank(n):
    rank = ['Highcard', 'One pair', 'Two pair', 'Three of kind', 'Straight',
            'Flush', 'Fullhouse', 'Four of kind','Straight Flush']
    return rank[n]

def compare(card):
    rank = 'AKQJT98765432'
    return rank.index(card[0])

def rechange(n):
    rechar = {14:'A', 13:'K', 12:'Q', 11:'J', 10:'T'}
    if n in rechar:
        return rechar[n]
    return n

poker()
