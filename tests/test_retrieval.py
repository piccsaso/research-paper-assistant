import unittest
from src.retrieval import Passage, retrieve, context_pack
from run import evaluate


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.passages = [Passage('transit:1','Transit depth measures a decrease in stellar brightness.'),
                         Passage('spectra:1','Spectroscopy measures absorption lines by wavelength.')]

    def test_relevant_passage_ranks_first(self):
        self.assertEqual(retrieve('transit depth',self.passages)[0]['citation'],'transit:1')

    def test_unrelated_and_stopword_queries_return_no_evidence(self):
        for question in ['basketball champion','the and of','']:
            self.assertEqual(retrieve(question,self.passages),[])

    def test_context_retains_exact_citation_and_text(self):
        pack = context_pack('depth',retrieve('depth',self.passages))
        self.assertIn('[transit:1]',pack)
        self.assertIn(self.passages[0].text,pack)

    def test_evaluation_distinguishes_hit_and_miss(self):
        cases = [{'question':'depth','expected_citation':'transit:1'},
                 {'question':'depth','expected_citation':'spectra:1'},
                 {'question':'football','expected_citation':''}]
        result = evaluate(self.passages,cases,1)
        self.assertEqual(result['answerable_hit_rate_at_k'],0.5)
        self.assertEqual(result['unrelated_zero_overlap_rate'],1)
