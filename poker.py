def poker(hands):
    """
    Show result of the game
    How to use >>>> poker([]) --> list only
    if have more than 1 hand show == they are draw

    """
    maxhand = hand_rank(max(hands,key=hand_rank))
    return 'The Winner is '+str([hand for hand in hands if maxhand  == hand_rank(hand)])

   
def hand_rank(hand):
    """
   (hand)-> int
 
   Return the hand rank of a hand
   """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
       
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
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
   
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
    """
    return hand that already sorted
    """
    rank='AKQJT98765432'
    hand=sorted(card,key=compare)
    return hand

def winnerrank(n):
    """
    Return rank of each hand
    """
    rank=['Highcard','One pair','Two pair','Three of kind','Straight','Flush','Fullhouse','Four of kind','Straight Flush']
    return rank[n]

def compare(card):
    """
    Compare rank of each hands
    """
    rank='AKQJT98765432'
    return rank.index(card[0])

def rechange(n):
    """
    Return if T J Q K A
    """
    rechar={14:'A',13:'K',12:'Q',11:'J',10:'T'}
    if n in rechar:
        return rechar[n]
    return n
