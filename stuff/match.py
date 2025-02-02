import numpy as np
from scipy.optimize import linear_sum_assignment

def default_match(det, gt, context):
    return det.match_score(gt, context)

def match_lsa(dets, gts, mfn=default_match, mfn_context=None):
    n_gts=len(gts)
    n_dets=len(dets)

    if n_gts==0 or n_dets==0:
        return [], [], []
    
    costs = [[0 for x in range(n_dets)] for y in range(n_gts)]
    for ii in range(n_gts):
        for jj in range(n_dets):
            if dets[jj] is not None and gts[ii] is not None:
                costs[ii][jj]=mfn(dets[jj], gts[ii], mfn_context)
    costs = np.array(costs)
    gt_ind, det_ind = linear_sum_assignment(np.array(costs), maximize=True)
    match_costs = costs[gt_ind, det_ind]

    return det_ind, gt_ind, match_costs