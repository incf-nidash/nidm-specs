% Ad-hoc code to write automatically peaks and clusters and statistical 
% image properties (otherwise very long manually...)

disp(['entity(niiri:stat_image_properties_id,'])
disp(['  [prov:type = ''spm:StatisticImageProperties'','])
disp(['  prov:label = "Statistical image properties",'])
disp(['  spm:expectedNumberOfVoxelsPerCluster = "' mat2str(TabDat.ftr{3,2}) '" %% xsd:float,'])
disp(['  spm:expectedNumberOfClusters = "' mat2str(TabDat.ftr{4,2}) '" %% xsd:float,'])
disp(['  spm:heightCriticalThresholdFWE05 = "' mat2str(TabDat.ftr{5,2}(1)) '" %% xsd:float,'])
disp(['  spm:heightCriticalThresholdFDR05 = "' mat2str(TabDat.ftr{5,2}(2)) '" %% xsd:float,'])
disp(['  spm:smallestSignifClusterSizeInVoxelsFWE05 = "' mat2str(TabDat.ftr{5,2}(3)) '" %% xsd:float,'])
disp(['  spm:smallestSignifClusterSizeInVoxelsFDR05 = "' mat2str(TabDat.ftr{5,2}(4)) '" %% xsd:float])'])

numPeaks = size(TabDat.dat, 1);
clusterId = 0;
for i = 1:numPeaks
    if ~isempty(TabDat.dat{i,3})
        % New cluster        
        clusterId = clusterId + 1;
        strClusterId = num2str(clusterId, '%04g');
        disp(['entity(niiri:cluster_' strClusterId ','])
        disp(['  [prov:type = ''nidm:ClusterStatistic'','])
        disp(['  prov:label = "Cluster Statistic: ' strClusterId '" %% xsd:string,'])
        clusterSizeInVoxels = TabDat.dat{i,5};
        disp(['  nidm:clusterSizeInVoxels = "' mat2str(clusterSizeInVoxels) '" %% xsd:int,'])
        disp(['  nidm:clusterLabelId = "' mat2str(clusterId) '",'])
        reselSizeInVoxels = TabDat.ftr{9,2}(end);
        disp(['  spm:clusterSizeInResels = "' mat2str(clusterSizeInVoxels/reselSizeInVoxels) '" %% xsd:float,'])
        disp(['  nidm:pValueUncorrected = "' mat2str(TabDat.dat{i,6}) '" %% xsd:float,'])
        disp(['  nidm:pValueFWER = "' mat2str(TabDat.dat{i,3}) '" %% xsd:float,'])
        disp(['  nidm:qValueFDR = "' mat2str(TabDat.dat{i,4}) '" %% xsd:float])'])
        disp(['wasDerivedFrom(niiri:cluster_' strClusterId ', niiri:set_statistic_id)'])
    end
    
    strPeakId = num2str(i, '%04g');
    disp(['entity(niiri:peak_' strPeakId ',']);
    disp('  [prov:type = ''nidm:PeakStatistic'',')
    disp(['  prov:label = "Peak Statistic: ' strPeakId '" %% xsd:string,'])
    disp(['  prov:location = ''niiri:coordinate_' strPeakId ''','])
    disp(['  prov:value = "' mat2str(TabDat.dat{i,9}) '" %% xsd:float,'])
    disp(['  nidm:equivalentZStatistic = "' mat2str(TabDat.dat{i,10}) '" %% xsd:float,'])
    disp(['  nidm:pValueUncorrected = "' mat2str(TabDat.dat{i,11}) '" %% xsd:float,'])
    disp(['  nidm:pValueFWER = "' mat2str(TabDat.dat{i,7}) '" %% xsd:float,'])
    disp(['  nidm:qValueFDR = "' mat2str(TabDat.dat{i,8}) '" %% xsd:float])'])
    disp(['entity(niiri:coordinate_' strPeakId ','])
    disp('  [prov:type = ''prov:Location'',')
    disp('  prov:type = ''nidm:Coordinate'',')
    disp(['  prov:label = "Coordinate: ' strPeakId '" %% xsd:string,'])
    disp(['  nidm:coordinate1 = "' mat2str(TabDat.dat{i,12}(1)) '" %% xsd:float,'])
    disp(['  nidm:coordinate2 = "' mat2str(TabDat.dat{i,12}(2)) '" %% xsd:float,'])
    disp(['  nidm:coordinate3 = "' mat2str(TabDat.dat{i,12}(3)) '" %% xsd:float])'])
    disp(['wasDerivedFrom(niiri:peak_' strPeakId ', niiri:cluster_' strClusterId ')   '])
end


