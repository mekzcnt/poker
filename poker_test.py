import unittest
import poker
 
class TestPoker(unittest.TestCase):
    '''Example unittest test methods for get_divisors.'''
 
    def test_poker_example_SF(self):
        '''Test get result of game
        Test Straight Flush
        sf = ['TS','JS','QS','KS','AS']
        '''
        sf = ['TS','JS','QS','KS','AS']
        actual = poker.poker([sf])
        expected = "The Winner is [['TS', 'JS', 'QS', 'KS', 'AS']] Rank:Straight Flush"
        self.assertEqual(actual, expected)
    
    def test_poker_example_ST(self):
        '''Test get result of game
        Test Straight
        st = ['8S','7C','6H','5H','4S']
        '''
        st = ['8S','7C','6H','5H','4S']
        actual = poker.poker([st])
        expected = "The Winner is [['8S', '7C', '6H', '5H', '4S']] Rank:Straight"
        self.assertEqual(actual, expected)
 
    def test_poker_example_FL(self):
        '''Test get result of game
        Test Flush
        fl = ['2S','4S','6S','KS','7S']
        '''
        fl = ['2S','4S','6S','KS','7S']
        actual = poker.poker([fl])
        expected = "The Winner is [['2S', '4S', '6S', 'KS', '7S']] Rank:Flush"
        self.assertEqual(actual, expected)
        
    def test_poker_example_FK(self):
        '''Test get result of game
        Test Four of kind
        fk = ['6S','6H','6D','6C','3D']
        '''
        fk = ['6S','6H','6D','6C','3D']
        actual = poker.poker([fk])
        expected = "The Winner is [['6S', '6H', '6D', '6C', '3D']] Rank:Four of kind"
        self.assertEqual(actual, expected)
            
    def test_poker_example_TK(self):
        '''Test get result of game
        Test Three of kind
        tk = ['7H','7S','7D','3C','2S']
        '''
        tk = ['7H','7S','7D','3C','2S']
        actual = poker.poker([tk])
        expected = "The Winner is [['7H', '7S', '7D', '3C', '2S']] Rank:Three of kind"
        self.assertEqual(actual, expected)
            
    def test_poker_example_TP(self):
        '''Test get result of game
        Test Two pair
        tp = ['KS','KH','2S','2C','6C']
        '''
        tp = ['KS','KH','2S','2C','6C']
        actual = poker.poker([tp])
        expected = "The Winner is [['KS', 'KH', '2S', '2C', '6C']] Rank:Two pair"
        self.assertEqual(actual, expected)
            
    def test_poker_example_OP(self):
        '''one Pair
        Test Straight Flush
        op = ['3S','3H','4S','AC','7C']
        '''
        op = ['3S','3H','4S','AC','7C']
        actual = poker.poker([op])
        expected = "The Winner is [['3S', '3H', '4S', 'AC', '7C']] Rank:One pair"
        self.assertEqual(actual, expected)
            
    def test_poker_example_FH(self):
        '''Test get result of game
        Test Full House
        fh = ['9S','9C','9D','AC','AS']
        '''
        fh = ['9S','9C','9D','AC','AS']
        actual = poker.poker([fh])
        expected = "The Winner is [['9S', '9C', '9D', 'AC', 'AS']] Rank:Fullhouse"
        self.assertEqual(actual, expected)
            
    def test_poker_example_HC(self):
        '''Test get result of game
        Test High Card
        hc = ['KH','JS','8S','7C','2D']
        '''
        hc = ['KH','JS','8S','7C','2D']
        actual = poker.poker([hc])
        expected = "The Winner is [['KH', 'JS', '8S', '7C', '2D']] Rank:Highcard"
        self.assertEqual(actual, expected)
            
    def test_poker_example_Match1(self):
        '''Test get result of game
        Test Match Between SF ,FH, TK,TP and ST
        '''
        sf = ['TS','JS','QS','KS','AS']
        fk = ['6S','6H','6D','6C','3D']
        tk = ['7H','7S','7D','3C','2S']
        tp = ['KS','KH','2S','2C','6C']
        st = ['8S','7C','6H','5H','4S']
        actual = poker.poker([sf,fk,tk,tp,st])
        expected = "The Winner is [['TS', 'JS', 'QS', 'KS', 'AS']] Rank:Straight Flush"
        self.assertEqual(actual, expected)
            
    def test_poker_example_Draw_Match(self):
        '''Test get result of game
        Test to draw between SF1,SF2

        '''
        sf1 = ['TH','JH','QH','KH','AH']
        sf2 = ['TC','JC','QC','KC','AC']
        tk = ['7H','7S','7D','3C','2S']
        tp = ['KS','KH','2S','2C','6C']
        st = ['8S','7C','6H','5H','4S']
        actual = poker.poker([sf1,sf2,tk,tp,st])
        expected = "The Winner is [['TH', 'JH', 'QH', 'KH', 'AH'], ['TC', 'JC', 'QC', 'KC', 'AC']] Rank:Straight Flush"
        self.assertEqual(actual, expected)
    
if __name__ == '__main__':
    unittest.main(exit=False)
