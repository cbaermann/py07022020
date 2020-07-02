import requests

def main():
    player_game_score = 0
    
    for x in range(0,10):
        request_jeporady_fact = requests.get("http://jservice.io/api/random")
        random_fact = request_jeporady_fact.json()
        print(random_fact[0]["question"])
        print(random_fact[0]["answer"])
        actual_answer = random_fact[0]["answer"].lower()
        player_answer = input("Enter your answer \n").lower()

        if(player_answer == actual_answer):
            print("You are correct!!!")
            player_game_score += 1

        else:
            print("How about you read a book sometime")
            player_game_score -= 1
            
    print(f'Your score is {player_game_score}')


main()