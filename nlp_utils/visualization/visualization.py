from wordcloud import WordCloud

def word_cloud(text, ngram=1):
    word_cloud = WordCloud(
        width=1400,
        height=800,
        random_state=42,
        background_color='black'
        )
    
    if ngram == 1:
        wordc = word_cloud.generate(' '.join(text))
    else:
        wordc = word_cloud.generate_from_frequencies(text)
    plt.figure(figsize=(12,6), facecolor='k')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)