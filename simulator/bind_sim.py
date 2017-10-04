
from crypto.simulator.base_sim import BaseSim


class BINDSim(BaseSim):
    """
    This simulator was written to be used with GameBIND. It simulates the
    game with an Adversary and allows you to compute an approximate advantage.
    """

    def run(self):
        """
        Runs the game with the adversary provided to the constructor.

        :return: True for success and False for failure.
        """
        self.game.initialize()
        return self.game.finalize(self.adversary(self.game.pi))

    def compute_success_ratio(self):
        """
        Runs the game 10 times and computes the ratio of successful runs
        over total runs. This is fewer runs than usual because RSA math is
        expensive/slow.

        :return: successes / total_runs
        """
        results = []
        for i in xrange(0, 10):
            results += [self.run()]

        successes = float(results.count(True))
        failures = float(results.count(False))

        return successes / (successes + failures)

    def compute_advantage(self):
        """
        Adv = Pr[Bind => true]

        :return: Approximate advantage computed using the above equation.
        """

        return self.compute_success_ratio()