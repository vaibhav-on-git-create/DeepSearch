def make_word_combset(string : str , max_pair : int):
    string_1 = [j for j in string] 
    pairs_list = []

    count = len(string_1)
    pointer = 0
    want = max_pair

    while pointer < count:
        temp = []

        for i in range(want):
            pointer_index = pointer + i
            try:
                temp.append(string_1[pointer_index])
            except IndexError:
                pass
            
        letters = "".join(temp)
        if len(letters) == want :
            pairs_list.append(letters)

        pointer += 1
    
    return pairs_list

# print(make_word_combset(string="happy" , max_pair=4))

def generate_pair_seq(string : str):
    len_word = len(string)
    counter = 0
    want = 2

    score = 1
    incre = 1

    lst = []
    while counter < len_word:
        if want < len_word:
            lst.append({score:make_word_combset(string=string , max_pair=want)})
            score+= incre

        want+=1
        counter += 1

    return lst

# print(generate_pair_seq(string="vaibhav"))

def match_words(main_word : str , match_word : str):
    pair_seq = generate_pair_seq(string=match_word)
    score_seq = []
    for seq_1 in pair_seq:
        key = list(seq_1.keys())[0]
        score_seq.append(key)
    # print(score_seq)
    #calulating total score
    total_score_per_section = []
    seq_counter = 0
    while seq_counter < len(pair_seq):
        total_score_per_section.append(score_seq[seq_counter]*len(pair_seq[seq_counter][score_seq[seq_counter]]))
        seq_counter += 1

    total_score = sum(total_score_per_section)

    word_score = 0
    counter = 0
    while counter < len(pair_seq):
        used_matchers = []
        grade_score = score_seq[counter]
        for i in score_seq:
            match_list = pair_seq[counter][score_seq[counter]]
            for matcher in match_list:
                if matcher in main_word:
                    if matcher not in used_matchers:
                        word_score += grade_score
                        used_matchers.append(matcher)
            
        counter += 1
   
    percent = (word_score/total_score)*100
    return percent

# print(match_words(main_word="vaibhav123455" , match_word="vaibhav123455"))





