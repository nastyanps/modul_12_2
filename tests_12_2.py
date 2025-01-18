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
        print(cls.all_results)

    def test_1(self):
        race = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        results = race.start()
        self.__class__.all_results.update(results)
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)

    def test_2(self):
        race = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        results = race.start()
        self.__class__.all_results.update(results)
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)

    def test_3(self):
        race = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = race.start()
        self.__class__.all_results.update(results)
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)


if __name__ == '__main__':
    unittest.main()
