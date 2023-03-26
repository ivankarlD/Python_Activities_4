def NumberedCard(playerCards, oppCards) :
    playerCards.sort(reverse=True)
    oppCards.sort(reverse=True)
    playerCardsHigh=int(str(playerCards[0]) + str(playerCards[1]))
    oppCardsHigh=int(str(oppCards[0]) + str(oppCards[1]))
    if playerCardsHigh > oppCardsHigh : return True
    else : return False

print(NumberedCard([2,3,4,5,1], [3,7,1,0,6]))