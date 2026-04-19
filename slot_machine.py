def spin_row():
    import random
    symbols=["⭐","💲","7️⃣"]
    return [random.choice(symbols) for i in range(3)]


def print_row(spin):
    print(" | ".join(spin))

def check_win(spin,bet):
    if spin[0]==spin[1]==spin[2]:
        print("You win!")
        return bet*10
    else:
        print("You lose!")
        return 0    

def main():
    balance=10.0
    print("Python slot machine 🎰")
    print("  ⭐  ","  7️⃣  "," 💲 ")
    print("-"*30)
    count=0
    while (balance>0):
        print(f"Your Balance: {balance:.2f}")
        bet=input("Place your bet amount: ")
        print("-"*26)
        if not bet.isdigit():
            print("Only number")
            continue
        bet=int(bet)
        if bet>balance:
            print("Balance incufficient :(")
            continue
        elif bet<0:
            print("Bet must be greater than 0")
            continue
        balance-=bet
        spin=spin_row()
        print_row(spin)
        balance+=check_win(spin,bet)
        count+=1
        if count%3==0:
            resume=input("Do you want to playagain? (y/n):").upper()
            if resume!="Y":
                break
        
    print("Game finished! Your final balance is: ",balance)
if __name__=="__main__":
    main()
