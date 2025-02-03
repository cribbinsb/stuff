import numpy as np
from scipy.optimize import linear_sum_assignment

def default_match(det, gt, context):
    return det.match_score(gt, context)

def match_greedy(dets, gts, mfn=default_match, mfn_context=None):
    n_gts=len(gts)
    n_dets=len(dets)

    if n_gts==0 or n_dets==0:
        return [], [], []

    gt_matched=[False]*n_gts
    out_det_index=[]
    out_gt_index=[]
    out_cost=[]
    for i,det in enumerate(dets):
        best_v=0
        best_match=None
        for j,gt in enumerate(gts):
            v=mfn(det,gt,mfn_context)
            if gt_matched[j] is False and v>best_v:
                best_v=v
                best_match=j
        if best_match is not None:
            gt_matched[best_match]=True
            out_det_index.append(i)
            out_gt_index.append(best_match)
            out_cost.append(best_v)
    return out_det_index, out_gt_index, out_cost

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