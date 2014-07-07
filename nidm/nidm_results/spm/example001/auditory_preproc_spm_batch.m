% Perform pre-processing for single-subject fMRI analysis. Pre-processed 
% data is used in tests of the NeuroImaging Data Model (NIDM)
% 
% To run this test download the data available at 
% http://www.fil.ion.ucl.ac.uk/spm/data/auditory/ and create a function
% config_data_path.m returning a string containing the path to the data.
%_______________________________________________________________________

% Copyright (C) 2014 The University of Warwick
% Camille Maumet
% Based on auditory_spm5_batch.m available at 
% http://www.fil.ion.ucl.ac.uk/spm/data/auditory/

% % Uncomment tp initialise SPM (and SPM batch in particular)
% spm fmri

% Path to original data directory
dataDir = test_config();

funcFiles = cellstr(spm_select('FPList', fullfile(dataDir, 'fM00223'), '^fM.*\.img$'));
anatFile = spm_select('FPList', fullfile(dataDir,'sM00223'), '^s.*\.img$') ;

lastSmoothFile = fullfile(spm_str_manip(funcFiles{end}, 'h'), ['swr' spm_str_manip(funcFiles{end}, 't')]);

if exist(lastSmoothFile, 'file') ~=2
    clear matlabbatch

    % --- Spatial realignment
    matlabbatch{1}.spm.spatial.realign.estwrite.data = {funcFiles};

    % --- Coregistration
    % Dependency on mean of spatial realignment
    matlabbatch{2}.spm.spatial.coreg.estimate.ref(1) = cfg_dep('Realign: Estimate & Reslice: Mean Image', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','rmean'));
    matlabbatch{2}.spm.spatial.coreg.estimate.source = {anatFile};

    % --- Segmentation
    % Dependency on coregistered structural file
    matlabbatch{3}.spm.tools.oldseg.data(1) = cfg_dep('Coregister: Estimate: Coregistered Images', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','cfiles'));

    % --- Normalised functional images
    % Dependency on previously estimated normalisation parameters (segmentation
    % step)
    matlabbatch{4}.spm.tools.oldnorm.write.subj.matname(1) = cfg_dep('Old Segment: Norm Params Subj->MNI', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','snfile', '()',{':'}));
    % Dependency on realigned and resliced functional files
    matlabbatch{4}.spm.tools.oldnorm.write.subj.resample(1) = cfg_dep('Realign: Estimate & Reslice: Resliced Images (Sess 1)', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','sess', '()',{1}, '.','rfiles'));
    
    matlabbatch{4}.spm.tools.oldnorm.write.roptions.vox = [3 3 3];

    % --- Smooth functional images
    matlabbatch{5}.spm.spatial.smooth.data(1) = cfg_dep('Old Normalise: Write: Normalised Images (Subj 1)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));

    spm_jobman('run', matlabbatch);
else
    disp('Pre-processing on auditory data already computed')
end