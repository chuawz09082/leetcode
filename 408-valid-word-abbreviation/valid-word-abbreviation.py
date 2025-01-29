class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Checks if a given abbreviation (abbr) is a valid abbreviation of the word.
        
        :param word: The original word to be checked against the abbreviation.
        :param abbr: The abbreviation string containing letters and numbers.
        :return: True if abbr is a valid abbreviation of word, otherwise False.
        """
        
        # Pointers to track positions in 'word' and 'abbr'
        startabbr = 0  # Pointer for abbreviation
        startword = 0  # Pointer for word
        
        # Iterate through both 'word' and 'abbr'
        while startabbr < len(abbr) and startword < len(word):
            
            # If the current character in abbr is NOT a digit
            if not abbr[startabbr].isdigit():
                # Directly compare the character in 'word' and 'abbr'
                if word[startword] != abbr[startabbr]:
                    return False  # Mismatch, invalid abbreviation
                else:
                    # Move to the next character in both 'word' and 'abbr'
                    startword += 1
                    startabbr += 1
            
            else:
                # If the abbreviation starts with '0', it's invalid (e.g., "01" is not a valid abbreviation)
                if int(abbr[startabbr]) == 0:
                    return False
                
                # Locate the full numeric substring in 'abbr'
                endabbr = startabbr  # Pointer to track the end of the number
                while endabbr < len(abbr) and abbr[endabbr].isdigit():
                    endabbr += 1  # Expand to get the full number
                
                # Convert the extracted numeric substring into an integer
                currint = int(abbr[startabbr:endabbr])
                
                # Move the word pointer forward by the extracted integer (skip characters)
                startword += currint
                
                # Move the abbreviation pointer past the numeric substring
                startabbr = endabbr
        
        # Ensure both pointers reached the end of their respective strings
        return len(word) == startword and len(abbr) == startabbr
        