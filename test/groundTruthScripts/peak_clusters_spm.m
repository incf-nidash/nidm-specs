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
        disp(['  [prov:type = ''spm:clusterStatistic'','])
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
    disp('  [prov:type = ''spm:peakStatistic'',')
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