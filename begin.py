from xgoogle.search import GoogleSearch
gs = GoogleSearch("cat facts")
gs.results_per_page = 10
results = gs.get_results()
for res in results:
	print res.title.encode('utf8')
