from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class DocumentType(grok.GlobalUtility):
    grok.name('wcc.document.document_type')
    grok.implements(IVocabularyFactory)

    _terms = [
        'Advocacy report',
        'Article - News item',
        'Background document',
        'Declaration of faith',
        'Incoming letter',
        'Lecture - Speech',
        'Liturgical song - music',
        'Liturgical text',
        'Letter',
        'Message',
        'Minutes',
        'Pastoral letter',
        'Policy document',
        'Report',
        'Response to study document',
        'Sermon',
        'Statement: letter',
        'Statement: minute',
        'Statement: public statement',
        'Study document',
        'Tribute',
    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(i, i, i))
        return SimpleVocabulary(terms)
