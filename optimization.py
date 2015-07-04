def problem_solver(n_trials=25):
     from PyGMO import problem, algorithm, island, archipelago
     from PyGMO.topology import fully_connected
     from numpy import mean, median
     import csv

     results = list()
     prob = problem.cassini_2()
     de_variants = [11,13,15,17]
     f_variants = [0, 0.2, 0.5, 0.8, 1]
     cr_variants = [0.3, 0.9]
     np_variants = [10, 25, 50]

     for f in f_variants:
         for cr in cr_variants:
             for np in np_variants:
                 algos = [algorithm.de(gen=np, f=f, cr=cr) for v in de_variants]

                 for trial in range(n_trials):
                         archi = archipelago(topology=fully_connected())
                         for algo in algos:
                                 archi.push_back(island(algo,prob,25))
                         archi.evolve(30)
                         results.append(min([isl.population.champion.f[0] for isl in archi]))

                 with open('results.csv', 'a') as out:
                    out.write('%f;' % f)
                    out.write('%f;' % cr)
                    out.write('%f;' % np)
                    out.write('\n')

                    out.write('%f;' % mean(results))
                    out.write('%f;' % median(results))
                    out.write('%f;' % min(results))
                    out.write('%f;' % max(results))
                    out.write('\n')
                 out.close()

problem_solver()
