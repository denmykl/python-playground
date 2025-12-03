def calculate_love_score(name1, name2):
    name_together = name1 + name2
    word_true = ['T', 'R', 'U', 'E']
    word_love = ['L', 'O', 'V', 'E']
    
    word_true_score = 0
    word_love_score = 0
    
    for letter1 in word_true:
        count_true_word = name_together.upper().count(letter1)
        word_true_score += count_true_word
        print(f"{letter1} occurs {count_true_word} times")
        
    print(f"Total = {word_true_score}")
    
    for letter2 in word_love:
        count_love_word = name_together.upper().count(letter2)
        word_love_score += count_love_word
        print(f"{letter2} occurs {word_love_score} times")
        
    print(f"Total = {word_love_score}\n")
    
    true_love_score = str(word_true_score) + str(word_love_score)
    print(f"Love Score = {true_love_score}")
    
    
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
calculate_love_score(name1, name2)