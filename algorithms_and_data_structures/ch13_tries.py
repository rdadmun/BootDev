# Tries
# In Python, a trie is easily implemented as a nested tree of dictionaries where each key is a 
# character that maps to the next character in a word. For example, the words:
    # hello
    # help
    # hi
# Would be represented as:

{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}
# The * character is used to indicate the end of a word.

# First Pass - Add
class Trie:
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

# Exists
    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return self.end_symbol in current
    
# Words with Prefix
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for key in sorted(current_level.keys()):
            if key != self.end_symbol:
                self.search_level(current_level[key], current_prefix + key, words)
        return words
    
    def words_with_prefix(self, prefix):
        lst = []
        current = self.root
        for char in prefix:
            if char not in current:
                return []
            current = current[char]
        return self.search_level(current, prefix, lst)  
    
# Find Matches
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char not in level:
                    break
                level = level[char]
                if self.end_symbol in level:
                    matches.add(document[i:j+1])
        return matches

# Challenge 1 - Longest Common Prefix
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = list(current.keys())
            if self.end_symbol in children:
                break
            if len(children) == 1:
                char = children[0]
                prefix += char
                current = current[char]
            else:
                break
        return prefix
    
# Challenge 2 - Advanced String Matching
def advanced_find_matches(self, document, variations):
        matches = set()
        document = document.lower()
        for i in range(len(document)):
            level = self.root
            word_variant = ""
            for j in range(i, len(document)):
                char = document[j]
                if char in variations:
                    possible_chars = variations[char]
                else:
                    possible_chars = char

                found = False
                for replacement in possible_chars:
                    if replacement in level:
                        level = level[replacement]
                        word_variant += char
                        found = True
                        break

                if not found:
                    break

                if self.end_symbol in level:
                    matches.add(word_variant)
        return matches