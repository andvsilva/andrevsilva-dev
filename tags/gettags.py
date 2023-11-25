from newspaper import Article

def gettag(kpaper):
    # Replace 'article_url' with the actual URL of the article
    article_url = f'https://andrevsilva.com/{kpaper}paper.html'
    article = Article(article_url)
    article.download()
    article.parse()

    # Use newspaper's built-in NLP to extract keywords
    article.nlp()

    # Get the keywords
    keywords = article.keywords
    print(f'{kpaper} paper: {keywords}')


for kpaper in range(1, 9):
    gettag(kpaper)

