def countvow():
    with open('Books.txt', 'r') as f:
        S = f.read().replace("\n", ' ')
        count = 0
        for i in S.split():
            if i[0].lower() in ['a','e','i','o','u']:
                count += 1
    return count


print("Count of words starting with a vowel =",countvow())
