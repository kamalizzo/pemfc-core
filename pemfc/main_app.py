import sys
import os
import inspect
import json
import numpy as np
import timeit
# from pemfc.data import input_dicts

# Location of this file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Location of main executing file
run_location = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(sys.argv[0])))
# if run_location == __location__:
if __name__ == "__main__":
    from src import simulation
else:
    from .src import simulation
# import .src.simulation as simulation

np.set_printoptions(threshold=sys.maxsize, linewidth=10000,
                    precision=9, suppress=True)
np.seterr(all='raise')


def main(settings=None):
    np.seterr(all='raise')
    start_time = timeit.default_timer()
    sim = simulation.Simulation(settings=settings)
    sim.timing['start'] = start_time
    sim.timing['initialization'] = timeit.default_timer()
    # simulation.timing['start'] = start_time
    g_data, l_data = sim.run()
    # sim.output.print_global_data(sim, g_data)
    sim.output.save_settings(sim.settings)
    return g_data, l_data, sim


if __name__ == "__main__":
    # base_dir = \
    #    os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0)))
    base_dir = 'ZBT/pemfc-core/pemfc/settings/setting.json'
    # with open(os.path.join(base_dir, 'settings', 'settings.json')) as file:
    with open(base_dir) as file:
        settings = json.load(file)
    # settings = input_dicts.sim_dict
    # with open(os.path.join(base_dir, 'settings', 'settings.json'), 'w') as file:
    #     json.dump(settings, file, indent=4)
    global_data, local_data, sim = main(settings)

