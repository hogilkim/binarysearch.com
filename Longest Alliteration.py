class Solution:
    def solve(self, words):
        prev_char = ""
        count = 0
        max_count = 0
        for word in words:
            if prev_char == "":
                prev_char = word[0]
                count += 1
            elif prev_char == word[0]:
                count += 1
            else:
                prev_char = word[0]
                count = 1
            max_count = max(max_count, count)
        return max_count


        # if len(words) == 0:
        #     return 0
        # sublist_len = 1
        # same_first_letter_list = [words[0][0]]
        # max_len = 1
        # for i in range(1, len(words)):
        #     sharing_string = words[i][0]
        #     if same_first_letter_list[0][0] != sharing_string:
        #         sublist_len = 1
        #         same_first_letter_list = [sharing_string]
        #     elif same_first_letter_list[0][0] == sharing_string:
        #         sublist_len += 1
        #         same_first_letter_list.append(sharing_string)
        #         max_len = max(max_len, len(same_first_letter_list))
        
        # return max_len