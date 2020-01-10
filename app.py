from newsapi import NewsApiClient

#init
newsapi = NewsApiClient(api_key='901bdb65fc784ec5938c223b604113bc')


all_articles = newsapi.get_everything(q='Australia',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
 