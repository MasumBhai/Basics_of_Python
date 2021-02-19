def main():
    print("Hi,I'm Masum Bhai Speaking...")
    failure = "Successful"
    print("I was a ",failure," student in my university life :')")

    def fun_Testing():
        x = 1
        while (x < 5):
            print("After ",x," year in university,I was like 'WoW,Great. Next Term, i will do better :-)'")
            if (x==4):
                break
            print("   One year consists 2 term, So I have enough Time. Now,Just Chill")
            for i in range(1,3):
                print("        After ",i," term ... Next term 'Kopp...Now Just Chill'")
                days = ['Sunday','Monday','Tuesday','Wednesday','Thusday','Friday','Saturday']
                for i,d in enumerate(days):
                    print("              ",d,"passes I used to think... Okay,I will study Next Day,Chill ")
                print("                   Okay next Week 'Kopp'")
            x+=1
        print("And The Next year and next Term didn't come :\")")
        print("feeling betrayed.")

    fun_Testing()
if __name__ == "__main__":
    main()