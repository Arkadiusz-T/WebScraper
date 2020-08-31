class WinRateReport:
    def __init__(self, names_sorted, winrates_sorted, role_sorted, n_of_best_choises_for_each_role):
        self.n_of_best_choises_for_each_role = n_of_best_choises_for_each_role
        self.names_sorted = names_sorted
        self.winrates_sorted = winrates_sorted
        self.role_sorted = role_sorted

    def __repr__(self):
        """

            :return: statistically best options for each role
        """
        dictionary_with_counters = dict()
        dictionary_with_results = dict()
        for i in range(len(self.winrates_sorted)):
            if self.role_sorted[i] in dictionary_with_counters.keys() and dictionary_with_counters[self.role_sorted[i]] < self.n_of_best_choises_for_each_role:
                dictionary_with_counters[self.role_sorted[i]] += 1
                dictionary_with_results[self.role_sorted[i]].append('{}: {}'.format(self.names_sorted[i], self.winrates_sorted[i]))

            elif self.role_sorted[i] not in dictionary_with_counters.keys():
                dictionary_with_counters[self.role_sorted[i]] = 1
                dictionary_with_results[self.role_sorted[i]] = ['{}: {}'.format(self.names_sorted[i], self.winrates_sorted[i])]

        report = str()
        for key in dictionary_with_results.keys():
            report = report + '\n{}'.format(key)
            for value in dictionary_with_results[key]:
                report = report + '\n{}'.format(value)

        return report
