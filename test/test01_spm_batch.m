% Perform single-subject fMRI analysis. Results are used to build test01 of
% the NeuroImaging Data Model (NIDM)
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

funcDir = fullfile(dataDir, 'fM00223');
funcFiles = cellstr(spm_select('FPList', funcDir, '^fM.*\.img$'));
anatFile = spm_select('FPList', fullfile(dataDir,'sM00223'), '^s.*\.img$') ;

matlabbatch = {};

% --- Perform pre-processing if not already done
auditory_preproc_spm_batch

smoothedFiles = strcat(fullfile(funcDir, 'swr'), spm_str_manip(funcFiles, 't'));

% New folder for test01
analysisDir = fullfile(spm_str_manip(dataDir, 'h'), 'test01');
if ~exist(analysisDir, 'dir')
    mkdir(analysisDir)
end

% --- fMRI analysis
matlabbatch{end+1}.spm.stats.fmri_spec.dir = {analysisDir};
matlabbatch{end}.spm.stats.fmri_spec.timing.units = 'scans';
matlabbatch{end}.spm.stats.fmri_spec.timing.RT = 7;
% Dependency on smoothed image
matlabbatch{end}.spm.stats.fmri_spec.sess.scans = smoothedFiles;
matlabbatch{end}.spm.stats.fmri_spec.sess.cond.name = 'active';
matlabbatch{end}.spm.stats.fmri_spec.sess.cond.onset = [6
                                                      18
                                                      30
                                                      42
                                                      54
                                                      66
                                                      78];
matlabbatch{end}.spm.stats.fmri_spec.sess.cond.duration = 6;

% Cannot use dependency as batch might be different if pre-processing are
% performed now or not
spmMat = fullfile(analysisDir, 'SPM.mat');
matlabbatch{end+1}.spm.stats.fmri_est.spmmat{1} = spmMat;

% --- Specify contrasts
% Dependency on estimated model
matlabbatch{end+1}.spm.stats.con.spmmat{1} = spmMat;
matlabbatch{end}.spm.stats.con.consess{1}.tcon.name = 'passine listening > rest';
matlabbatch{end}.spm.stats.con.consess{1}.tcon.weights = 1;

% --- Inference
% Dependency on estimated model after contrast definition
matlabbatch{end+1}.spm.stats.results.spmmat{1} = spmMat;
matlabbatch{end}.spm.stats.results.conspec.contrasts = 1;
matlabbatch{end}.spm.stats.results.conspec.threshdesc = 'FWE';
matlabbatch{end}.spm.stats.results.conspec.thresh = 0.05;
matlabbatch{end}.spm.stats.results.write.tspm.basename = 'thresh';

spm_jobman('run', matlabbatch);

% % Rename excursion set file
% movefile(fullfile(analysisDir, 'spmT_0001_thresh.nii'), fullfile(analysisDir, 'thresh_spmT_0001.nii'))
% Gzip all nifti files
niiFiles = cellstr(spm_select('FPList', analysisDir, '.*.nii$'));
gzip(niiFiles)

% Ad-hoc code to write automatically peaks and clusters (otherwise very 
% long manually...)
numPeaks = size(TabDat.dat, 1);
clusterId = 0;
for i = 1:numPeaks
    if ~isempty(TabDat.dat{i,3})
        % New cluster        
        clusterId = clusterId + 1;
        strClusterId = num2str(clusterId, '%04g');
        disp(['entity(niiri:cluster_' strClusterId ','])
        disp(['  [prov:type = ''spm:ClusterStatistic'','])
        disp(['  prov:label = "Cluster Statistic: ' strClusterId '" %% xsd:string,'])
        clusterSizeInVoxels = TabDat.dat{i,5};
        disp(['  nidm:clusterSizeInVoxels = "' num2str(clusterSizeInVoxels) '" %% xsd:int,'])
        disp(['  nidm:labelId = "' num2str(clusterId) '",'])
        reselSizeInVoxels = TabDat.ftr{9,2}(end);
        disp(['  spm:clusterSizeInResels = "' num2str(clusterSizeInVoxels/reselSizeInVoxels) '" %% xsd:float,'])
        disp(['  nidm:pValueUncorrected = "' num2str(TabDat.dat{i,6}) '" %% xsd:float,'])
        disp(['  spm:pValueFWER = "' num2str(TabDat.dat{i,3}) '" %% xsd:float,'])
        disp(['  spm:qValueFDR = "' num2str(TabDat.dat{i,4}) '" %% xsd:float])'])
        disp(['wasDerivedFrom(niiri:cluster_' strClusterId ', niiri:set_statistic_id)'])
    end
    
    strPeakId = num2str(i, '%04g');
    disp(['entity(niiri:peak_' strPeakId ',']);
    disp('  [prov:type = ''spm:PeakStatistic'',')
    disp(['  prov:label = "Peak Statistic: ' strPeakId '" %% xsd:string,'])
    disp(['  prov:location = ''niiri:coordinate_' strPeakId ''','])
    disp(['  prov:value = "' num2str(TabDat.dat{i,9}) '" %% xsd:float,'])
    disp(['  nidm:equivalentZStatistic = "' num2str(TabDat.dat{i,10}) '" %% xsd:float,'])
    disp(['  nidm:pValueUncorrected = "' num2str(TabDat.dat{i,11}) '" %% xsd:float,'])
    disp(['  spm:pValueFWER = "' num2str(TabDat.dat{i,7}) '" %% xsd:float,'])
    disp(['  spm:qValueFDR = "' num2str(TabDat.dat{i,8}) '" %% xsd:float])'])
    disp(['entity(niiri:coordinate_' strPeakId ','])
    disp('  [prov:type = ''prov:location'',')
    disp('  prov:type = ''nidm:coordinate'',')
    disp(['  prov:label = "Coordinate: ' strPeakId '" %% xsd:string,'])
    disp(['  nidm:coordinate1 = "' num2str(TabDat.dat{i,12}(1)) '" %% xsd:float,'])
    disp(['  nidm:coordinate2 = "' num2str(TabDat.dat{i,12}(2)) '" %% xsd:float,'])
    disp(['  nidm:coordinate3 = "' num2str(TabDat.dat{i,12}(3)) '" %% xsd:float])'])
    disp(['wasDerivedFrom(niiri:peak_' strPeakId ', niiri:cluster_' strClusterId ')   '])
end
aa=1