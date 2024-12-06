import unittest
import run_2


class TournamentTest(unittest.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = run_2.Runner('Усэйн', 10)
        self.andrey = run_2.Runner('Андрей', 9)
        self.nik = run_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    def test_1(self):
        tournament = run_2.Tournament(90, self.usain, self.nik)
        result = tournament.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_2(self):
        tournament = run_2.Tournament(90, self.andrey, self.nik)
        result = tournament.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    def test_3(self):
        tournament = run_2.Tournament(90, self.andrey, self.usain, self.nik)
        result = tournament.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()