class Sol:
    def find_words(self,words):
        first_row=['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P','q','a']
        sec_row=['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
        third_row=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
        l=[]

        for word in words:
            if word[0] in first_row:
                row=first_row
            elif word[0] in sec_row:
                row=sec_row
            else:
                row = third_row

            for char in word:
                if char not in row:
                    l.append(word)
        return list(set(words)-set(l))
