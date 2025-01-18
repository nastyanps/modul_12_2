import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    def test_1(self):
        race = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        results = race.start()
        formatted_results = {place: runner.name for place, runner in results.items()}
        self.__class__.all_results['test_1'] = formatted_results
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)

    def test_2(self):
        race = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        results = race.start()
        formatted_results = {place: runner.name for place, runner in results.items()}
        self.__class__.all_results['test_2'] = formatted_results
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)

    def test_3(self):
        race = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = race.start()
        formatted_results = {place: runner.name for place, runner in results.items()}
        self.__class__.all_results['test_3'] = formatted_results
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)


if __name__ == '__main__':
    unittest.main()
