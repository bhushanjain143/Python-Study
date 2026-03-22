quations = [
["Which planet is known as the Red Planet?","Saturn","Jupiter","Mars","Venus",3],
["In the game of Kabaddi, what must a player hold while raiding the opponent's court?","A ball","A whistle","Their hands","Their breath",4],
["Which city is hosting the AI Action Summit in 2025?","Paris","New York","Tokyo","New Delhi",1],
["Who was the first woman to become the Chief Election Commissioner of India?","Kiran Bedi"," V. S. Ramadevi","Anna George Malhotra","Punita Arora",2],
["Which country officially became the 21st member of the Eurozone on January 1, 2026?","Romania","Croatia","Bulgaria","Serbia",3],
["Which organization released the \"Global Risk Report 2026\" identifying geoeconomic confrontation as a top threat?","World Economic Forum","World Bank","International Monetary Fund","United Nations",1],
["In 1860, who became the first Auditor General of India?","Sir A. F. Cox"," Sir Edmund Drummond","Lord Salisbury","Sir Proby Cautley",2],
["Which 2025 film won the Dadasaheb Phalke International Film Festival Award for Best Film?","Stree 2","12th Fail","Laapataa Ladies","Kalki 2898 AD",2],
]

prizes = [1000,2000,3000,4000,5000,6000,7000,8000,10000]
sum = 0
i = 0
for quation in quations:
    print(quation[0])
    print(f"a. {quation[1]}")
    print(f"b. {quation[2]}")
    print(f"c. {quation[3]}")
    print(f"d. {quation[4]}")
    
    user_option = int(input("Entrt you answer. 1 for a, 2 for b, 3 for c, 4 for d: \n"))
    if(user_option == quation[5]):
        print("Correct Answer.")
    else:
        print(f"Incorrect, the correct answer was {quation[5]}.")
        print("Better luck next time")
        break
    print(f"Yor won : {prizes[i]} \n")
    sum += prizes[i]
    i += 1
    print(sum)
    
    