def detector_anagrama(word1, word2):
    return sorted(word1) == sorted(word2)



print(detector_anagrama('car','rac'))