### Template files for NIDM entity, activity and agents

These template files are used by the scripts `create_[fsl|spm]_example_xxx.py` (in nidm/nidm-results/scripts) to generate the examples stored in nidm/nidm-results/fsl and nidm/nidm-results/spm.

#### List of template files
- `StatisticMap.txt`: required attributes for a `StatisticMap` entity.
- `StatisticMap_T.txt`: required attributes for a `StatisticMap` entity with `statisticType` equals to `TStatistic` (on top of required attributes from `StatisticMap.txt`).
- `StatisticMap_PseudoT.txt`: required attributes for a `StatisticMap` entity with `statisticType` equals to `PseudoTStatistic` (on top of required attributes from `StatisticMap.txt`).