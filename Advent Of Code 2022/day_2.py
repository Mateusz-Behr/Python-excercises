with open("day_2", "r") as file:
    results = ''.join(file.readlines()).split("\n")

    scores = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    sum = 0

    for result in results:
        sum += scores[result]
        #for key, value in scores.items():
         #   if key == result:
         #       sum += value
    print(sum)

    scores_2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    sum_2 = 0

    for result in results:
        sum_2 += scores_2[result]
       # for key, value in scores_2.items():
        #    if key == result:
        #        sum_2 += value
    print(sum_2)

#X - lose Y - draw Z - win
# A - rock - (X)
# B - paper - (Y)
# C - scissors - (Z)
# win - 6 pkt
# draw - 3 pkt
# lose - 0 pkt



#    sum = 0
#    counter_A = 0
#   counter_B = 0
#    counter_C = 0
#    for result in results:
#        if result.startswith("A"):
#            sum += 1
#            counter_A +=1
#        elif result.startswith("B"):
#            sum += 2
#            counter_B += 1
#        elif result.startswith("C"):
#            sum +=3
#            counter_C += 1
#    print(sum, counter_A, counter_B, counter_C)



