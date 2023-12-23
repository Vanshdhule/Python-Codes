questions =[ 
    ["What is the capital of India?","Jaipur","Mumbai","New Delhi","Pune",3],

    ["Which is the national bird?", "Peacock", "Sparrow","Owl","Jaduu", 1],

    ["Which is the national animal?","Dog","Lion","Tiger","Elephant",3],

    ["Who is king of jungle?","Dog","Lion","Tiger","Elephant",2],

    ["What is the National Sport of India?","Football","Cricket","Hockey","Kabaddi",3],

    ["Which of the following monument is reconized as one of the 7 wonders of the world?","Gate way of India","Taj Mahal","Red Fort","Charminar",2],

    ["Which is the Tech Giant in India?","TCS","Infosys","Wipro","HCl",1],

    ["Which is the National Color of India?","Red","Blue","Kesari","Green",3],

    ["Which is the Parent Company of Land rover and Jaquar?","Tata","Ford","VW","GMC",1],

    ["There are how many Colors in the Rainbow?","5","7","6","8",2],

    ["What is the Color Of Andrew Tate's Buggati?","Red","Balck","Copper","Exposed Carbon Fiber",3],

    ["Which is the Smallest Prime Number?","4","3","7","2",4],

    ["Lamborgini Urus Fall under which category?","SUV","Super SUV","Compact SUV","Hyper SUV",2],

    ["There are how many Seat in the Lok Sabha?","543","542","643","256",1],

    ["Total there are how many units produced of LA FERRARI?","567","210","710","500",3]

    
]
   

levels =[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")

    print(f"{questions[i][0]}")

    print(f"1. {questions[i][1]}                  2. {questions[i][2]}")
    print(f"3. {questions[i][3]}                  4. {questions[i][4]}")

    reply = int(input("Enter your answer(1,2,3,4) : "))

    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")

        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer")
        break

print(f"your take home money is {money}")
