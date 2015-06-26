from django.conf.urls import patterns, url
from search import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search$', views.search, name='search'),
	url(r'^clicked$', views.clicked, name='clicked'),
    url(r'^metases/lnk/save$', views.savelink, name='savelink'),
    url(r'^metases/lnk/delete$', views.deleteSavedlink, name='deleteSavedLink'),
    url(r'^metases/close$', views.closeMetases, name = 'closeMetases'),
    url(r'^metases/open$', views.openMetases, name = 'openMetases'),
    url(r'^metases/save$', views.saveAndCloseMeta, name = 'saveAndCloseMeta'),
    url(r'^filter/save$', views.retrieveSearch, name='retrieveSearchSavedLinks'),
    url(r'^relevance/$', views.doRelevanceFeedback, name='doRelevanceFeedback'),
    url(r'^diversity/$', views.doDiversity, name='doDiversity'),
    url(r'^evaluation/$', views.evaluationIndex, name='evaluationIndex'),
    url(r'^evaluation/clicked/$', views.evalclicked, name='evaluationClick'),
    url(r'^evaluation/search$', views.evaluationSearch, name='evaluationSearch'),
    url(r'^evaluation/evaluate/clicks$', views.evaluateClicks, name='evaluateClicks'),
    url(r'^evaluation/evaluate/queries$', views.evaluateQueries, name='evaluateQueries'),
    url(r'^evaluation/evaluate/patk$', views.evaluatePATK, name='evaluatePAtK'),
    url(r'^evaluation/evaluate/ratk$', views.evaluateRATK, name='evaluateRAtK'),
    url(r'^evaluation/evaluate/ndcg$', views.evaluateNDCGATK, name='evaluateNDCG'),
    url(r'^evaluation/evaluate/mrr$', views.evaluateMRR, name='evaluateMRR'),
    url(r'^evaluation/evaluate/map$', views.evaluateMAP, name='evaluateMAP'),
    url(r'^evaluation/evaluate/ild$', views.evaluateILD, name='evaluateILD'),
    url(r'^evaluation/evaluate/report$', views.evalReport, name = 'evaluationReport'),
    url(r'^evaluation/diversity/$', views.evalDiversityIndex,  name='evalDiversityIndex'),
    url(r'^evaluation/diversity/search$', views.evaldoDiversity, name='evaldoDiversity'),
    url(r'^evaluation/diversity/change$', views.evalChangeDiversity, name='evalChangeDiversity'),
    url(r'^evaluation/metasearch/$', views.evalRankSymIndex,  name='evalRanksymIndex'),
    url(r'^evaluation/metasearch/search$', views.evaldoRanksym, name='evaldoRanksym'),
    url(r'^evaluation/metasearch/change$', views.evalChangeRanksym, name='evalChangeRanksym'),
)