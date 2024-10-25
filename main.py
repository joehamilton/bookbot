def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(splitToWords(file_contents))
        wordOccourances = occourances(file_contents.split())
        
        for key, value in wordOccourances.items() :
            print(f"{key} was found {value} times.")

def splitToWords(s) :
    return len(s.split())

def occourances(w) :
    wordDictionary = {}
    for word in w:
        word = word.lower()
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sorted_by_values = dict(sorted(wordDictionary.items(), key=lambda item: item[1], reverse=False))
    return sorted_by_values

main()

