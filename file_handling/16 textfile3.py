def countvow():
    with open('Books.txt', 'r') as f:
        S = f.read().replace("\n", ' ')
        count = 0
        for i in S.split():
            if i[0].lower() in ['a','e','i','o','u']:
                count += 1
    return count


print("Count of words starting with a vowel =",countvow())


"""Books.txt
Hey Kids! Let me tell you a little story.
Once upon a time there was a melon
It was named as coco by the kids
It became amazingly famous
"""