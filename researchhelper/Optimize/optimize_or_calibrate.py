"""Optimization algorithms."""

import numpy as np
import tqdm


def metro_hast(
        tdata, N, sim_setting, perturb_setting, sim_func, perturb_func, score_func
):
    """Metropolis hastings algorithm that samples parameter space.

    Parameters
    ----------
    tdata : np.array
        True dataset on which the score function calculates its value.
    N : int
        Number of iterations the metropolist hastings algorithm performs.
    sim_setting : dict
        Dictionary of settings needed for the simulation.
    perturb_setting : dict
        Dictionary of settings needed for the perturbation function.
    sim_func : function
        Function that performs the actual simulation with np.array output.
    perturb_func : function
        Function that perturbs variable inputs into simulation function.
    score_func : function
        Function that calculates a score from the fit between real data and
        simulated data.

    Returns
    -------
    sim_settings : np.array
        Set of variable settings that were sampled.
    all_data : np.array
        Generated data from the previous settings.
    scores : np.array
        Scores according to provided score function regarding data fit.
    """
    # start simulation
    all_data = [sim_func(**sim_setting)[1]]
    scores = [score_func(tdata, all_data[-1])]
    sim_settings = [sim_setting]

    for i in tqdm(range(N)):
        # Perturb parameters slightly
        new_settings = perturb_func(sim_settings[-1].copy(), perturb_setting)
        # Run simulation
        new_data = sim_func(**new_settings)[1]
        # Calculate score
        new_score = score_func(tdata, new_data)
        # See if score is better than the last iteration and keep if it is
        if new_score <= scores[-1]:
            sim_settings.append(new_settings)
            all_data.append(new_data)
            scores.append(new_score)
        # Or else give a random chance to still be accepted
        else:
            random = np.random.rand()
            if random < scores[-1] / new_score:
                sim_settings.append(new_settings)
                all_data.append(new_data)
                scores.append(new_score)
    return np.array(sim_settings), np.array(all_data), np.array(scores)
