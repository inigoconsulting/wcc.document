from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class DocumentOwner(grok.GlobalUtility):
    grok.name('wcc.document.document_owner')
    grok.implements(IVocabularyFactory)

    _terms = [
        'Assembly',
        'Central Committee',
        'Commission on Faith and Order',
        'Commission on International Affairs',
        'Commission on World Mission and Evangelism',
        'Conference on World Mission and Evangelism',
        'Continuation Committee on Ecumenism in the 21st Century',
        'Echos - Commission on youth in the ecumenical movement',
        'Executive committee',
        'General Secretary',
        'International Ecumenical Peace Convocation',
        'Inter-Religious Relations and Dialogue',
        'Joint Consultative Commission WCC - Christian World Communions',
        'Joint Consultative Group Pentecostals - WCC',
        'Joint Working Group',
        'Member church',
        'Moderator of Central Committee',
        'Other ecumenical bodies',
        'Report of the Joint Consultative Group Pentecostals - WCC',
        'Special Commission on Orthodox participation in the WCC',
        'WCC Commisions',
        'WCC Officers',
        'WCC Presidents',
        'WCC Programmes',
        'Wider ecumenical movement (incl WCC)'
    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(i,i,i))
        return SimpleVocabulary(terms)
