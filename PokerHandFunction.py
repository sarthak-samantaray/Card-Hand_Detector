def findPokerHand(hand):

    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2] # This is because , if the card "10H" then card[0] will give us 1, so if there are 3 digits we will extract 0to2 index.
            suit = card[2]
        
        # we need to sort the ranks.
        if rank == "A": 
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11
        ranks.append(int(rank))
        suits.append(suit)
    
    # sort the ranks
    sortedRanks = sorted(ranks)
    
    # ROYAL FLUSH and Straight and Flush
    # we will check the count of the suit, suppose we will take h, if count of h == 5, then it flush
    if suits.count(suits[0]) == 5:
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks: # this condition is for royal flush
            possibleRanks.append(10) # ROYAL FLUSH
        elif all(sortedRanks[i]  == sortedRanks[i-1]+1 for i in range(1,len(sortedRanks))):
            possibleRanks.append(9) # STRAIGHT FLUSH
        else:
            possibleRanks.append(6) # FLUSH

    # Straight 10,11,12,13,14
    # 11 == 10+1 ,TRUE
    # 12 == 11+1 ,TRUE
    if all(sortedRanks[i]  == sortedRanks[i-1]+1 for i in range(1,len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueVals = list(set(sortedRanks))


    # Four of a kind and Full House
    # 3 3 3 3 5   -- set --- 3 5 --- unique values = 2 --- Four of a kind
    # 3 3 3 5 5   -- set -- 3 5 ---- unique values = 2 --- Full house
    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 4: # FOUR OF A KIND
                possibleRanks.append(8)
            if sortedRanks.count(val) == 3: # FULL HOUSE
                possibleRanks.append(7)

    # Three of a Kind and Pair
    # 5 5 5 6 7 -- set -- 5 6 7 --- unique values = 3   -- three of a kind
    # 8 8 7 7 2 -- set -- 8 7 2 --- unique values = 3   -- two pair
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3:  # -- three of a kind
                possibleRanks.append(4)
            if sortedRanks.count(val) == 2:  # -- two pair
                possibleRanks.append(3)

    # Pair
    # 5 5 3 6 7 -- set -- 5 3 6 7 - unique values = 4 -- Pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)

    if not possibleRanks: # if possible ranks is empty
        possibleRanks.append(1)

    
    pokerHandRanks = {10:"Royal Flush", 9:"Straight Flush",8:"Four of a kind",7:"Full House",6:"Flush",5:"Straight",4:"Three of a Kind",3:"Two Pair",2:"Pair",1:"High Card"}
    output = pokerHandRanks[max(possibleRanks)]
    print(hand , output)
    return output ,pokerHandRanks


if __name__ == "__main__":
    findPokerHand(["AH","KH","QH","JH","10H"]) # ROYALE FLUSH
    findPokerHand(["QC","JC","10C","9C","8C"]) # STRAIGHT FLUSH
    findPokerHand(["5C","5S","5H","5D","QH"]) # FOUR A KIND
    findPokerHand(["2H","2D","2S","10H","10C"]) # FULL HOUSE
    findPokerHand(["2D","KD","7D","6D","5D"])  # FLUSH
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card