from collections import deque, defaultdict

def gen_template(word):
    return [word[:i] + "*" + word[i+1:] for i in range(len(word))]

def ladder_length_impl(start_word, end_word, templates):
    to_eval = deque([(start_word, 0)])
    min_found = None

    while bool(to_eval):
        word, depth = to_eval.popleft()
        if word == end_word:
            if min_found == None:
                min_found = depth
            else:
                min_found = min(min_found, depth)
        elif min_found == None or depth + 1 < min_found:
            for template in gen_template(word):
                if template in templates:
                    for one_off in templates.pop(template, None):
                        to_eval.append((one_off, depth + 1))
    
    return 0 if min_found == None else min_found + 1

def ladder_length(start_word, end_word, words):
    if end_word not in words:
        return 0
    
    templates = defaultdict(list)
    for word in words:
        for template in gen_template(word):
            templates[template].append(word)
    
    return ladder_length_impl(start_word, end_word, templates)

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        return ladder_length(beginWord, endWord, wordList)

sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
result = sol.ladderLength(beginWord, endWord, wordList)
print(result)
